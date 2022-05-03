import sys, os, shutil
from PyQt5.QtWidgets import QApplication, QMainWindow
from app import *
from lxml import etree

# Global variables
original_file = "stringtable.xml"
tempfile = "temp.xml"
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
# Table
package_names = []
key_names = []
key_original = [] # List of all key values of original language
key_values = [] # List of all key values of selected language
key_lines = []
package_names_unique = []
revision_mode = False

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
        self.languages_3.addItem("English")
        self.languages_3.addItem("French")
        self.languages_3.addItem("Spanish")
        self.languages_3.addItem("German")
        self.languages_3.addItem("Russian")
        self.languages_3.addItem("Turkish")
        self.languages_3.addItem("Czech")
        self.languages_3.addItem("Portuguese")
        self.text_original_3.setPlainText("Please select a language from the dropdown above and click 'Confirm translation' to continue.")
        self.text_translation_3.setPlainText("Activate 'Revision Mode' to review previous translations for selected language.")
    
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
        global index
        index -= 1
        if index < 0:
            index = count_key - 1
        self.update()
        
    def next(self):
        global index
        index += 1
        if index > count_key - 1:
            index = 0
        self.update()
        
    def confirm(self):
        global count_package, count_key, key_original, key_values, package_names, key_names, project, package_names_unique
        if self.languages_3.currentText() != "English" and self.first_launch:
            # First launch
            self.first_launch = False
            self.clear()
            selected_language = self.languages_3.currentText()
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
                original = tree.xpath("/Project/Package/Key[@ID='" + key.attrib['ID'] + "']/Original")[0].text
                key_original.append(original)
                if tree.xpath("/Project/Package/Key[@ID='" + key.attrib['ID'] + "']/" + selected_language): # Check if key has translation in selected language
                    translate = tree.xpath("/Project/Package/Key[@ID='" + key.attrib['ID'] + "']/" + selected_language)[0].text
                    key_values.append(translate)
                else:
                    translate = ""
                    key_values.append(translate)
                count_key += 1
            # Display first element
            self.update()
        else: # Not first launch
            text = self.text_translation_3.toPlainText()
            if text != "":
                print("write")
        
    def update_lines():
        global key_lines
        key_lines = [] # reset table
        file = open(tempfile, "r", encoding="utf8")
        lines = file.readlines()
        for i in range(len(key_values)):
            line_count = 0
            new = False
            if key_values[i] == "": # if no translation exist for selected language and key
                print(str(i+1) + ": no translation for key: " + key_original[i])
                phrase = key_original[i] # phrase to search in file is the original key
                new = True
            else:
                phrase = key_values[i] # phrase to search in file is the previously translated key
                print(str(i+1) + ": translated key: " + phrase)
            for line in lines:
                line_count += 1                      
                if phrase in line:
                    print("\t\tfound in line: " + str(line_count))
                    if new:
                        line_number = line_count + 1 # line to which we will append new line
                    else:
                         line_number = line_count # line to which we will modify translation
                    break
            key_lines.append(line_number)
    
    def update(self):
        global index, project, revision_mode
        if self.checkBox_revision.isChecked():
            revision_mode = True
        else:
            revision_mode = False
        while True:
            original_text = key_original[index]
            translated = key_values[index]
            if revision_mode or not revision_mode and translated == "":
                break
            else:
                index += 1
                if index > count_key - 1:
                    index = 0
        self.clear()
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
        self.update_lines()
        print(key_lines)
                
    def reset(self):
        self.update()    

# Qt5 Application main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())