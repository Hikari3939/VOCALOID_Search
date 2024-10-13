from PySide6 import QtCore, QtWidgets, QtGui

import sys
import random

from Main_Window_ui import Ui_Main_Window

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = QtWidgets.QWidget()
    ui = Ui_Main_Window()
    ui.setupUi(widget)
    widget.show()

    sys.exit(app.exec())