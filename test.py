#!/usr/bin/python3

import subprocess
from subprocess import Popen,PIPE,call,STDOUT
import os
import signal
import re
import gettext
import locale
import sys
import getopt
import time

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class DemoImpl(QDialog):
    def __init__(self, *args):
        super(DemoImpl, self).__init__(*args)

        loadUi('/home/khrys/desarrollo/Formatstick/share/formatstick/formatstick.ui', self)

    def 

app = QApplication(sys.argv)
widget = DemoImpl()
widget.show()
sys.exit(app.exec_())