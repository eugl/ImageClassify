# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConvertToSHPMenu.ui'
#
# Created: Tue Nov 29 14:13:37 2016
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

class Ui_ConvertToSHP(object):
    def setupUi(self, ConvertToSHP):
        ConvertToSHP.setObjectName(_fromUtf8("ConvertToSHP"))
        ConvertToSHP.resize(400, 242)
        self.AllPhotos = QtGui.QListWidget(ConvertToSHP)
        self.AllPhotos.setGeometry(QtCore.QRect(30, 30, 151, 151))
        self.AllPhotos.setInputMethodHints(QtCore.Qt.ImhNone)
        self.AllPhotos.setFrameShape(QtGui.QFrame.StyledPanel)
        self.AllPhotos.setFrameShadow(QtGui.QFrame.Sunken)
        self.AllPhotos.setLineWidth(4)
        self.AllPhotos.setMidLineWidth(1)
        self.AllPhotos.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.AllPhotos.setSelectionRectVisible(True)
        self.AllPhotos.setObjectName(_fromUtf8("AllPhotos"))
        self.ConversionButton = QtGui.QPushButton(ConvertToSHP)
        self.ConversionButton.setEnabled(False)
        self.ConversionButton.setGeometry(QtCore.QRect(300, 200, 75, 23))
        self.ConversionButton.setObjectName(_fromUtf8("ConversionButton"))
        self.lineEdit = QtGui.QLineEdit(ConvertToSHP)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 161, 20))
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        #self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.SelectedPhotos = QtGui.QListWidget(ConvertToSHP)
        self.SelectedPhotos.setGeometry(QtCore.QRect(220, 30, 151, 151))
        self.SelectedPhotos.setInputMethodHints(QtCore.Qt.ImhNone)
        self.SelectedPhotos.setFrameShape(QtGui.QFrame.StyledPanel)
        self.SelectedPhotos.setFrameShadow(QtGui.QFrame.Sunken)
        self.SelectedPhotos.setLineWidth(4)
        self.SelectedPhotos.setMidLineWidth(1)
        self.SelectedPhotos.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.SelectedPhotos.setSelectionRectVisible(True)
        self.SelectedPhotos.setObjectName(_fromUtf8("SelectedPhotos"))
        self.SelectPhotos = QtGui.QPushButton(ConvertToSHP)
        self.SelectPhotos.setGeometry(QtCore.QRect(185, 30, 31, 23))
        self.SelectPhotos.setObjectName(_fromUtf8("SelectPhotos"))
        self.DeletePhotos = QtGui.QPushButton(ConvertToSHP)
        self.DeletePhotos.setGeometry(QtCore.QRect(185, 60, 31, 23))
        self.DeletePhotos.setObjectName(_fromUtf8("DeletePhotos"))

        self.retranslateUi(ConvertToSHP)
        QtCore.QMetaObject.connectSlotsByName(ConvertToSHP)

    def retranslateUi(self, ConvertToSHP):
        ConvertToSHP.setWindowTitle(_translate("ConvertToSHP", "Konwersja do SHP", None))
        self.ConversionButton.setText(_translate("ConvertToSHP", "Konwertuj", None))
        self.lineEdit.setText(_translate("ConvertToSHP", "Wybierz rastry do konwersji", None))
        self.SelectPhotos.setText(_translate("ConvertToSHP", ">>", None))
        self.DeletePhotos.setText(_translate("ConvertToSHP", "<<", None))

