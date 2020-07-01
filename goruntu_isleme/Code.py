# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 17:07:19 2018

@author: PC
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QFileDialog
from vize_tasarim import Ui_Dialog
from shutil import copyfile
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
from scipy.ndimage import rotate
import cv2
import sys
import scipy.misc
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import random
import math
import io
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
from skimage import io

class MainWindow(QWidget,Ui_Dialog):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.btn_resim_sec.clicked.connect(self.resim_sec)
        self.btn_gurultu_olustur.clicked.connect(self.gurultu_olustur)
        self.btn_daire_ciz.clicked.connect(self.daire_ciz)
        
        
                 
    def resim_sec(self):
        dosya_adi = QFileDialog.getOpenFileName()
        self.resim_yolu = dosya_adi[0]
        yol = str(self.resim_yolu)
        pixmap = QPixmap(self.resim_yolu)
        self.lbl_resim_sec.setScaledContents(True)
        self.lbl_resim_sec.setPixmap(pixmap)
        self.show()
        
    def gurultu_olustur(self):
        resim = misc.imread(self.resim_yolu,mode="L")
        gurultu=resim+3*resim.std()*np.random.random(resim.shape)
        alot=2*resim.max()*np.random.random(resim.shape)
        gurultu2=resim+alot
        
        f,axarr=plt.subplots(2,2)
        axarr[0,0].imshow(resim,cmap=plt.get_cmap('gray'))
        axarr[0,0].set_title('Gri Resim')
        
        axarr[0,1].imshow(gurultu,cmap=plt.get_cmap('gray'))
        axarr[0,1].set_title('Gurultulu Resim 1')
        
        axarr[1,0].imshow(gurultu2,cmap=plt.get_cmap('gray'))
        axarr[1,0].set_title('Gurultulu Resim 2')
        
        axarr[1,1].imshow(alot,cmap=plt.get_cmap('gray'))
        axarr[1,1].set_title('Cok Fazla Gurultulu Resim')
        
        plt.show()
        #cv2.imwrite('./gurultulu_resim.jpg',resim)
        #sonuc = './gurultulu_resim.jpg'
        #pixmap = QPixmap(sonuc)
        #self.lbl_resim_goster.setScaledContents(True)
        #self.lbl_resim_goster.setPixmap(pixmap)
    
    def daire_ciz(self):
        resim=cv2.imread('./image.jpg')
        w,h=resim.shape[:2]
        r=random.randint(1,75)
        x=random.randint(r,w-r)
        y=random.randint(r,h-r)
        
        for a in range(w):
                for b in range(h):
                    if math.sqrt((a-x)**2+(b-y)**2)<r:
                        resim[a,b]=(255,255,255)
                    else:
                        resim[a,b]=(50,125,255)
        cv2.imwrite('./daire.jpg',resim)
        pixmap=QPixmap('./daire.jpg')
        self.txt_merkez.setText('M('+str(x)+','+str(y)+')')
        self.lbl_daire_goster.setScaledContents(True)
        self.lbl_daire_goster.setPixmap(pixmap)
        self.show()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        