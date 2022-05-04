import sys, os, shutil
from PyQt5.QtWidgets import QApplication, QMainWindow
from app import *
from lxml import etree
import html

# Global variables
original_file = "stringtable.xml"
tempfile = "stringtable_translated.xml"
# File management
if os.path.exists(tempfile):
    os.remove(tempfile)
shutil.copy(original_file, tempfile)
# Core
tree = etree.parse(tempfile)
count_package = 0
count_key = 0
index = 0 # current index
project = ""
prev_line = 0
language = ""
# Table
package_names = []
key_names = []
key_original = [] # List of all key values of original language
key_values = [] # List of all key values of selected language
key_lines = []
package_names_unique = []
revision_mode = False
unescape_mode = True

# Qt5 Application
class Window(QMainWindow, Ui_MainWindow):
    
    # Qt5
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.previous_3.clicked.connect(self.previous)
        self.next_3.clicked.connect(self.next)
        self.confirm_3.clicked.connect(self.confirm)
        self.reset_3.clicked.connect(self.reset)
        self.languages_3.addItem("Select language")
        self.languages_3.addItem("English")
        self.languages_3.addItem("French")
        self.languages_3.addItem("Spanish")
        self.languages_3.addItem("German")
        self.languages_3.addItem("Russian")
        self.languages_3.addItem("Turkish")
        self.languages_3.addItem("Czech")
        self.languages_3.addItem("Portuguese")
        self.text_original_3.setPlainText("Please select a language from the dropdown above and click 'Confirm translation' to continue.")
        self.text_translation_3.setPlainText("Activate 'Revision Mode' to review previous translations for selected language.\nActivate 'Unescape HTML' to remove HTML tags from translation and original text (activated by default).")
    
    # Core Function
    first_launch = True
    # Qt5 Function
    def clear(self):
        self.text_original_3.setPlainText("")
        self.text_translation_3.setPlainText("")
        self.label_key_text_3.setText("")
        self.label_project_text_3.setText("")
        self.label_package_text_3.setText("")
        
    def previous(self):
        if not self.first_launch:
            global index
            index -= 1
            if index < 0:
                index = count_key - 1
            self.update(-1)
        
    def next(self):
        if not self.first_launch:
            global index
            index += 1
            if index > count_key - 1:
                index = 0
            self.update(1)
        
    def confirm(self):
        global count_package, count_key, key_original, key_values, package_names, key_names, project, package_names_unique
        if self.languages_3.currentText() != "Select language" and self.first_launch:
            # First launch
            self.first_launch = False
            self.clear()
            selected_language = self.languages_3.currentText()      
            global language
            language = selected_language
            # Initialisation of tables
            for projet in tree.xpath("/Project"):
                project = projet.attrib["name"]
            for package in tree.xpath("/Project/Package"):
                package_names_unique.append(package.attrib["name"])
                count_package += 1
            for key in tree.xpath("/Project/Package/Key"):
                key_names.append(key.attrib['ID'])
                # get parent name
                parent = key.getparent()
                package_parent = parent.attrib['name']
                package_names.append(package_parent)
                # get specific key
                original = tree.xpath("/Project/Package/Key[@ID='" + key.attrib['ID'] + "']/Original")[0]
                original2 = etree.tostring(original, encoding="utf-8").decode("utf-8")
                original2 = original2.replace("<Original>", "")
                original2 = original2.replace("</Original>", "")
                key_original.append(original2)
                if tree.xpath("/Project/Package/Key[@ID='" + key.attrib['ID'] + "']/" + selected_language): # Check if key has translation in selected language
                    translate = tree.xpath("/Project/Package/Key[@ID='" + key.attrib['ID'] + "']/" + selected_language)[0]
                    translate2 = etree.tostring(translate, encoding="utf-8").decode("utf-8")
                    translate2 = translate2.replace("<" + selected_language + ">", "")
                    translate2 = translate2.replace("</" + selected_language + ">", "")
                    key_values.append(translate2)
                else:
                    translate = ""
                    key_values.append(translate)
                count_key += 1
            # Display first element
            self.update_lines()
            self.update(1)
        elif not self.first_launch: # Not first launch
            text = self.text_translation_3.toPlainText()
            if text != "" and text != key_values[index]:
                translated_confirmed = self.text_translation_3.toPlainText()
                translated_confirmed = translated_confirmed.replace('\t', "")
                translated_confirmed = translated_confirmed.replace('\n', "")
                translated_initial = translated_confirmed
                translated_confirmed = "\t\t\t" + "<" + language + ">" + translated_confirmed + "</" + language + ">\n"
                with open(tempfile, "r", encoding="utf8") as file:
                    lines = file.readlines()
                if key_values[index] != "": # just modify if translation is not empty
                    lines[key_lines[index]-1] = translated_confirmed # Replace line with new translation
                    file = open(tempfile, "w", encoding="utf8")
                    file.writelines(lines)
                    file.close()
                else: # insert new translation
                    lines.insert(key_lines[index]-1, translated_confirmed)
                    file = open(tempfile, "w", encoding="utf8")
                    lines = "".join(lines)
                    file.writelines(lines)
                    file.close()
                key_values[index] = translated_initial
                self.update_lines() # probably not useful becose lines are already predicted
                self.next()

    def update_lines(self):
        global key_lines, prev_line
        key_lines = [] # reset table
        file = open(tempfile, "r", encoding="utf8")
        lines = file.readlines()
        line_number = 0
        for i in range(len(key_values)):
            line_count = 0
            new = False
            if key_values[i] == "": # if no translation exist for selected language and key
                #print(str(i+1) + ": no translation for key: " + key_original[i])
                phrase = key_original[i] # phrase to search in file is the original key
                new = True
            else:
                phrase = key_values[i] # phrase to search in file is the previously translated key
                #print(str(i+1) + ": translated key: " + phrase)
            phrase = phrase.replace('\t', "")
            phrase = phrase.replace('\n', "")
            # remove xml tag
            for line in lines:
                line = line.replace('\t', "")
                line = line.replace('\n', "")
                line_count += 1
                phrase = html.unescape(phrase)
                line = html.unescape(line)           
                if phrase in line and line_count > prev_line:
                    #file2.writelines("\t\tfound in line: " + str(line_count) + "\n")
                    if new:
                        line_number = line_count + 1 # line to which we will append new line
                    else:
                         line_number = line_count # line to which we will modify translation
                    prev_line = line_number
                    break
            key_lines.append(line_number)
    
    def update(self, way):
        global index, revision_mode, unescape_mode
        if self.checkBox_revision.isChecked():
            revision_mode = True
        else:
            revision_mode = False
        if self.checkBox_unescape.isChecked():
            unescape_mode = True
        else:
            unescape_mode = False
        while True:
            original_text = key_original[index]
            translated = key_values[index]
            if revision_mode or not revision_mode and translated == "":
                break
            else:
                if way == 1:
                    index += 1
                    if index > count_key - 1:
                        index = 0
                elif way == -1: # way = -1
                    index -= 1
                    if index < 0:
                        index = count_key - 1
        self.clear()
        if unescape_mode:
            original_text = html.unescape(original_text)
            translated = html.unescape(translated)
        self.text_translation_3.setPlainText(translated)
        self.text_original_3.setPlainText(original_text)
        self.label_key_text_3.setText(key_names[index] + " (" + str(index + 1) + "/" + str(count_key) + ")")
        self.label_project_text_3.setText(project)
        for i in range(len(package_names_unique)):
            if package_names[index] == package_names_unique[i]:
                self.label_package_text_3.setText(package_names_unique[i] + " (" + str(i + 1) + "/" + str(count_package) + ")")
                break
        value = round((index + 1) *100/ count_key)
        self.progressBar_3.setProperty("value", value)
                
    def reset(self):
        if not self.first_launch:
            self.update(0)    

# Qt5 Application main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())