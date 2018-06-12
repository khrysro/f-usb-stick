import dbus, sys
from dbus.mainloop.pyqt5 import DBusQtMainLoop
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QObject
from lib.update_devices import *

class MyApplication(QObject):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        DBusQtMainLoop(set_as_default=True)
        bus = dbus.SystemBus()
        # Which signal to have an eye for
        iface = 'org.freedesktop.DBus.ObjectManager'
        signal = 'InterfacesAdded'
        bus.add_signal_receiver(self.callback_function, signal, iface)

    # Function which will run when signal is received
    def callback_function(*args):
        #print('Received something .. ', args)
        dev1=get_usb()

        print('Received something .. ', dev1[-1] )
        print(len(dev1))
        #print(usb_details(dev1[-1]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApplication()
    #myapp.show()
    sys.exit(app.exec_())
 
