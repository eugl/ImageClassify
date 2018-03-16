# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created: Tue Nov 08 15:04:26 2016
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(395, 261)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.projectName = QtGui.QLineEdit(self.centralwidget)
        self.projectName.setGeometry(QtCore.QRect(60, 220, 331, 20))
        self.projectName.setFrame(False)
        self.projectName.setReadOnly(True)
        self.projectName.setObjectName(_fromUtf8("projectName"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 220, 60, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(60, 20))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(60, 20))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.Frame = QtGui.QFrame(self.centralwidget)
        self.Frame.setGeometry(QtCore.QRect(270, 20, 120, 80))
        self.Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.Frame.setObjectName(_fromUtf8("Frame"))
        self.PhotoList = QtGui.QListWidget(self.centralwidget)
        self.PhotoList.setGeometry(QtCore.QRect(0, 20, 256, 91))
        #self.PhotoList.setSizeAdjustPolicy(QtGui.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.PhotoList.setObjectName(_fromUtf8("PhotoList"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 121, 20))
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.ClassifiedList = QtGui.QListWidget(self.centralwidget)
        self.ClassifiedList.setGeometry(QtCore.QRect(0, 130, 256, 91))
        #self.ClassifiedList.setSizeAdjustPolicy(QtGui.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.ClassifiedList.setObjectName(_fromUtf8("ClassifiedList"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 110, 121, 20))
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 395, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuPlik = QtGui.QMenu(self.menubar)
        self.menuPlik.setObjectName(_fromUtf8("menuPlik"))
        self.menuNarz_dzia = QtGui.QMenu(self.menubar)
        self.menuNarz_dzia.setEnabled(False)
        self.menuNarz_dzia.setObjectName(_fromUtf8("menuNarz_dzia"))
        self.menuImport = QtGui.QMenu(self.menubar)
        self.menuImport.setEnabled(False)
        self.menuImport.setObjectName(_fromUtf8("menuImport"))
        self.menuPomoc = QtGui.QMenu(self.menubar)
        self.menuPomoc.setObjectName(_fromUtf8("menuPomoc"))
        MainWindow.setMenuBar(self.menubar)
        self.actionNewProject = QtGui.QAction(MainWindow)
        self.actionNewProject.setObjectName(_fromUtf8("actionNewProject"))
        self.actionOpenProject = QtGui.QAction(MainWindow)
        self.actionOpenProject.setObjectName(_fromUtf8("actionOpenProject"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionClassDefinition = QtGui.QAction(MainWindow)
        self.actionClassDefinition.setEnabled(True)
        self.actionClassDefinition.setObjectName(_fromUtf8("actionClassDefinition"))
        self.actionClassify = QtGui.QAction(MainWindow)
        self.actionClassify.setObjectName(_fromUtf8("actionClassify"))
        self.actionConvertToSHP = QtGui.QAction(MainWindow)
        self.actionConvertToSHP.setObjectName(_fromUtf8("actionConvertToSHP"))
        self.actionFromFile = QtGui.QAction(MainWindow)
        self.actionFromFile.setEnabled(True)
        self.actionFromFile.setObjectName(_fromUtf8("actionFromFile"))
        self.actionFromGeoportal = QtGui.QAction(MainWindow)
        self.actionFromGeoportal.setObjectName(_fromUtf8("actionFromGeoportal"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuPlik.addAction(self.actionNewProject)
        self.menuPlik.addAction(self.actionOpenProject)
        self.menuPlik.addAction(self.actionExit)
        self.menuNarz_dzia.addAction(self.actionClassDefinition)
        self.menuNarz_dzia.addAction(self.actionClassify)
        self.menuNarz_dzia.addAction(self.actionConvertToSHP)
        self.menuImport.addAction(self.actionFromFile)
        self.menuImport.addAction(self.actionFromGeoportal)
        self.menuPomoc.addAction(self.actionAbout)
        self.menubar.addAction(self.menuPlik.menuAction())
        self.menubar.addAction(self.menuNarz_dzia.menuAction())
        self.menubar.addAction(self.menuImport.menuAction())
        self.menubar.addAction(self.menuPomoc.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lineEdit_2.setText(_translate("MainWindow", " Projekt:", None))
        self.PhotoList.setSortingEnabled(True)
        self.lineEdit.setText(_translate("MainWindow", "Zaimportowane obrazy:", None))
        self.ClassifiedList.setSortingEnabled(True)
        self.lineEdit_3.setText(_translate("MainWindow", "Sklasyfikowane obrazy:", None))
        self.menuPlik.setTitle(_translate("MainWindow", "Plik", None))
        self.menuNarz_dzia.setTitle(_translate("MainWindow", "Narzędzia", None))
        self.menuImport.setTitle(_translate("MainWindow", "Import zdjęć", None))
        self.menuPomoc.setTitle(_translate("MainWindow", "Pomoc", None))
        self.actionNewProject.setText(_translate("MainWindow", "Nowy projekt", None))
        self.actionOpenProject.setText(_translate("MainWindow", "Otwórz projekt", None))
        self.actionExit.setText(_translate("MainWindow", "Zakończ", None))
        self.actionClassDefinition.setText(_translate("MainWindow", "Definicja klas", None))
        self.actionClassify.setText(_translate("MainWindow", "Klasyfikacja", None))
        self.actionConvertToSHP.setText(_translate("MainWindow", "Konwersja do .shp", None))
        self.actionFromFile.setText(_translate("MainWindow", "Z pliku", None))
        self.actionFromGeoportal.setText(_translate("MainWindow", "Z geoportalu", None))
        self.actionAbout.setText(_translate("MainWindow", "O programie", None))

