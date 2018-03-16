#!/usr/bin/env python
## -*- coding: utf-8 -*-

import cv2, gdal, ogr
from urllib2 import urlopen
import numpy as np
from skimage.filters.rank import entropy
from skimage.morphology import disk
from PyQt4.QtGui import QMessageBox
from PyQt4.QtCore import QString
import matplotlib.pyplot as mpp
from scipy.signal import fftconvolve

def imageClassify(gui, image, classPath, savePath, minArea):
    r,c,d = np.shape(image)

    #odczyt z pliku; criteria: r g b h s v veg ent
    num_lines = sum(1 for line in open(classPath))
    if num_lines<3:
        QMessageBox.warning(gui,QString.fromUtf8('Błąd'),QString.fromUtf8('Za mało danych w pliku klas!'),'Ok')
        return 0
    cls = np.loadtxt(classPath, delimiter=' ', dtype=str, skiprows=1)
    criteria = open(classPath).readline().rstrip()
    criteria = criteria.split()
    param = cls[:,1:len(criteria)+1].astype(float)
    imMaxMin = np.zeros((2,len(criteria)))
    for i in range(len(criteria)):
        imMaxMin[0,i] = np.amin(cls[:,len(criteria)+1+i*2].astype(float))
        imMaxMin[1,i] = np.amax(cls[:,len(criteria)+2+i*2].astype(float))
        param[:,i] = standarize(param[:,i],imMaxMin[0,i],imMaxMin[1,i])
    names = list(set(cls[:,0]))
    n, x = np.shape(cls)
    m = len(names)
    nrcls = np.zeros(n)
    for i in range(n):
        for j in range(m):
            if cls[i,0]==names[j]:
                nrcls[i] = j
                break

    #dzielenie zdj i klasyfikacja
    clsImage = np.zeros((r,c))
    for i in range(0,r,1000):
        for j in range(0,c,1000):
            nr = i+1010
            nc = j+1010
            if nr>r:
                nr = r
            if nc>c:
                nc = c
            imCrop = image[i:nr,j:nc,:]
            clsImage[i:nr,j:nc] = minDistClassify(imCrop, nrcls, param, criteria, imMaxMin)
    for i in range(0,m):
        clsImage2 = np.zeros((r,c))
        clsImage2[clsImage==i] = 1
        print np.sum(clsImage2), names[i]
    saveRaster(clsImage,savePath,names, minArea)

def minDistClassify(image, nrcls, param, criteria, imMaxMin):
    r,c,d = np.shape(image)
    n = len(nrcls)
    allClass = np.zeros((r,c,n))
    criteriaImage  = np.zeros((r,c,len(criteria)))
    for i in range(len(criteria)):
        criteriaImage[:,:,i] = standarize(imageCriteria(image,criteria[i],0,0,r,c),imMaxMin[0,i],imMaxMin[1,i])

    for i in range(n):
        sum = 0
        for j in range(len(criteria)):
            sum = sum + abs(criteriaImage[:,:,j]-param[i,j])
        allClass[:,:,i] = sum

    imClassMin = np.amin(allClass,(2))
    imClass = np.zeros((r,c))
    for i in range(n):
        imClass[imClassMin==allClass[:,:,i]] = nrcls[i]
    return imClass

def saveClass(image, classPath, className, criteria, lx, ly, rx, ry, mask):
    r,c = np.shape(mask)
    print r,c
    param = np.zeros(3*len(criteria))
    imCrop = np.zeros((rx-lx,ry-ly))
    r,c = np.shape(imCrop)
    print r,c
    for i in range(len(criteria)):
        imCrop[:,:] = imageCriteria(image,criteria[i],lx,ly,rx,ry)*mask
        param[i] = np.sum(imCrop)/np.sum(mask)
        param[len(criteria)+(i*2)+1] = np.amax(imCrop)
        imCrop[imCrop==0] = 300;
        param[len(criteria)+i*2] = np.amin(imCrop)
    classFile = open(classPath, 'a')
    classFile.write('%s' %className)
    for i in range(len(param)):
        classFile.write(' %f' %param[i])
    classFile.write('\n')
    classFile.closed

