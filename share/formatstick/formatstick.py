# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formatstick.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(625, 168)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_Volume = QtWidgets.QLabel(Dialog)
        self.label_Volume.setObjectName("label_Volume")
        self.gridLayout.addWidget(self.label_Volume, 1, 0, 1, 1)
        self.comboBox_type = QtWidgets.QComboBox(Dialog)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.gridLayout.addWidget(self.comboBox_type, 0, 3, 1, 1)
        self.label_format = QtWidgets.QLabel(Dialog)
        self.label_format.setObjectName("label_format")
        self.gridLayout.addWidget(self.label_format, 0, 0, 1, 1)
        self.comboBox_device = QtWidgets.QComboBox(Dialog)
        self.comboBox_device.setObjectName("comboBox_device")
        self.gridLayout.addWidget(self.comboBox_device, 0, 1, 1, 1)
        self.label_as = QtWidgets.QLabel(Dialog)
        self.label_as.setObjectName("label_as")
        self.gridLayout.addWidget(self.label_as, 0, 2, 1, 1)
        self.textEdit_name = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_name.sizePolicy().hasHeightForWidth())
        self.textEdit_name.setSizePolicy(sizePolicy)
        self.textEdit_name.setMaximumSize(QtCore.QSize(300, 30))
        self.textEdit_name.setObjectName("textEdit_name")
        self.gridLayout.addWidget(self.textEdit_name, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_Volume.setText(_translate("Dialog", "Volume Label"))
        self.comboBox_type.setItemText(0, _translate("Dialog", "FAT32"))
        self.comboBox_type.setItemText(1, _translate("Dialog", "NTFS"))
        self.comboBox_type.setItemText(2, _translate("Dialog", "FAT16"))
        self.label_format.setText(_translate("Dialog", "Format"))
        self.label_as.setText(_translate("Dialog", "as"))
        self.textEdit_name.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">USB Stick</p></body></html>"))

