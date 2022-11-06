from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtCore import Qt

import sys
if __name__ == '__main__':
    Appltext = ApplicationContext()
    window = QMainWindow()
    window.setWindowTitle("Hello World!")
    window.resize(800, 680)
    label = QLabel("Hello World!")
    label.setAlignment(Qt.AlignCenter)
    window.setCentralWidget(label)
    window.show()
    exit_code = Appltext.app.exec_()
    sys.exit(exit_code)
