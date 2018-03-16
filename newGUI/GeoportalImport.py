# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GeoportalImport.ui'
#
# Created: Sun Nov 13 02:23:52 2016
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

class Ui_GeoportalImport(object):
    def setupUi(self, GeoportalImport):
        GeoportalImport.setObjectName(_fromUtf8("GeoportalImport"))
        GeoportalImport.resize(407, 259)
        self.lineEdit = QtGui.QLineEdit(GeoportalImport)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 91, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(GeoportalImport)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 50, 91, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.OutputDir = QtGui.QLineEdit(GeoportalImport)
        self.OutputDir.setGeometry(QtCore.QRect(130, 20, 221, 20))
        self.OutputDir.setReadOnly(True)
        self.OutputDir.setObjectName(_fromUtf8("OutputDir"))
        self.OutputName = QtGui.QLineEdit(GeoportalImport)
        self.OutputName.setGeometry(QtCore.QRect(130, 50, 221, 20))
        self.OutputName.setObjectName(_fromUtf8("OutputName"))
        self.pushButton = QtGui.QPushButton(GeoportalImport)
        self.pushButton.setGeometry(QtCore.QRect(300, 220, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.XL = QtGui.QLineEdit(GeoportalImport)
        self.XL.setGeometry(QtCore.QRect(90, 120, 81, 20))
        self.XL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.XL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.XL.setObjectName(_fromUtf8("XL"))
        self.lineEdit_3 = QtGui.QLineEdit(GeoportalImport)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 120, 51, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.YL = QtGui.QLineEdit(GeoportalImport)
        self.YL.setGeometry(QtCore.QRect(250, 120, 81, 20))
        self.YL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YL.setObjectName(_fromUtf8("YL"))
        self.lineEdit_4 = QtGui.QLineEdit(GeoportalImport)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 120, 51, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.XP = QtGui.QLineEdit(GeoportalImport)
        self.XP.setGeometry(QtCore.QRect(90, 150, 81, 20))
        self.XP.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.XP.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.XP.setObjectName(_fromUtf8("XP"))
        self.lineEdit_5 = QtGui.QLineEdit(GeoportalImport)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 150, 51, 20))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.YP = QtGui.QLineEdit(GeoportalImport)
        self.YP.setGeometry(QtCore.QRect(250, 150, 81, 20))
        self.YP.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YP.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YP.setObjectName(_fromUtf8("YP"))
        self.lineEdit_6 = QtGui.QLineEdit(GeoportalImport)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 150, 51, 20))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(GeoportalImport)
        self.lineEdit_7.setGeometry(QtCore.QRect(30, 90, 113, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(GeoportalImport)
        self.lineEdit_8.setGeometry(QtCore.QRect(30, 190, 91, 20))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.ImPix = QtGui.QLineEdit(GeoportalImport)
        self.ImPix.setGeometry(QtCore.QRect(130, 190, 61, 20))
        self.ImPix.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ImPix.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImPix.setObjectName(_fromUtf8("ImPix"))
        self.SelectDir = QtGui.QPushButton(GeoportalImport)
        self.SelectDir.setGeometry(QtCore.QRect(360, 20, 21, 20))
        self.SelectDir.setObjectName(_fromUtf8("SelectDir"))
        self.SelectProjection = QtGui.QComboBox(GeoportalImport)
        self.SelectProjection.setGeometry(QtCore.QRect(150, 220, 61, 22))
        self.SelectProjection.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.SelectProjection.setObjectName(_fromUtf8("SelectProjection"))
        self.SelectProjection.addItem(_fromUtf8(""))
        self.SelectProjection.addItem(_fromUtf8(""))
        self.SelectProjection.addItem(_fromUtf8(""))
        self.SelectProjection.addItem(_fromUtf8(""))
        self.SelectProjection.addItem(_fromUtf8(""))
        self.lineEdit_9 = QtGui.QLineEdit(GeoportalImport)
        self.lineEdit_9.setGeometry(QtCore.QRect(30, 220, 111, 20))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))

        self.retranslateUi(GeoportalImport)
        QtCore.QMetaObject.connectSlotsByName(GeoportalImport)

    def retranslateUi(self, GeoportalImport):
        GeoportalImport.setWindowTitle(_translate("GeoportalImport", "Dialog", None))
        self.lineEdit.setText(_translate("GeoportalImport", "Folder docelowy", None))
        self.lineEdit_2.setText(_translate("GeoportalImport", "Nazwa:", None))
        self.OutputName.setText(_translate("GeoportalImport", "import", None))
        self.pushButton.setText(_translate("GeoportalImport", "Importuj", None))
        self.XL.setText(_translate("GeoportalImport", "387252", None))
        self.lineEdit_3.setText(_translate("GeoportalImport", "X lewy", None))
        self.YL.setText(_translate("GeoportalImport", "580040", None))
        self.lineEdit_4.setText(_translate("GeoportalImport", "Y lewy", None))
        self.XP.setText(_translate("GeoportalImport", "387300", None))
        self.lineEdit_5.setText(_translate("GeoportalImport", "Y prawy", None))
        self.YP.setText(_translate("GeoportalImport", "580120", None))
        self.lineEdit_6.setText(_translate("GeoportalImport", "X prawy", None))
        self.lineEdit_7.setText(_translate("GeoportalImport", "Współrzędne naroży:", None))
        self.lineEdit_8.setText(_translate("GeoportalImport", "Piksel obrazu [m]", None))
        self.ImPix.setText(_translate("GeoportalImport", "0.1", None))
        self.SelectDir.setText(_translate("GeoportalImport", "...", None))
        self.SelectProjection.setItemText(0, _translate("GeoportalImport", "92", None))
        self.SelectProjection.setItemText(1, _translate("GeoportalImport", "2000 s. V", None))
        self.SelectProjection.setItemText(2, _translate("GeoportalImport", "2000 s. VI", None))
        self.SelectProjection.setItemText(3, _translate("GeoportalImport", "2000 s. VII", None))
        self.SelectProjection.setItemText(4, _translate("GeoportalImport", "2000 s. VIII", None))
        self.lineEdit_9.setText(_translate("GeoportalImport", "Układ współrzędnych", None))

