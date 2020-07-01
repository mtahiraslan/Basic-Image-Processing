# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 17:07:19 2018

@author: PC
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QFileDialog
from odev_tasarim import Ui_Dialog
from shutil import copyfile
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
from scipy.ndimage import rotate
import cv2
import sys
import scipy.misc
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import random
import math
import io
import numpy as np


class MainWindow(QWidget,Ui_Dialog):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        #self.btn_kapat.clicked.connect(self.kapat)
        
        self.cm_box.clear()
        self.cm_box.addItem('OR')
        self.cm_box.addItem('AND')
        self.cm_box.addItem('NOT')
        self.cm_box.addItem('XOR')
        
        self.cm_box_2.clear()
        self.cm_box_2.addItem('Griye Cevirme')
        self.cm_box_2.addItem('Binary Cevirme')
        self.cm_box_2.addItem('Sifirlama')
        self.cm_box_2.addItem('Otsu')
        self.cm_box_2.addItem('Histogram Esitleme')
        self.cm_box_2.addItem('Clahe')
             

        self.btn_sec.clicked.connect(self.resim_sec)
        self.btn_boyutlandir.clicked.connect(self.boyutlandir)
        self.btn_ekle.clicked.connect(self.resim_ekle_1)
        self.btn_sola_dondur.clicked.connect(self.sola_dondur)
        self.btn_saga_dondur.clicked.connect(self.saga_dondur)
        self.btn_ekle_resim.clicked.connect(self.resim_ekle_2)
        self.btn_ekle_resim_2.clicked.connect(self.resim_ekle_3)
        self.btn_uygula.clicked.connect(self.mantiksal_islemler)
        self.btn_gozat.clicked.connect(self.resim_ekle_4)
        self.btn_filtre_uygula.clicked.connect(self.filtreleme)
        self.btn_resim_sec.clicked.connect(self.resim_ekle_5)
        self.btn_lableling.clicked.connect(self.template_matching)
        self.btn_gozat_resim.clicked.connect(self.resim_ekle_6)
        self.btn_resim_ekle.clicked.connect(self.resim_ekle_7)
        self.btn_gurultu.clicked.connect(self.gurultu_ekle)
        self.btn_daire_ciz.clicked.connect(self.daire_ciz)
        self.btn_labelling_sec.clicked.connect(self.resim_ekle_8)
        self.btn_labelling_uygula.clicked.connect(self.labelling)
        self.buton_resim_sec.clicked.connect(self.resim_ekle_9)
        self.btn_piksel_bul.clicked.connect(self.piksel_bul)
        
        
    def resim_sec(self):
        dosya_adi = QFileDialog.getOpenFileName()
        resim_yolu = dosya_adi[0]
        yol = str(resim_yolu)
        pixmap = QPixmap(resim_yolu)
        self.lbl_resim_1.setScaledContents(True)
        self.lbl_resim_1.setPixmap(pixmap)
        self.show()
        copyfile(yol, './resize.jpg')
        
        
    def boyutlandir(self):
        yukseklik_deger = int(self.txt_yukseklik.text())
        genislik_deger = int(self.txt_genislik.text())
        dosya_adi = './resize.jpg'
        orijinal_resim = cv2.imread(dosya_adi)
        yeni_resim = cv2.resize(orijinal_resim, (genislik_deger, yukseklik_deger))
        cv2.imwrite('./resizeResult.jpg', yeni_resim)
        pixmap = QPixmap('./resizeResult.jpg')
        self.lbl_resim_2.setScaledContents(False)
        self.lbl_resim_2.setPixmap(pixmap)
        self.show()
        
    def resim_ekle_1(self):
        dosya_adi = QFileDialog.getOpenFileName()
        self.resim_yolu = dosya_adi[0]
        yol = str(self.resim_yolu)
        pixmap = QPixmap(self.resim_yolu)
        self.lbl_resim_3.setScaledContents(True)
        self.lbl_resim_3.setPixmap(pixmap)
        self.show()
        copyfile(yol, './dondurulecek_resim.jpg')
        
    def sola_dondur(self):
        resim = cv2.imread(self.resim_yolu)
        resim2 = rotate(resim, 180)
        cv2.imwrite('./sola_donuk.jpg', resim2)
        string = './sola_donuk.jpg'
        pixmap = QPixmap(string)
        self.lbl_resim_3.setScaledContents(True)
        self.lbl_resim_3.setPixmap(pixmap)
        self.show()
         
    def saga_dondur(self):
        resim = cv2.imread(self.resim_yolu)
        resim2 = rotate(resim, 90)
        cv2.imwrite('./saga_donuk.jpg', resim2)
        string = './saga_donuk.jpg'
        pixmap = QPixmap(string)
        self.lbl_resim_3.setScaledContents(True)
        self.lbl_resim_3.setPixmap(pixmap)
        self.show()
        
    def resim_ekle_2(self):
        dosya_adi = QFileDialog.getOpenFileName()
        resim_yolu = dosya_adi[0]
        yol = str(resim_yolu)
        pixmap = QPixmap(resim_yolu)
        self.lbl_resim_4.setScaledContents(True)
        self.lbl_resim_4.setPixmap(pixmap)
        self.show()
        copyfile(yol, './resim1.jpg')

            
    def resim_ekle_3(self):
        dosya_adi = QFileDialog.getOpenFileName()
        resim_yolu = dosya_adi[0]
        yol = str(resim_yolu)
        pixmap = QPixmap(resim_yolu)
        self.lbl_resim_5.setScaledContents(True)
        self.lbl_resim_5.setPixmap(pixmap)
        self.show()
        copyfile(yol, './resim2.jpg')
        
    
    def mantiksal_islemler(self):
        resim1 = cv2.imread('./resim1.jpg', 0)
        resim2 = cv2.imread('./resim2.jpg', 0)
        
        resized1 = cv2.resize(resim1, (600, 600))
        resized2 = cv2.resize(resim2, (600, 600))
         
        islem = str(self.cm_box.currentText())
        
        if islem == 'OR':
            islem_or = cv2.bitwise_or(resized1, resized2)
            cv2.imwrite('./mantiksal_or.jpg', islem_or)
            pixmap = QPixmap('./mantiksal_or.jpg')
            self.lbl_resim_6.setScaledContents(True)
            self.lbl_resim_6.setPixmap(pixmap)
            self.show()
        elif islem == 'AND':
            islem_and = cv2.bitwise_and(resized1, resized2)
            cv2.imwrite('./mantiksal_and.jpg', islem_and)
            pixmap = QPixmap('./mantiksal_and.jpg')
            self.lbl_resim_6.setScaledContents(True)
            self.lbl_resim_6.setPixmap(pixmap)
            self.show()
        elif islem == 'NOT':
            islem_not = cv2.bitwise_not(resized1, resized2)
            cv2.imwrite('./mantiksal_not.jpg', islem_not)
            pixmap = QPixmap('./mantiksal_not.jpg')
            self.lbl_resim_6.setScaledContents(True)
            self.lbl_resim_6.setPixmap(pixmap)
            self.show()
        elif islem == 'XOR':
            islem_xor = cv2.bitwise_xor(resized1, resized2)
            cv2.imwrite('./mantiksal_xor.jpg', islem_xor)
            pixmap = QPixmap('./mantiksal_xor.jpg')
            self.lbl_resim_6.setScaledContents(True)
            self.lbl_resim_6.setPixmap(pixmap)
            self.show()
            
    def resim_ekle_4(self):
        dosya_adi = QFileDialog.getOpenFileName()
        resim_yolu = dosya_adi[0]
        yol = str(resim_yolu)
        pixmap = QPixmap(resim_yolu)
        self.lbl_resim_7.setScaledContents(True)
        self.lbl_resim_7.setPixmap(pixmap)
        self.show()
        copyfile(yol, './filtreleme.jpg')
        
    def filtreleme(self):

        filtre_islem = str(self.cm_box_2.currentText())
        
        if filtre_islem=='Griye Cevirme':
            img = cv2.imread('./filtreleme.jpg', cv2.IMREAD_GRAYSCALE)
            cv2.imwrite('./gray_resim.jpg', img)
            pixmap = QPixmap('./gray_resim.jpg')
            self.lbl_resim_8.setScaledContents(True)
            self.lbl_resim_8.setPixmap(pixmap)
            self.show()
            
        elif filtre_islem=='Binary Cevirme':
            img = cv2.imread('./filtreleme.jpg', 0)
            ret, resim = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
            cv2.imwrite('./binary_resim.jpg', resim)
            pixmap = QPixmap('./binary_resim.jpg')
            self.lbl_resim_8.setScaledContents(True)
            self.lbl_resim_8.setPixmap(pixmap)
            self.show()
            
        elif filtre_islem=='Sifirlama':
            img = cv2.imread('./filtreleme.jpg', 0)
            ret, resim = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
            cv2.imwrite('./zero_resim.jpg', resim)
            pixmap = QPixmap('./zero_resim.jpg')
            self.lbl_resim_8.setScaledContents(True)
            self.lbl_resim_8.setPixmap(pixmap)
            self.show()
            
        elif filtre_islem=='Otsu':
            img = cv2.imread('./filtreleme.jpg', 0)
            ret, resim = cv2.threshold(img, 127, 255, cv2.THRESH_OTSU)
            cv2.imwrite('./otsu_resim.jpg', resim)
            pixmap = QPixmap('./otsu_resim.jpg')
            self.lbl_resim_8.setScaledContents(True)
            self.lbl_resim_8.setPixmap(pixmap)
            self.show()
            
        elif filtre_islem=='Histogram Esitleme':
            img = cv2.imread('./filtreleme.jpg', 0)
            equ = cv2.equalizeHist(img)        
            cv2.imwrite('./histogram_resim.jpg',equ)
            pixmap = QPixmap('./histogram_resim.jpg')
            self.lbl_resim_8.setScaledContents(True)
            self.lbl_resim_8.setPixmap(pixmap)
            self.show()
            
        elif filtre_islem=='Clahe':
            img = cv2.imread('./filtreleme.jpg', 0)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
            cl1 = clahe.apply(img)
            cv2.imwrite('./clahe_resim.jpg',cl1)
            pixmap = QPixmap('./clahe_resim.jpg')
            self.lbl_resim_8.setScaledContents(True)
            self.lbl_resim_8.setPixmap(pixmap)
            self.show()
            
    def resim_ekle_5(self):
        dosya_adi = QFileDialog.getOpenFileName()
        resim_yolu = dosya_adi[0]
        yol = str(resim_yolu)
        pixmap = QPixmap(resim_yolu)
        self.lbl_resim_9.setScaledContents(True)
        self.lbl_resim_9.setPixmap(pixmap)
        self.show()
        copyfile(yol, './orjinal_resim.jpg')
        
    def resim_ekle_6(self):
        dosya_adi = QFileDialog.getOpenFileName()
        resim_yolu = dosya_adi[0]
        yol = str(resim_yolu)
        pixmap = QPixmap(resim_yolu)
        self.lbl_detected.setScaledContents(True)
        self.lbl_detected.setPixmap(pixmap)
        self.show()
        copyfile(yol, './aranacak_resim.jpg')
        
    def template_matching(self):
        resim1 = cv2.imread('./orjinal_resim.jpg', 0)
        resim2 = resim1.copy()
        template = cv2.imread('./aranacak_resim.jpg',0)
        w,h = template.shape[::-1]
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        for meth in methods:
            resim1 = resim2.copy()   
            method = eval(meth)
            res = cv2.matchTemplate(resim1,template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(resim1,top_left, bottom_right, 35, 2)
        
        self.lbl_resim_10.setScaledContents(True)
        scipy.misc.toimage(resim1, cmin=0.0, cmax=resim1.max()).save('./sonuc_resim.jpg')
        result = './sonuc_resim.jpg'
        pixmap = QPixmap(result)
        self.lbl_resim_10.setPixmap(pixmap)
        
    def resim_ekle_7(self):
        dosya_adi = QFileDialog.getOpenFileName()
        self.resim_yolu = dosya_adi[0]
        pixmap = QPixmap(self.resim_yolu)
        self.lbl_resim_11.setScaledContents(True)
        self.lbl_resim_11.setPixmap(pixmap)
        self.show()
        
    def gurultu_ekle(self):
        resim = cv2.imread(self.resim_yolu,0)
        height, width = resim.shape[:2]
        gurultu = np.zeros((height, width))
        cv2.randu(gurultu, 0, 256)
        noisy_gray = resim + np.array(0.6*gurultu, dtype=np.int)
        cv2.imwrite('./gurultulu_resim.jpg', noisy_gray)
        sonuc = './gurultulu_resim.jpg'
        pixmap = QPixmap(sonuc)
        self.lbl_resim_12.setScaledContents(True)
        self.lbl_resim_12.setPixmap(pixmap)
               
    def daire_ciz(self):
        x=random.randint(15,400)
        y=random.randint(15,400)
        r=random.randint(15,200)
        
        img = np.zeros((750,750,3), np.uint8)
        image = cv2.circle(img,(y,x), 27, (106,244,38), -1)
        cv2.imwrite('./cember.jpg', image)
        pixmap = QPixmap('./cember.jpg')
        self.lbl_cember.setScaledContents(True)
        self.lbl_cember.setPixmap(pixmap)
        self.show()
        
        x_koordinat=x
        y_koordinat=y
        self.txt_koordinat.setText('M('+str(x_koordinat)+','+str(y_koordinat)+')')
        
    def resim_ekle_8(self):
        dosya_adi = QFileDialog.getOpenFileName()
        self.resim_yolu = dosya_adi[0]
        pixmap = QPixmap(self.resim_yolu)
        self.label_resim_sec.setScaledContents(True)
        self.label_resim_sec.setPixmap(pixmap)
        self.show()
        
    def labelling(self):
        img = cv2.imread(self.resim_yolu, 0)
        img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]  # ensure binary
        ret, labels = cv2.connectedComponents(img)

        # Map component labels to hue val
        label_hue = np.uint8(179*labels/np.max(labels))
        blank_ch = 255*np.ones_like(label_hue)
        labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

        # cvt to BGR for display
        labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

        # set bg label to black
        labeled_img[label_hue==0] = 0

        
        cv2.imshow('labeled.png', labeled_img)
        
    def resim_ekle_9(self):
        dosya_adi = QFileDialog.getOpenFileName()
        self.resim_yolu = dosya_adi[0]
        pixmap = QPixmap(self.resim_yolu)
        self.label_resim_goster.setScaledContents(True)
        self.label_resim_goster.setPixmap(pixmap)
        self.show()
        
    def piksel_bul(self):
        img=cv2.imread(self.resim_yolu)
        for i,rows in enumerate(img):
            for j,pixels in enumerate(rows):
                self.label_piksel.setText("Row: {},Cell {}, RGB ({},{},{})".format(i,j,pixels[0],pixels[1],pixels[2]))
                print("Row: {},Cell {}, RGB ({},{},{})".format(i,j,pixels[0],pixels[1],pixels[2]))
    
        

        
        
        
        
        
    
        