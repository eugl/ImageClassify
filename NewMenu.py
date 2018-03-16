#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from sys import argv
from sys import exit
from PyQt4 import QtCore, QtGui
from newGUI.MainMenu import Ui_MainWindow
from newGUI.NewProject import Ui_NewProject
from newGUI.ClassDefMenu import Ui_ClassDefinition
from newGUI.GeoportalImport import Ui_GeoportalImport
from newGUI.NewClassMenu import Ui_NewClass
from newGUI.ClassifyMenu import Ui_Classify
from newGUI.ConvertToSHPMenu import Ui_ConvertToSHP
import matplotlib.image as mpi
import matplotlib.pyplot as mpp
from PyQt4.QtCore import QString
from matplotlib import patches
from matplotlib.path import Path
import numpy as np
import gdal
from math import floor
from operator import itemgetter
import Classify
from PIL import Image, ImageDraw

class Menu(QtGui.QMainWindow):
    classPath = ''
    prjPath = ''
    fig = 0
    image = 0
    photoDir = ''
    outputDir = ''

    @QtCore.pyqtSlot()
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.PhotoList,QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.showImage)
        QtCore.QObject.connect(self.ui.ClassifiedList,QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.showRaster)

    @QtCore.pyqtSlot()
    def on_actionNewProject_triggered(self):
        NewProjectMenu(self).show()

    @QtCore.pyqtSlot()
    def on_actionOpenProject_triggered(self):
        self.ui.PhotoList.clear()
        self.ui.projectName.clear()
        self.ui.menuImport.setEnabled(False)
        self.ui.menuNarz_dzia.setEnabled(False)
        projectPath = str(QtGui.QFileDialog.getExistingDirectory(self, "Wybierz folder projektu", QtCore.QDir.currentPath()))
        if projectPath:
            prjName = projectPath[projectPath.rfind('\\')+1:]
            self.classPath = projectPath + '\\' + 'klasy.txt'
            self.prjPath = projectPath + '\\' + prjName + '.txt'
            self.outputDir = projectPath + '\\' + 'Sklasyfikowane'
            try:
                open(self.classPath).close()
            except:
                QtGui.QMessageBox.warning(self,QString.fromUtf8('Błąd','Brak pliku klas!'),'Ok')
                return 0
            try:
                projectFile = open(self.prjPath)
                imagesList = projectFile.read().splitlines()
                projectFile.close()
                try:
                    for image in imagesList:
                        mpi.imread(image)
                        imName = image[image.rfind('\\')+1:]
                        item = QtGui.QListWidgetItem(self.ui.PhotoList)
                        item.setText(imName)
                        item.setToolTip(image)
                    if imagesList:
                        self.ui.menuNarz_dzia.setEnabled(True)
                    self.ui.menuImport.setEnabled(True)
                    self.ui.projectName.setText(self.prjPath)
                except Exception,e:
                    print str(e)
                    QtGui.QMessageBox.warning(self,QString.fromUtf8('Bład'),QString.fromUtf8('Niepoprawne dane zdjęć w pliku projektu!'),'Ok')
            except Exception,e:
                print str(e)
                QtGui.QMessageBox.warning(self,QString.fromUtf8('Bład','Brak pliku projektu!'),'Ok')
                return 0
            try:
                classifiedFiles = os.listdir(''.join((projectPath,'\\Sklasyfikowane')))
                for file in classifiedFiles:
                    ext = file[file.rfind('.')+1:]
                    if ext=='tiff':
                        filePath = ''.join((projectPath,'\\Sklasyfikowane\\',file))
                        item = QtGui.QListWidgetItem(self.ui.ClassifiedList)
                        item.setText(file)
                        item.setToolTip(filePath)
            except Exception,e:
                print str(e)

    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        reply = QtGui.QMessageBox.question(self, '', QString.fromUtf8('Czy na pewno chcesz zanończyć?'), 'Nie', 'Tak')
        if reply:
           exit()

    @QtCore.pyqtSlot()
    def on_actionFromFile_triggered(self):
        image = str(QtGui.QFileDialog.getOpenFileName(self, "Open File", QtCore.QDir.currentPath()))
        if image:
            try:
                mpi.imread(image)
                self.writeToPrj(image)
                imName = image[image.rfind('/')+1:]
                item = QtGui.QListWidgetItem(self.ui.PhotoList)
                item.setText(imName)
                item.setToolTip(image)
                self.ui.menuNarz_dzia.setEnabled(True)
            except Exception,e:
                print str(e)
                QtGui.QMessageBox.warning(self,QString.fromUtf8('Błąd'),QString.fromUtf8('Niepoprawny plik obrazu!'),'Ok')

    @QtCore.pyqtSlot()
    def on_actionFromGeoportal_triggered(self):
        GeoportalImportMenu(self).show()

    @QtCore.pyqtSlot()
    def on_actionClassDefinition_triggered(self):
        classDef = ClassDefinitionMenu(self)
        classDef.setGeometry(QtCore.QRect(180,220,150,250))
        classDef.show()

    @QtCore.pyqtSlot()
    def on_actionClassify_triggered(self):
        ClassifyMenu(self).show()

    @QtCore.pyqtSlot()
    def on_actionConvertToSHP_triggered(self):
        ConvertToSHPMenu(self).show()

    def writeToPrj(self, content):
        content = list(content)
        for i in range(len(content)):
            if content[i]=='/':
                content[i] = '\\'
        projectFile = open(self.prjPath, 'a')
        projectFile.write(''.join(content) + '\n')
        projectFile.close()

    def showImage(self, item):
        self.setVisible(False)
        imPath = str(item.toolTip())
        mpp.ion()
        self.fig = mpp.figure(imPath)
        self.image = np.array(readImage(imPath))
        mpp.imshow(self.image)
        self.fig.canvas.mpl_connect('close_event', self.closeFig)

    def showRaster(self, item):
        self.setVisible(False)
        imPath = str(item.toolTip())
        mpp.ion()
        self.fig = mpp.figure(imPath)
        self.image = gdal.Open(imPath)
        imageBand = self.image.GetRasterBand(1).ReadAsArray()
        imageRAT = self.image.GetRasterBand(1).GetDefaultRAT()
        n = imageRAT.GetRowCount()
        values = []
        ticks = []
        for i in range(n):
            values.append(imageRAT.GetValueAsString(i, 1))
            ticks.append(i)
        print  n, values
        cmap = mpp.get_cmap('Accent', n)
        cax = mpp.imshow(imageBand, cmap=cmap)
        cbar = mpp.colorbar(cax, ticks=ticks, orientation='horizontal')
        cbar.ax.set_xticklabels(values)
        #mpp.colorbar(cax)
        self.fig.canvas.mpl_connect('close_event', self.closeFig)

    def closeFig(self, evt):
        self.setVisible(True)
        self.fig = 0


