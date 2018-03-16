# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewProject.ui'
#
# Created: Thu Dec 01 14:59:38 2016
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

class Ui_NewProject(object):
    def setupUi(self, NewProject):
        NewProject.setObjectName(_fromUtf8("NewProject"))
        NewProject.resize(404, 70)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewProject.sizePolicy().hasHeightForWidth())
        NewProject.setSizePolicy(sizePolicy)
        NewProject.setMinimumSize(QtCore.QSize(404, 70))
        NewProject.setMaximumSize(QtCore.QSize(404, 70))
        self.Path = QtGui.QLineEdit(NewProject)
        self.Path.setGeometry(QtCore.QRect(100, 10, 241, 20))
        self.Path.setReadOnly(True)
        self.Path.setObjectName(_fromUtf8("Path"))
        self.SelectPath = QtGui.QToolButton(NewProject)
        self.SelectPath.setGeometry(QtCore.QRect(350, 10, 25, 21))
        self.SelectPath.setObjectName(_fromUtf8("SelectPath"))
        self.lineEdit = QtGui.QLineEdit(NewProject)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 81, 20))
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)
        #self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(NewProject)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setReadOnly(True)
        #self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.ProjectName = QtGui.QLineEdit(NewProject)
        self.ProjectName.setGeometry(QtCore.QRect(100, 40, 191, 20))
        self.ProjectName.setReadOnly(False)
        self.ProjectName.setObjectName(_fromUtf8("ProjectName"))
        self.OkButton = QtGui.QPushButton(NewProject)
        self.OkButton.setGeometry(QtCore.QRect(320, 40, 75, 23))
        self.OkButton.setObjectName(_fromUtf8("OkButton"))

        self.retranslateUi(NewProject)
        QtCore.QMetaObject.connectSlotsByName(NewProject)

    def retranslateUi(self, NewProject):
        NewProject.setWindowTitle(_translate("NewProject", "Nowy Projekt", None))
        self.Path.setText(_translate("NewProject", "...", None))
        self.SelectPath.setText(_translate("NewProject", "...", None))
        self.lineEdit.setText(_translate("NewProject", "Folder projektu", None))
        self.lineEdit_2.setText(_translate("NewProject", "Nazwa projektu", None))
        self.ProjectName.setText(_translate("NewProject", "MyProject", None))
        self.OkButton.setText(_translate("NewProject", "Ok", None))

