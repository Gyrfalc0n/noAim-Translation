# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 671)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.box_translation = QtWidgets.QGroupBox(self.centralwidget)
        self.box_translation.setGeometry(QtCore.QRect(0, 330, 1045, 158))
        self.box_translation.setObjectName("box_translation")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.text_translation_3 = QtWidgets.QPlainTextEdit(self.box_translation)
        self.text_translation_3.setGeometry(QtCore.QRect(10, 20, 1021, 131))
        self.text_translation_3.setObjectName("text_translation_3")
        self.box_actions = QtWidgets.QGroupBox(self.centralwidget)
        self.box_actions.setGeometry(QtCore.QRect(0, 494, 1045, 159))
        self.box_actions.setObjectName("box_actions")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.box_actions)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_left_3 = QtWidgets.QFrame(self.box_actions)
        self.frame_left_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_3.setObjectName("frame_left_3")
        self.progressBar_3 = QtWidgets.QProgressBar(self.frame_left_3)
        self.progressBar_3.setGeometry(QtCore.QRect(0, 70, 501, 25))
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_3.setFont(font)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_3.setInvertedAppearance(True)
        self.progressBar_3.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_3.setObjectName("progressBar_3")
        self.copyright_3 = QtWidgets.QLabel(self.frame_left_3)
        self.copyright_3.setGeometry(QtCore.QRect(0, 100, 101, 16))
        self.copyright_3.setObjectName("copyright_3")
        self.checkBox_revision = QtWidgets.QCheckBox(self.frame_left_3)
        self.checkBox_revision.setGeometry(QtCore.QRect(10, 10, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.checkBox_revision.setFont(font)
        self.checkBox_revision.setObjectName("checkBox_revision")
        self.horizontalLayout_5.addWidget(self.frame_left_3)
        self.frame_right_3 = QtWidgets.QFrame(self.box_actions)
        self.frame_right_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_right_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_right_3.setObjectName("frame_right_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_right_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_nav_3 = QtWidgets.QFrame(self.frame_right_3)
        self.frame_nav_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_nav_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_nav_3.setObjectName("frame_nav_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_nav_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.previous_3 = QtWidgets.QPushButton(self.frame_nav_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.previous_3.setFont(font)
        self.previous_3.setCheckable(False)
        self.previous_3.setFlat(False)
        self.previous_3.setObjectName("previous_3")
        self.verticalLayout_6.addWidget(self.previous_3)
        self.next_3 = QtWidgets.QPushButton(self.frame_nav_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.next_3.setFont(font)
        self.next_3.setObjectName("next_3")
        self.verticalLayout_6.addWidget(self.next_3)
        self.horizontalLayout_6.addWidget(self.frame_nav_3)
        self.frame_boutons_3 = QtWidgets.QFrame(self.frame_right_3)
        self.frame_boutons_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_boutons_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_boutons_3.setObjectName("frame_boutons_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_boutons_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.confirm_3 = QtWidgets.QPushButton(self.frame_boutons_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.confirm_3.setFont(font)
        self.confirm_3.setObjectName("confirm_3")
        self.verticalLayout_7.addWidget(self.confirm_3)
        self.reset_3 = QtWidgets.QPushButton(self.frame_boutons_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.reset_3.setFont(font)
        self.reset_3.setObjectName("reset_3")
        self.verticalLayout_7.addWidget(self.reset_3)
        self.horizontalLayout_6.addWidget(self.frame_boutons_3)
        self.horizontalLayout_5.addWidget(self.frame_right_3)
        self.box_original = QtWidgets.QGroupBox(self.centralwidget)
        self.box_original.setGeometry(QtCore.QRect(0, 165, 1045, 159))
        self.box_original.setObjectName("box_original")
        self.text_original_3 = QtWidgets.QPlainTextEdit(self.box_original)
        self.text_original_3.setGeometry(QtCore.QRect(10, 20, 1021, 131))
        self.text_original_3.setReadOnly(True)
        self.text_original_3.setObjectName("text_original_3")
        self.box_infos = QtWidgets.QGroupBox(self.centralwidget)
        self.box_infos.setGeometry(QtCore.QRect(0, 0, 1045, 159))
        self.box_infos.setObjectName("box_infos")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.box_infos)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_package_text_3 = QtWidgets.QLabel(self.box_infos)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(False)
        self.label_package_text_3.setFont(font)
        self.label_package_text_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_package_text_3.setObjectName("label_package_text_3")
        self.gridLayout_3.addWidget(self.label_package_text_3, 4, 1, 1, 1)
        self.label_project_3 = QtWidgets.QLabel(self.box_infos)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_project_3.setFont(font)
        self.label_project_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_project_3.setObjectName("label_project_3")
        self.gridLayout_3.addWidget(self.label_project_3, 2, 0, 1, 1)
        self.label_package_3 = QtWidgets.QLabel(self.box_infos)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_package_3.setFont(font)
        self.label_package_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_package_3.setObjectName("label_package_3")
        self.gridLayout_3.addWidget(self.label_package_3, 2, 1, 1, 1)
        self.label_project_text_3 = QtWidgets.QLabel(self.box_infos)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(False)
        self.label_project_text_3.setFont(font)
        self.label_project_text_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_project_text_3.setObjectName("label_project_text_3")
        self.gridLayout_3.addWidget(self.label_project_text_3, 4, 0, 1, 1)
        self.label_key_3 = QtWidgets.QLabel(self.box_infos)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_key_3.setFont(font)
        self.label_key_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_key_3.setObjectName("label_key_3")
        self.gridLayout_3.addWidget(self.label_key_3, 2, 2, 1, 1)
        self.label_key_text_3 = QtWidgets.QLabel(self.box_infos)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.label_key_text_3.setFont(font)
        self.label_key_text_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_key_text_3.setObjectName("label_key_text_3")
        self.gridLayout_3.addWidget(self.label_key_text_3, 4, 2, 1, 1)
        self.label_language_3 = QtWidgets.QLabel(self.box_infos)
        self.label_language_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_language_3.setObjectName("label_language_3")
        self.gridLayout_3.addWidget(self.label_language_3, 4, 3, 1, 1)
        self.languages_3 = QtWidgets.QComboBox(self.box_infos)
        self.languages_3.setCurrentText("")
        self.languages_3.setObjectName("languages_3")
        self.gridLayout_3.addWidget(self.languages_3, 3, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.reset_3.clicked.connect(self.reset_3.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.text_translation_3, self.confirm_3)
        MainWindow.setTabOrder(self.confirm_3, self.previous_3)
        MainWindow.setTabOrder(self.previous_3, self.next_3)
        MainWindow.setTabOrder(self.next_3, self.reset_3)
        MainWindow.setTabOrder(self.reset_3, self.languages_3)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "noAim Translator"))
        self.box_translation.setTitle(_translate("MainWindow", "TRANSLATION"))
        self.box_actions.setTitle(_translate("MainWindow", "ACTIONS"))
        self.copyright_3.setText(_translate("MainWindow", "v1.0 Gyrfalcon"))
        self.checkBox_revision.setText(_translate("MainWindow", "Revision mode"))
        self.previous_3.setText(_translate("MainWindow", "Previous text"))
        self.next_3.setText(_translate("MainWindow", "Next text"))
        self.confirm_3.setText(_translate("MainWindow", "Confirm translation"))
        self.reset_3.setText(_translate("MainWindow", "Reset current text"))
        self.box_original.setTitle(_translate("MainWindow", "ORIGINAL TEXT"))
        self.box_infos.setTitle(_translate("MainWindow", "INFORMATIONS"))
        self.label_package_text_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_project_3.setText(_translate("MainWindow", "Project"))
        self.label_package_3.setText(_translate("MainWindow", "Package"))
        self.label_project_text_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_key_3.setText(_translate("MainWindow", "Key"))
        self.label_key_text_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_language_3.setText(_translate("MainWindow", "Language to translate to"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
