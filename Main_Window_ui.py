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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, ImageLabel, ScrollArea, SearchLineEdit,
    TextBrowser, TitleLabel)

class Ui_Main_Window(object):
    def setupUi(self, Main_Window):
        if not Main_Window.objectName():
            Main_Window.setObjectName(u"Main_Window")
        Main_Window.resize(1024, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main_Window.sizePolicy().hasHeightForWidth())
        Main_Window.setSizePolicy(sizePolicy)
        Main_Window.setMinimumSize(QSize(1024, 640))
        Main_Window.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(Main_Window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 1, -1, -1)
        self.horizontalLayout_title = QHBoxLayout()
        self.horizontalLayout_title.setSpacing(0)
        self.horizontalLayout_title.setObjectName(u"horizontalLayout_title")
        self.horizontalLayout_title.setContentsMargins(24, -1, 24, 0)
        self.label_title = TitleLabel(Main_Window)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamilies([u"\u841d\u8389\u4f53 \u7b2c\u4e8c\u7248"])
        font.setPointSize(22)
        self.label_title.setFont(font)

        self.horizontalLayout_title.addWidget(self.label_title)

        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_title.addItem(self.horizontalSpacer_1)

        self.horizontalLayout_title.setStretch(0, 3)
        self.horizontalLayout_title.setStretch(1, 6)

        self.verticalLayout.addLayout(self.horizontalLayout_title)

        self.horizontalLayout_search = QHBoxLayout()
        self.horizontalLayout_search.setSpacing(0)
        self.horizontalLayout_search.setObjectName(u"horizontalLayout_search")
        self.horizontalLayout_search.setContentsMargins(0, 0, 0, 24)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_search.addItem(self.horizontalSpacer_2)

        self.lineEdit_search = SearchLineEdit(Main_Window)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_search.sizePolicy().hasHeightForWidth())
        self.lineEdit_search.setSizePolicy(sizePolicy1)
        self.lineEdit_search.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(12)
        self.lineEdit_search.setFont(font1)
        self.lineEdit_search.setFrame(False)
        self.lineEdit_search.setCursorPosition(0)

        self.horizontalLayout_search.addWidget(self.lineEdit_search)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_search.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_search.setStretch(0, 1)
        self.horizontalLayout_search.setStretch(1, 3)
        self.horizontalLayout_search.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_search)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea_music = ScrollArea(Main_Window)
        self.scrollArea_music.setObjectName(u"scrollArea_music")
        self.scrollArea_music.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 500, 437))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_1 = CardWidget(self.scrollAreaWidgetContents)
        self.widget_1.setObjectName(u"widget_1")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_picture_1 = ImageLabel(self.widget_1)
        self.label_picture_1.setObjectName(u"label_picture_1")

        self.horizontalLayout_2.addWidget(self.label_picture_1)

        self.textBrowser_1 = TextBrowser(self.widget_1)
        self.textBrowser_1.setObjectName(u"textBrowser_1")

        self.horizontalLayout_2.addWidget(self.textBrowser_1)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.widget_1)

        self.widget_2 = CardWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_picture_2 = ImageLabel(self.widget_2)
        self.label_picture_2.setObjectName(u"label_picture_2")

        self.horizontalLayout_3.addWidget(self.label_picture_2)

        self.textBrowser_2 = TextBrowser(self.widget_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.horizontalLayout_3.addWidget(self.textBrowser_2)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_3 = CardWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_picture_3 = ImageLabel(self.widget_3)
        self.label_picture_3.setObjectName(u"label_picture_3")

        self.horizontalLayout_4.addWidget(self.label_picture_3)

        self.textBrowser_3 = TextBrowser(self.widget_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.horizontalLayout_4.addWidget(self.textBrowser_3)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.widget_3)

        self.scrollArea_music.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea_music)

        self.textBrowser_details = TextBrowser(Main_Window)
        self.textBrowser_details.setObjectName(u"textBrowser_details")

        self.horizontalLayout.addWidget(self.textBrowser_details)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 5)

        self.retranslateUi(Main_Window)

        QMetaObject.connectSlotsByName(Main_Window)
    # setupUi

    def retranslateUi(self, Main_Window):
        Main_Window.setWindowTitle(QCoreApplication.translate("Main_Window", u"VOCALOID_Music", None))
        self.label_title.setText(QCoreApplication.translate("Main_Window", u"VOCALOID MUSIC ", None))
        self.label_picture_1.setText("")
        self.label_picture_2.setText("")
        self.label_picture_3.setText("")
    # retranslateUi

