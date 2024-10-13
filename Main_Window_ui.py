# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QSizePolicy, QWidget)

class Ui_Main_Window(object):
    def setupUi(self, Main_Window):
        if not Main_Window.objectName():
            Main_Window.setObjectName(u"Main_Window")
        Main_Window.resize(960, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main_Window.sizePolicy().hasHeightForWidth())
        Main_Window.setSizePolicy(sizePolicy)
        Main_Window.setMinimumSize(QSize(720, 640))
        Main_Window.setAutoFillBackground(False)
        self.lineEdit_search = QLineEdit(Main_Window)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setGeometry(QRect(300, 170, 360, 36))
        self.lineEdit_search.setFrame(False)

        self.retranslateUi(Main_Window)

        QMetaObject.connectSlotsByName(Main_Window)
    # setupUi

    def retranslateUi(self, Main_Window):
        Main_Window.setWindowTitle(QCoreApplication.translate("Main_Window", u"VOCALOID_Music", None))
    # retranslateUi

