# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewClassMenu.ui'
#
# Created: Wed Nov 16 15:58:10 2016
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

class Ui_NewClass(object):
    def setupUi(self, NewClass):
        NewClass.setObjectName(_fromUtf8("NewClass"))
        NewClass.resize(171, 68)
        NewClass.setMinimumSize(QtCore.QSize(171, 68))
        NewClass.setMaximumSize(QtCore.QSize(171, 68))
        self.OKButton = QtGui.QPushButton(NewClass)
        self.OKButton.setGeometry(QtCore.QRect(90, 40, 75, 23))
        self.OKButton.setObjectName(_fromUtf8("OKButton"))
        self.ClassName = QtGui.QLineEdit(NewClass)
        self.ClassName.setGeometry(QtCore.QRect(10, 10, 151, 20))
        self.ClassName.setObjectName(_fromUtf8("ClassName"))

        self.retranslateUi(NewClass)
        QtCore.QMetaObject.connectSlotsByName(NewClass)

    def retranslateUi(self, NewClass):
        NewClass.setWindowTitle(_translate("NewClass", "Nowa Klasa", None))
        self.OKButton.setText(_translate("NewClass", "Dodaj", None))
        self.ClassName.setText(_translate("NewClass", "nowa", None))