def imageCriteria(image, criteria, lx, ly, rx, ry):
    if criteria == "r":
        return image[lx:rx, ly:ry,2].astype(float)
    elif criteria == "g":
        return image[lx:rx, ly:ry,1].astype(float)
    elif criteria == "b":
        return image[lx:rx, ly:ry,0].astype(float)
    elif criteria == "veg":
        b = image[lx:rx, ly:ry,0].astype(float)
        g = image[lx:rx, ly:ry,1].astype(float)
        return (g-b)/(g+b+0.0001)+1
    elif criteria == "ent":
        return entropy(cv2.cvtColor(image[lx:rx, ly:ry], cv2.COLOR_RGB2GRAY),disk(10))
    imHSV = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    if criteria == "h":
        return imHSV[lx:rx, ly:ry,0].astype(float)
    else:
        if criteria == "s":
            return imHSV[lx:rx, ly:ry,1].astype(float)
        else:
            if criteria == "v":
                return imHSV[lx:rx, ly:ry,2].astype(float)

def switchCorners(r, l):
    if r>l:
        return l, r
    else:
        return r, l

def standarize(image, immin, immax):
    image = (image-immin)/(immax-immin)
    return image

def img2shp(inputPath, outputPath):
    image = gdal.Open(inputPath)
    imageBand = image.GetRasterBand(1)
    imageRAT = image.GetRasterBand(1).GetDefaultRAT()

    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataSet = driver.CreateDataSource(outputPath)
    layer = dataSet.CreateLayer(outputPath, srs = None)
    layer.CreateField(ogr.FieldDefn('value', ogr.OFTInteger))
    layer.CreateField(ogr.FieldDefn('landuse', ogr.OFTString))
    gdal.Polygonize(imageBand, None, layer, 0, [], callback=None)

    feature = layer.GetNextFeature()
    i=0
    while feature:
        i=i+1
        value = feature.GetField('value')
        landuse = imageRAT.GetValueAsString(value,1)
        feature.SetField('landuse',landuse)
        layer.SetFeature(feature)
        feature = layer.GetNextFeature()

def saveRaster(image, path, attributes, minArea):
    image = image.astype(int)
    r,c = np.shape(image)
    rasterRAT = gdal.RasterAttributeTable()
    rasterRAT.SetRowCount(len(attributes))
    rasterRAT.CreateColumn('value', gdal.GFT_Integer, gdal.GFU_Generic)
    rasterRAT.CreateColumn('class_name', gdal.GFT_String, gdal.GFU_Name)
    for i in range(len(attributes)):
        rasterRAT.SetValueAsInt(i,0,i)
        rasterRAT.SetValueAsString(i,1,attributes[i])
    output_raster = gdal.GetDriverByName('GTiff').Create(path,c, r, 1 ,gdal.GDT_Int32)
    output_raster.GetRasterBand(1).WriteArray(image)
    if (minArea<5 and minArea>0):
        gdal.SieveFilter(output_raster.GetRasterBand(1),None,output_raster.GetRasterBand(1),minArea,4,[],None,None)
    if minArea>=5:
        gdal.SieveFilter(output_raster.GetRasterBand(1),None,output_raster.GetRasterBand(1),5,4,[],None,None)
    if minArea>=15:
        gdal.SieveFilter(output_raster.GetRasterBand(1),None,output_raster.GetRasterBand(1),15,4,[],None,None)
        gdal.SieveFilter(output_raster.GetRasterBand(1),None,output_raster.GetRasterBand(1),minArea,4,[],None,None)
    output_raster.GetRasterBand(1).SetDefaultRAT(rasterRAT)

def importFromGeoportal(gui, savePath, minx, miny, maxx, maxy, pix, crs, epsg):
    if maxx<minx:
        QMessageBox.warning(gui,'Błąd','X lewy mniejszy od X prawy!','Ok')
        return 0
    if maxy<miny:
        QMessageBox.warning(gui,'Błąd','Y lewy mniejszy od Y prawy!','Ok')
        return 0
    width = round((maxx-minx)/pix)
    height = round((maxy-miny)/pix)
    if width<100 or height<100:
        QMessageBox.warning(gui,'Błąd','Za mały obraz!','Ok')
        return 0
    try:
        url = 'http://mapy.geoportal.gov.pl/wss/service/img/guest/ORTO_TIME/MapServer/WMSServer?REQUEST=GetMap&TRANSPARENT=TRUE&' \
              'FORMAT=image%%2Ftiff&VERSION=1.3.0&LAYERS=RASTER&STYLES=&EXCEPTIONS=xml&BBOX=%s,%s,%s,%s&CRS=%s&WIDTH=%s&HEIGHT=%s'\
              %(minx, miny, maxx, maxy, crs, width, height)
        image = urlopen(url).read()
    except:
        QMessageBox.warning(gui,QString.fromUtf8('Błąd'),QString.fromUtf8('Nie można pobrać obrazu!'),'Ok')
        return 0
    open(savePath, 'wb').write(image)
    QMessageBox.warning(gui,'Sukces','Zaimportowano!','Ok')
    return 1


