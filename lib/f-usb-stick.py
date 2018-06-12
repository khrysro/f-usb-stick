#!/usr/bin/python3
import sys
from share.formatstick.formatstick import *
from mountutils import *
from raw_format import *
from raw_write import *

from lib.update_devices import *
import dbus, sys
from dbus.mainloop.pyqt5 import DBusQtMainLoop

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QDialog, QApplication,QMainWindow
from PyQt5.QtCore import QFile, Qt, QVariant, QObject
from PyQt5.Qt import QApplication, QStandardItemModel, QStandardItem, QTreeView

class Miformulario(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        DBusQtMainLoop(set_as_default=True)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBox_device.mousePressEvent(self.update_usb_devices)

    def update_usb_devices(self):
        model = QStandardItemModel()
        bus = dbus.SystemBus()
        self.iface = 'org.freedesktop.DBus.ObjectManager'
        #bus.add_signal_receiver(self.callback_function, signal, iface)
        proxy = bus.get_object("org.freedesktop.UDisks2", "/org/freedesktop/UDisks2")
        self.iface = dbus.Interface(proxy, "org.freedesktop.UDisks2")


        self.iface.connect_to_signal('DeviceAdded', self.device_added_callback)
        self.iface.connect_to_signal('DeviceRemoved', self.device_removed_callback)
        self.iface.connect_to_signal('InterfacesAdded', self.device_changed_callback)

        dev1 = get_usb()
        items = get_usb()

        #for text, checked in items:
        for text in sorted(items):

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

    def device_changed_callback(*args):
        # print('Received something .. ', args)
        dev1 = get_usb()

        # print('Received something .. ', dev1 )
        print(usb_details(dev1[0]))

    def device_added_callback(device):
        #self.logger(_('Device %s was added' % (device))
        print("device Added")
        #self.get_devices()

    def device_removed_callback(device):
        #self.logger(_('Device %s has been removed' % (device))
        print("device removed")
        #self.get_devices()






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Miformulario()
    myapp.show()
    sys.exit(app.exec())