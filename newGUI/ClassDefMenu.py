# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClassDefMenu.ui'
#
# Created: Thu Dec 08 16:30:53 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ClassDefinition(object):
    def setupUi(self, ClassDefinition):
        ClassDefinition.setObjectName(_fromUtf8("ClassDefinition"))
        ClassDefinition.resize(130, 249)
        self.ClassList = QtGui.QListWidget(ClassDefinition)
        self.ClassList.setGeometry(QtCore.QRect(0, 20, 121, 151))
        self.ClassList.setObjectName(_fromUtf8("ClassList"))
        self.lineEdit = QtGui.QLineEdit(ClassDefinition)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.AddClass = QtGui.QPushButton(ClassDefinition)
        self.AddClass.setGeometry(QtCore.QRect(10, 180, 91, 23))
        self.AddClass.setObjectName(_fromUtf8("AddClass"))
        self.DrawClass = QtGui.QPushButton(ClassDefinition)
        self.DrawClass.setGeometry(QtCore.QRect(10, 210, 91, 23))
        self.DrawClass.setObjectName(_fromUtf8("DrawClass"))

        self.retranslateUi(ClassDefinition)
        QtCore.QMetaObject.connectSlotsByName(ClassDefinition)

    def retranslateUi(self, ClassDefinition):
        ClassDefinition.setWindowTitle(_translate("ClassDefinition", "Dialog", None))
        self.lineEdit.setText(_translate("ClassDefinition", " Klasy:", None))
        self.AddClass.setText(_translate("ClassDefinition", "Dodaj klasę", None))
        self.DrawClass.setToolTip(_translate("ClassDefinition", "Aby zaznaczyć obszar zaznacz klasę i otwórz zdjęcie z menu głównego", None))
        self.DrawClass.setText(_translate("ClassDefinition", "Zaznacz obszar", None))

