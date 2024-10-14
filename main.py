from PySide6 import QtCore, QtWidgets, QtGui

import sys
import random

from Main_Window import Main_Window

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Main_Window()
    widget.show()

    sys.exit(app.exec())