# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Image_Capture_ViewTgRpWQ.ui'
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
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
import View.UI_ViewResource_rc

class Ui_Image_Capture_View(object):
    def setupUi(self, Image_Capture_View):
        if not Image_Capture_View.objectName():
            Image_Capture_View.setObjectName(u"Image_Capture_View")
        Image_Capture_View.resize(1080, 1920)
        self.next_button = QPushButton(Image_Capture_View)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setGeometry(QRect(955, 25, 100, 100))
        icon = QIcon()
        icon.addFile(u":/View/Icon/right_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.next_button.setIcon(icon)
        self.next_button.setIconSize(QSize(100, 100))
        self.preview_fps_label = QLabel(Image_Capture_View)
        self.preview_fps_label.setObjectName(u"preview_fps_label")
        self.preview_fps_label.setGeometry(QRect(25, 1600, 50, 50))
        self.preview_fps_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.capture_button = QPushButton(Image_Capture_View)
        self.capture_button.setObjectName(u"capture_button")
        self.capture_button.setGeometry(QRect(490, 1600, 100, 100))
        icon1 = QIcon()
        icon1.addFile(u":/View/Icon/Capture_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.capture_button.setIcon(icon1)
        self.capture_button.setIconSize(QSize(100, 100))
        self.preview_image_label = QLabel(Image_Capture_View)
        self.preview_image_label.setObjectName(u"preview_image_label")
        self.preview_image_label.setGeometry(QRect(0, 150, 1080, 1440))
        self.preview_image_label.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.preview_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.back_button = QPushButton(Image_Capture_View)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(25, 25, 100, 100))
        icon2 = QIcon()
        icon2.addFile(u":/View/Icon/left_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_button.setIcon(icon2)
        self.back_button.setIconSize(QSize(100, 100))

        self.retranslateUi(Image_Capture_View)

        QMetaObject.connectSlotsByName(Image_Capture_View)
    # setupUi

    def retranslateUi(self, Image_Capture_View):
        Image_Capture_View.setWindowTitle(QCoreApplication.translate("Image_Capture_View", u"Form", None))
        self.next_button.setText("")
        self.preview_fps_label.setText(QCoreApplication.translate("Image_Capture_View", u"FPS", None))
        self.capture_button.setText("")
        self.preview_image_label.setText("")
        self.back_button.setText("")
    # retranslateUi



