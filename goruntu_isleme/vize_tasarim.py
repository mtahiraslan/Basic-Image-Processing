# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vize_tasarim.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1094, 860)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1091, 861))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btn_resim_sec = QtWidgets.QPushButton(self.tab)
        self.btn_resim_sec.setGeometry(QtCore.QRect(310, 450, 141, 28))
        self.btn_resim_sec.setObjectName("btn_resim_sec")
        self.lbl_resim_sec = QtWidgets.QLabel(self.tab)
        self.lbl_resim_sec.setGeometry(QtCore.QRect(10, 20, 961, 361))
        self.lbl_resim_sec.setText("")
        self.lbl_resim_sec.setObjectName("lbl_resim_sec")
        self.btn_gurultu_olustur = QtWidgets.QPushButton(self.tab)
        self.btn_gurultu_olustur.setGeometry(QtCore.QRect(740, 450, 161, 28))
        self.btn_gurultu_olustur.setObjectName("btn_gurultu_olustur")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btn_daire_ciz = QtWidgets.QPushButton(self.tab_2)
        self.btn_daire_ciz.setGeometry(QtCore.QRect(130, 670, 111, 28))
        self.btn_daire_ciz.setObjectName("btn_daire_ciz")
        self.lbl_daire_goster = QtWidgets.QLabel(self.tab_2)
        self.lbl_daire_goster.setGeometry(QtCore.QRect(30, 50, 991, 531))
        self.lbl_daire_goster.setText("")
        self.lbl_daire_goster.setObjectName("lbl_daire_goster")
        self.txt_merkez = QtWidgets.QLineEdit(self.tab_2)
        self.txt_merkez.setGeometry(QtCore.QRect(370, 670, 311, 31))
        self.txt_merkez.setObjectName("txt_merkez")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_resim_sec.setText(_translate("Dialog", "Resim Seç"))
        self.btn_gurultu_olustur.setText(_translate("Dialog", "Gürültü Oluştur"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Gürültü Oluşturma"))
        self.btn_daire_ciz.setText(_translate("Dialog", "Daire Çiz"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Çember Çizme"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

