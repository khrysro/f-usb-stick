#!/usr/bin/python3
import sys
from share.formatstick.formatstick import *
from mountutils import *
from raw_format import *
from raw_write import *
#from udisks import *

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QDialog, QApplication
from PyQt5.QtCore import QFile, Qt, QVariant
from PyQt5.Qt import QApplication, QStandardItemModel, QStandardItem, QTreeView

class Miformulario(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        model = QStandardItemModel()

        items = [("ABC"),
                 ("DEF"),
                 ("GHI")]

        #for text, checked in items:
        for text in items:
            text_item = QStandardItem(text)
            #checked_item = QStandardItem()
            #checked_item.setData(QVariant(checked), Qt.CheckStateRole)
            model.appendRow(text_item)#([text_item, checked_item])

        view = QTreeView()
        view.header().hide()
        view.setRootIsDecorated(False)

        combo = self.ui.comboBox_device
        combo.setView(view)
        combo.setModel(model)
        combo.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Miformulario()
    myapp.show()
    sys.exit(app.exec())