class NewProjectMenu(QtGui.QMainWindow):

    def __init__(self, parent=Menu):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_NewProject()
        self.ui.setupUi(self)
        self.ui.Path.setText(os.path.expanduser("~\\Desktop"))

    @QtCore.pyqtSlot()
    def on_SelectPath_released(self):
        projectPath = str(QtGui.QFileDialog.getExistingDirectory(self, "Wybierz folder docelowy", QtCore.QDir.currentPath()))
        self.ui.Path.setText(projectPath)

    @QtCore.pyqtSlot()
    def on_OkButton_released(self):
        self.parent().ui.PhotoList.clear()
        self.parent().ui.projectName.clear()
        self.parent().ui.menuImport.setEnabled(False)
        self.parent().ui.menuNarz_dzia.setEnabled(False)
        projectName = str(self.ui.ProjectName.text())
        projectPath = str((self.ui.Path.text()))
        path = projectPath + '\\' + projectName
        self.parent().outputDir = path + '\\' + 'Sklasyfikowane'
        if os.path.exists(path):
            QtGui.QMessageBox.warning(self,QString.fromUtf8('Błąd'),QString.fromUtf8('Folder o tej nazwie już istnieje!'),'OK')
            return 0
        else:
            os.makedirs(path)
            os.makedirs(self.parent().outputDir)
            self.parent().classPath = path + '\\' + 'klasy.txt'
            classFile = open(self.parent().classPath, 'a')
            classFile.write('h s v veg ent\n')
            classFile.close()
            self.parent().prjPath = path + '\\' + projectName + '.txt'
            prjFile = open(self.parent().prjPath, 'a')
            prjFile.close()
            self.parent().ui.projectName.setText(path)
            self.parent().ui.menuImport.setEnabled(True)
            self.close()


