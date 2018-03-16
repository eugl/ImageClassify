# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClassifyMenu.ui'
#
# Created: Tue Apr 25 00:26:25 2017
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

class Ui_Classify(object):
    def setupUi(self, Classify):
        Classify.setObjectName(_fromUtf8("Classify"))
        Classify.resize(400, 242)
        self.AllPhotos = QtGui.QListWidget(Classify)
        self.AllPhotos.setGeometry(QtCore.QRect(30, 30, 151, 151))
        self.AllPhotos.setInputMethodHints(QtCore.Qt.ImhNone)
        self.AllPhotos.setFrameShape(QtGui.QFrame.StyledPanel)
        self.AllPhotos.setFrameShadow(QtGui.QFrame.Sunken)
        self.AllPhotos.setLineWidth(4)
        self.AllPhotos.setMidLineWidth(1)
        self.AllPhotos.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.AllPhotos.setSelectionRectVisible(True)
        self.AllPhotos.setObjectName(_fromUtf8("AllPhotos"))
        self.ClassifyButton = QtGui.QPushButton(Classify)
        self.ClassifyButton.setEnabled(False)
        self.ClassifyButton.setGeometry(QtCore.QRect(300, 200, 75, 23))
        self.ClassifyButton.setObjectName(_fromUtf8("ClassifyButton"))
        self.lineEdit = QtGui.QLineEdit(Classify)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(150, 10, 113, 20))
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        #self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.SelectedPhotos = QtGui.QListWidget(Classify)
        self.SelectedPhotos.setGeometry(QtCore.QRect(220, 30, 151, 151))
        self.SelectedPhotos.setInputMethodHints(QtCore.Qt.ImhNone)
        self.SelectedPhotos.setFrameShape(QtGui.QFrame.StyledPanel)
        self.SelectedPhotos.setFrameShadow(QtGui.QFrame.Sunken)
        self.SelectedPhotos.setLineWidth(4)
        self.SelectedPhotos.setMidLineWidth(1)
        self.SelectedPhotos.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.SelectedPhotos.setSelectionRectVisible(True)
        self.SelectedPhotos.setObjectName(_fromUtf8("SelectedPhotos"))
        self.SelectPhotos = QtGui.QPushButton(Classify)
        self.SelectPhotos.setGeometry(QtCore.QRect(185, 30, 31, 23))
        self.SelectPhotos.setObjectName(_fromUtf8("SelectPhotos"))
        self.DeletePhotos = QtGui.QPushButton(Classify)
        self.DeletePhotos.setGeometry(QtCore.QRect(185, 60, 31, 23))
        self.DeletePhotos.setObjectName(_fromUtf8("DeletePhotos"))
        self.checkSieve = QtGui.QCheckBox(Classify)
        self.checkSieve.setGeometry(QtCore.QRect(30, 190, 141, 17))
        self.checkSieve.setObjectName(_fromUtf8("checkSieve"))
        self.lineEdit_2 = QtGui.QLineEdit(Classify)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 210, 121, 20))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.minAreaSize = QtGui.QLineEdit(Classify)
        self.minAreaSize.setEnabled(False)
        self.minAreaSize.setGeometry(QtCore.QRect(150, 210, 51, 20))
        self.minAreaSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.minAreaSize.setObjectName(_fromUtf8("minAreaSize"))

        self.retranslateUi(Classify)
        QtCore.QMetaObject.connectSlotsByName(Classify)

    def retranslateUi(self, Classify):
        Classify.setWindowTitle(_translate("Classify", "Klasyfikacja", None))
        self.ClassifyButton.setText(_translate("Classify", "Klasyfikuj", None))
        self.lineEdit.setText(_translate("Classify", "Wybierz zdjęcia", None))
        self.SelectPhotos.setText(_translate("Classify", ">>", None))
        self.DeletePhotos.setText(_translate("Classify", "<<", None))
        self.checkSieve.setText(_translate("Classify", "Usuwaj małe obszary", None))
        self.lineEdit_2.setText(_translate("Classify", "Minimalna wielkość [pix]:", None))
        self.minAreaSize.setText(_translate("Classify", "0", None))

