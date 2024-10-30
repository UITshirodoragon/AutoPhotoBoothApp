# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Start_ViewQcVRDV.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_Start_View(object):
    def setupUi(self, Start_View):
        if not Start_View.objectName():
            Start_View.setObjectName(u"Start_View")
        Start_View.resize(1080, 1920)
        self.start_button = QPushButton(Start_View)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(0, 150, 1080, 1620))
        self.settings_button = QPushButton(Start_View)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(25, 25, 100, 100))
        self.quit_button = QPushButton(Start_View)
        self.quit_button.setObjectName(u"quit_button")
        self.quit_button.setGeometry(QRect(955, 25, 100, 100))

        self.retranslateUi(Start_View)

        QMetaObject.connectSlotsByName(Start_View)
    # setupUi

    def retranslateUi(self, Start_View):
        Start_View.setWindowTitle(QCoreApplication.translate("Start_View", u"Form", None))
        self.start_button.setText(QCoreApplication.translate("Start_View", u"TAP TO START", None))
        self.settings_button.setText(QCoreApplication.translate("Start_View", u"SETTINGS", None))
        self.quit_button.setText(QCoreApplication.translate("Start_View", u"QUIT", None))
    # retranslateUi