class GeoportalImportMenu(QtGui.QMainWindow):

    def __init__(self, parent=Menu):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_GeoportalImport()
        self.ui.setupUi(self)
        path = str(self.parent().ui.projectName.text())
        dirPath = path[0:path.rfind('\\')]
        self.ui.OutputDir.setText(dirPath)

    @QtCore.pyqtSlot()
    def on_SelectDir_released(self):
        outputPath = str(QtGui.QFileDialog.getExistingDirectory(self, "Wybierz folder docelowy", QtCore.QDir.currentPath()))
        self.ui.OutputDir.setText(outputPath)

    @QtCore.pyqtSlot()
    def on_pushButton_released(self):
        path = str(self.ui.OutputDir.text()) + '\\' + str(self.ui.OutputName.text()) + '.tiff'
        if os.path.isfile(path):
            QtGui.QMessageBox.warning(self,QString.fromUtf8('Błąd'),QString.fromUtf8('Plik o tej nazwie już istnieje!'),'Ok')
            return
        Xmin = float(self.ui.XL.text())
        Ymin = float(self.ui.YL.text())
        Xmax = float(self.ui.XP.text())
        Ymax = float(self.ui.YP.text())
        pix = float(self.ui.ImPix.text())
        crs = str(self.ui.SelectProjection.currentText())
        crs, epsg = self.selectCRS(crs)
        result = Classify.importFromGeoportal(self, path, Xmin, Ymin, Xmax, Ymax, pix, crs, epsg)
        if result:
            item = QtGui.QListWidgetItem(self.parent().ui.PhotoList)
            item.setText(str(self.ui.OutputName.text()) + '.tiff')
            item.setToolTip(path)
            self.parent().writeToPrj(path)
            self.parent().ui.menuNarz_dzia.setEnabled(True)

    def on_XL_editingFinished(self):
        try:
            float(self.ui.XL.text())
        except:
            QtGui.QMessageBox.warning(self,QString.fromUtf8('Błąd'),QString.fromUtf8('Niepoprawna wartość!'),'OK')
            self.ui.XL.setText('0')

    def on_YL_editingFinished(self):
        try:
            float(self.ui.YL.text())
        except:
            QtGui.QMessageBox.warning(self,QString.fromUtf8('Błąd'),QString.fromUtf8('Niepoprawna wartość!'),'OK')
            self.ui.YL.setText('0')

    def on_XP_editingFinished(self):
        try:
            float(self.ui.XP.text())
        except:
            QtGui.QMessageBox.warning(self,QString.fromUtf8('Błąd'),QString.fromUtf8('Niepoprawna wartość!'),'OK')
            self.ui.XP.setText('0')

    def on_YP_editingFinished(self):
        try:
            float(self.ui.YP.text())
        except:
            QtGui.QMessageBox.warning(self,QString.fromUtf8('Błąd'),QString.fromUtf8('Niepoprawna wartość!'),'OK')
            self.ui.YP.setText('0')

    def on_ImPix_editingFinished(self):
        try:
            pix = float(self.ui.YP.text())
            if pix>1:
                QtGui.QMessageBox.warning(self,QString.fromUtf8('Błąd'),QString.fromUtf8('Za duża wartość!'),'OK')
                self.ui.YP.setText('1')
            if pix<0.05:
                QtGui.QMessageBox.warning(self,QString.fromUtf8('Błąd'),QString.fromUtf8('Za mała wartość!'),'OK')
                self.ui.YP.setText('0.05')
        except:
            QtGui.QMessageBox.warning(self,QString.fromUtf8('Błąd'),QString.fromUtf8('Niepoprawna wartość!'),'OK')
            self.ui.YP.setText('0.1')

    def selectCRS(self, crs):
        if crs == '92':
            crs = 'EPSG%3A2180'
            epsg = 2180
        elif crs == '2000 s. V':
            crs = 'EPSG%3A2176'
            epsg = 2176
        elif crs == '2000 s. VI':
            crs = 'EPSG%3A2177'
            epsg = 2177
        elif crs == '2000 s. VII':
            crs = 'EPSG%3A2178'
            epsg = 2178
        elif crs == '2000 s. VIII':
            crs = 'EPSG%3A2179'
            epsg = 2179
        return crs, epsg


