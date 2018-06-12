import dbus, sys
import threading, time


'''
if mainloop == 'glib':
        from dbus.mainloop.glib import DBusGMainLoop
        mainloop = DBusGMainLoop()
elif mainloop == 'qt':
        from dbus.mainloop.qt import DBusQtMainLoop
'''

def start_listening():
    import dbus
    from dbus.mainloop.pyqt5 import DBusQtMainLoop
    DBusQtMainLoop(set_as_default=True)

    bus = dbus.SystemBus()

    # Function which will run when signal is received
    def callback_function(*args):
        print('Received something .. ', args)

    # Which signal to have an eye for
    iface = 'org.freedesktop.DBus.ObjectManager'
    signal = 'InterfacesAdded'
    bus.add_signal_receiver(callback_function, signal, iface)

    # Let's start the loop
    from  PyQt5.QtCore import QObject
        QObject.thread()
      # Without this, we will be stuck in the glib loop
    loop = QObject.MainLoop()
    loop.run()'''
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    app.exec_()


# Our thread will run start_listening
thread = threading.Thread(target=start_listening)
thread.daemon = True  # This makes sure that CTRL+C works
thread.start()

# And our program will continue in this pointless loop
while True:
    time.sleep(10)
    print("tralala")

'''
from PyQt5.QtWidgets import QApplication

#app.exec_()
app = QApplication(sys.argv)
testWindow = SampleMainWindow()
testWindow.show()
# run custom event loop instead of app.exec_()
while APP_RUNNING:
    app.processEvents()
    # sleep to prevent that my "great" event loop eats 100% cpu
    time.sleep(0.01)