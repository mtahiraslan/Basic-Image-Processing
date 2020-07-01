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
        self.btn_resim_sec.setGeometry(QtCore.QRect(90, 290, 141, 28))
        self.btn_resim_sec.setObjectName("btn_resim_sec")
        self.lbl_resim_sec = QtWidgets.QLabel(self.tab)
        self.lbl_resim_sec.setGeometry(QtCore.QRect(10, 20, 301, 251))
        self.lbl_resim_sec.setText("")
        self.lbl_resim_sec.setObjectName("lbl_resim_sec")
        self.lbl_resim_goster = QtWidgets.QLabel(self.tab)
        self.lbl_resim_goster.setGeometry(QtCore.QRect(650, 20, 301, 251))
        self.lbl_resim_goster.setText("")
        self.lbl_resim_goster.setObjectName("lbl_resim_goster")
        self.btn_gurultu_olustur = QtWidgets.QPushButton(self.tab)
        self.btn_gurultu_olustur.setGeometry(QtCore.QRect(350, 90, 161, 28))
        self.btn_gurultu_olustur.setObjectName("btn_gurultu_olustur")
        self.lbl_resim_goster_2 = QtWidgets.QLabel(self.tab)
        self.lbl_resim_goster_2.setGeometry(QtCore.QRect(650, 290, 301, 251))
        self.lbl_resim_goster_2.setText("")
        self.lbl_resim_goster_2.setObjectName("lbl_resim_goster_2")
        self.lbl_resim_goster_3 = QtWidgets.QLabel(self.tab)
        self.lbl_resim_goster_3.setGeometry(QtCore.QRect(110, 450, 301, 251))
        self.lbl_resim_goster_3.setText("")
        self.lbl_resim_goster_3.setObjectName("lbl_resim_goster_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_resim_sec.setText(_translate("Dialog", "Resim Seç"))
        self.btn_gurultu_olustur.setText(_translate("Dialog", "Gürültü Oluştur"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Gürültü Oluşturma"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Çember Dizme"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