class ClassDefinitionMenu(QtGui.QMainWindow):
    vertices = []
    clickNumber = 0
    lx = 0
    ly = 0
    rx = 0
    ry = 0

    @QtCore.pyqtSlot()
    def __init__(self, parent=Menu):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_ClassDefinition()
        self.ui.setupUi(self)
        self.fillClassList()
        self.ui.DrawClass.setEnabled(False)
        QtCore.QObject.connect(self.ui.ClassList,QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), self.itemActivated)

    @QtCore.pyqtSlot()
    def on_AddClass_released(self):
        NewClassMenu(self).show()

    def fillClassList(self):
        #self.parent().classPath = projectPath + '\\' + 'klasy.txt'
        flen = len(open(self.parent().classPath).readlines())
        if flen>2:
            classData = np.loadtxt(self.parent().classPath, delimiter=' ', dtype=str, skiprows=1)
            classNames = list(set(classData[:,0]))
            for name in classNames:
                item = QtGui.QListWidgetItem(self.ui.ClassList)
                item.setText(name)
        elif flen==2:
            classData = np.loadtxt(self.parent().classPath, delimiter=' ', dtype=str, skiprows=1)
            className = classData[0]
            item = QtGui.QListWidgetItem(self.ui.ClassList)
            item.setText(className)

    def on_DrawClass_released(self):
        if self.parent().fig:
            self.clickNumber = 0
            self.vertices = []
            self.parent().fig.canvas.mpl_connect('button_press_event', self.onclick)
        else:
            QtGui.QMessageBox.warning(self,QString.fromUtf8('Błąd'),QString.fromUtf8('Żaden obraz nie jest otwarty!'),'Ok')

    def itemActivated(self):
        self.ui.DrawClass.setEnabled(True)

    def onclick(self, event):
        if (event.button == 1):
            self.vertices.append((int(floor(event.xdata)),int(floor(event.ydata))))
            self.clickNumber += 1
            print self.vertices
        if (event.button == 2):
            self.vertices.append(self.vertices[0])
            codes = []
            codes.append(Path.MOVETO)
            for i in range(len(self.vertices)-2):
                codes.append((Path.LINETO))
            codes.append(Path.CLOSEPOLY)
            path = Path(self.vertices, codes)
            gca = mpp.gca()
            gca.add_patch(patches.PathPatch(path, facecolor='orange', lw=2))
            mpp.show()
            maxx = max(self.vertices)[0]
            minx = min(self.vertices)[0]
            maxy = max(self.vertices, key=itemgetter(1))[1]
            miny = min(self.vertices, key =itemgetter(1))[1]
            img = Image.new('L', (maxx, maxy), 0)
            ImageDraw.Draw(img).polygon(self.vertices, outline=1, fill=1)
            mask = np.array(img)
            mask = mask[miny:, minx:]
            print np.sum(mask), self.vertices, codes, maxx-minx, maxy-miny
            self.vertices = []
            criteria = ('h','s','v','veg','ent')
            className = str(self.ui.ClassList.currentItem().text())
            Classify.saveClass(self.parent().image, self.parent().classPath,
                               className, criteria, miny, minx, maxy, maxx, mask)

    def saveClass(self, lx, ly, rx, ry):
        criteria = ('h','s','v','veg','ent')
        className = str(self.ui.ClassList.currentItem().text())
        Classify.saveClass(self.parent().image, self.parent().classPath,
                           className, criteria, self.lx, self.ly, self.rx, self.ry)

    # def drawRectangle(self, rx, ry, lx, ly, color, fig):
    #     rx, lx = self.switchCorners(rx, lx)
    #     ry, ly = self.switchCorners(ry,ly)
    #     dx = rx - lx
    #     dy = ry - ly
    #     xy = (lx, ly)
    #     gca = mpp.gca()
    #     gca.add_patch(Rectangle(xy, dx, dy, fill=True, color=color, figure=fig))
    #     mpp.show()

    # def switchCorners(self, r, l):
    #     if r>l:
    #         return l, r
    #     else:
    #         return r, l


class NewClassMenu(QtGui.QMainWindow):

    def __init__(self, parent=ClassDefinitionMenu):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_NewClass()
        self.ui.setupUi(self)

    def on_OKButton_released(self):
        if self.ui.ClassName != '':
            #for item in range(self.parent().ui.ClassList.count()):
            #    if str(item.text()) == str(self.ui.ClassName.text()):
            #        QtGui.QMessageBox.warning(self,'','Klasa o podanej nazwie już istnieje!','Ok')
            #        return 0
            item = QtGui.QListWidgetItem(self.parent().ui.ClassList)
            item.setText(str(self.ui.ClassName.text()))
            self.close()


