import sys
from multiprocessing import Process, freeze_support

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

import silx
import pyFAI
import pyFAI.app
import pyFAI.app.calib2
import pyFAI.app.integrate
import silx.app
import silx.app.view
import silx.app.view.main

def app_silx_view():
    silx.app.view.main.main(sys.argv)
    
def app_pyfai_calib2():
    result = pyFAI.app.calib2.main()
    sys.exit(result)
    
def app_pyfai_integrate():
    pyFAI.app.integrate.main()


class Launcher(QWidget):
    def __init__(self):
        super().__init__()        
        self.setWindowTitle('Easy pyFAI')
        
        self.label = QtWidgets.QLabel('Click to Launch silx & pyFAI Apps')
        self.pushButton_silxview = QtWidgets.QPushButton('silx view')
        self.pushButton_pyfaicalib2 = QtWidgets.QPushButton('pyFAI-calib2')
        self.pushButton_pyfaiintegrate = QtWidgets.QPushButton('pyFAI-integrate')
        self.verticalLayout = QVBoxLayout()
        self.setLayout(self.verticalLayout)
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.pushButton_silxview)
        self.verticalLayout.addWidget(self.pushButton_pyfaicalib2)
        self.verticalLayout.addWidget(self.pushButton_pyfaiintegrate)
        
        self.pushButton_silxview.clicked.connect(self.launch_silxview)
        self.pushButton_pyfaicalib2.clicked.connect(self.launch_pyfaicalib2)
        self.pushButton_pyfaiintegrate.clicked.connect(self.launch_pyfaiintegrate)
        
    def launch_silxview(self):
        Process(target=app_silx_view).start()
    
    def launch_pyfaicalib2(self):
        Process(target=app_pyfai_calib2).start()
    
    def launch_pyfaiintegrate(self):
        Process(target=app_pyfai_integrate).start()


if __name__ == "__main__":
    freeze_support()
    
    app = QApplication(sys.argv)
    window = Launcher()
    window.show()
    sys.exit(app.exec_())
    