class ClassifyMenu(QtGui.QMainWindow):

    def __init__(self, parent=Menu):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Classify()
        self.ui.setupUi(self)
        self.fillPhotoList()

    def fillPhotoList(self):
        for i in range(self.parent().ui.PhotoList.count()):
            photo = str(self.parent().ui.PhotoList.item(i).text())
            path = str(self.parent().ui.PhotoList.item(i).toolTip())
            item = QtGui.QListWidgetItem(self.ui.AllPhotos)
            item.setText(photo)
            item.setToolTip(path)

    @QtCore.pyqtSlot()
    def on_SelectPhotos_released(self):
        self.moveItems(self.ui.AllPhotos, self.ui.SelectedPhotos)

    @QtCore.pyqtSlot()
    def on_DeletePhotos_released(self):
        self.moveItems(self.ui.SelectedPhotos, self.ui.AllPhotos)

    @QtCore.pyqtSlot()
    def on_ClassifyButton_released(self):
        minArea = 0
        for i in range(self.ui.SelectedPhotos.count()):
            item = self.ui.SelectedPhotos.item(i)
            image = readImage(str(item.toolTip()))
            imName = str(self.parent().ui.PhotoList.item(i).text())
            outPath = self.parent().outputDir + '\\' + imName[:imName.rfind('.')] + '.tiff'
            if self.ui.minAreaSize.isEnabled():
                minArea = int(self.ui.minAreaSize.text())
            Classify.imageClassify(self,image,self.parent().classPath,outPath,minArea)
            item = QtGui.QListWidgetItem(self.parent().ui.ClassifiedList)
            item.setText(imName)
            item.setToolTip(outPath)

    def on_checkSieve_stateChanged(self):
        if self.ui.minAreaSize.isEnabled():
            self.ui.minAreaSize.setEnabled(False)
        else:
            self.ui.minAreaSize.setEnabled(True)

    def moveItems(self, list1, list2):
        photos = list1.selectedItems()
        for photo in photos:
            item  = QtGui.QListWidgetItem(list2)
            name = str(photo.text())
            item.setText(name)
            item.setToolTip(str(photo.toolTip()))
            list1.takeItem(list1.row(photo))
        if self.ui.SelectedPhotos.count():
            self.ui.ClassifyButton.setEnabled(True)
        else:
            self.ui.ClassifyButton.setEnabled(False)


class ConvertToSHPMenu(QtGui.QMainWindow):

    def __init__(self, parent=Menu):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_ConvertToSHP()
        self.ui.setupUi(self)
        self.fillPhotoList()

    def fillPhotoList(self):
        for i in range(self.parent().ui.ClassifiedList.count()):
            photo = str(self.parent().ui.ClassifiedList.item(i).text())
            path = str(self.parent().ui.ClassifiedList.item(i).toolTip())
            item = QtGui.QListWidgetItem(self.ui.AllPhotos)
            item.setText(photo)
            item.setToolTip(path)

    @QtCore.pyqtSlot()
    def on_SelectPhotos_released(self):
        self.moveItems(self.ui.AllPhotos, self.ui.SelectedPhotos)

    @QtCore.pyqtSlot()
    def on_DeletePhotos_released(self):
        self.moveItems(self.ui.SelectedPhotos, self.ui.AllPhotos)

    @QtCore.pyqtSlot()
    def on_ConversionButton_released(self):
        for i in range(self.ui.SelectedPhotos.count()):
            item = self.ui.SelectedPhotos.item(i)
            imPath = str(self.ui.SelectedPhotos.item(i).toolTip())
            imName = str(self.ui.SelectedPhotos.item(i).text())
            outPath = self.parent().outputDir + '\\' + imName[:imName.rfind('.')] + '.shp'
            print imPath, outPath
            Classify.img2shp(imPath,outPath)

    def moveItems(self, list1, list2):
        photos = list1.selectedItems()
        for photo in photos:
            item  = QtGui.QListWidgetItem(list2)
            name = str(photo.text())
            item.setText(name)
            item.setToolTip(str(photo.toolTip()))
            list1.takeItem(list1.row(photo))
        if self.ui.SelectedPhotos.count():
            self.ui.ConversionButton.setEnabled(True)
        else:
            self.ui.ConversionButton.setEnabled(False)


def readImage(path):
    ds = gdal.Open(path)
    image = np.array(ds.GetRasterBand(1).ReadAsArray())
    r, c = np.shape(image)
    image = np.zeros((r,c,3))
    for i in range(ds.RasterCount):
        image[:,:,i] = np.array(ds.GetRasterBand(i+1).ReadAsArray())
    if ds.RasterCount==3:
        image = image.astype(np.uint8)
    return image


if __name__ == "__main__":
    app = QtGui.QApplication(argv)
    myapp = Menu()
    myapp.show()
    exit(app.exec_())