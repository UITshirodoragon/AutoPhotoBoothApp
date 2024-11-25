# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Template_Image_Preview_ViewNJLkLy.ui'
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


class Ui_Template_Image_Preview_View(object):
    def setupUi(self, Template_Image_Preview_View):
        if not Template_Image_Preview_View.objectName():
            Template_Image_Preview_View.setObjectName(u"Template_Image_Preview_View")
        Template_Image_Preview_View.resize(1080, 1920)
        Template_Image_Preview_View.setMinimumSize(QSize(1080, 1920))
        self.preview_template_label = QLabel(Template_Image_Preview_View)
        self.preview_template_label.setObjectName(u"preview_template_label")
        self.preview_template_label.setGeometry(QRect(25, 150, 1030, 1030))
        self.preview_template_label.setStyleSheet(u"background-color: rgb(134, 134, 134);")
        self.raw_image_label = QLabel(Template_Image_Preview_View)
        self.raw_image_label.setObjectName(u"raw_image_label")
        self.raw_image_label.setGeometry(QRect(25, 1210, 500, 500))
        self.raw_image_label.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.image_with_background_label = QLabel(Template_Image_Preview_View)
        self.image_with_background_label.setObjectName(u"image_with_background_label")
        self.image_with_background_label.setGeometry(QRect(555, 1210, 500, 500))
        self.image_with_background_label.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.restart_capture_button = QPushButton(Template_Image_Preview_View)
        self.restart_capture_button.setObjectName(u"restart_capture_button")
        self.restart_capture_button.setGeometry(QRect(150, 1740, 250, 150))
        self.restart_capture_button.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        icon = QIcon()
        icon.addFile(u":/View/Icon/restart_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restart_capture_button.setIcon(icon)
        self.restart_capture_button.setIconSize(QSize(50, 50))
        self.confirm_capture_button = QPushButton(Template_Image_Preview_View)
        self.confirm_capture_button.setObjectName(u"confirm_capture_button")
        self.confirm_capture_button.setGeometry(QRect(680, 1740, 250, 150))
        self.confirm_capture_button.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/View/Icon/check_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.confirm_capture_button.setIcon(icon1)
        self.confirm_capture_button.setIconSize(QSize(50, 50))
        self.export_template_button = QPushButton(Template_Image_Preview_View)
        self.export_template_button.setObjectName(u"export_template_button")
        self.export_template_button.setGeometry(QRect(415, 1740, 250, 150))
        self.export_template_button.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/View/Icon/export_template_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.export_template_button.setIcon(icon2)
        self.export_template_button.setIconSize(QSize(50, 50))
        self.image_info_label = QLabel(Template_Image_Preview_View)
        self.image_info_label.setObjectName(u"image_info_label")
        self.image_info_label.setGeometry(QRect(25, 25, 1030, 100))
        self.image_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview_countdown_label = QLabel(Template_Image_Preview_View)
        self.preview_countdown_label.setObjectName(u"preview_countdown_label")
        self.preview_countdown_label.setGeometry(QRect(855, 25, 200, 100))
        self.preview_countdown_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(Template_Image_Preview_View)

        QMetaObject.connectSlotsByName(Template_Image_Preview_View)
    # setupUi

    def retranslateUi(self, Template_Image_Preview_View):
        Template_Image_Preview_View.setWindowTitle(QCoreApplication.translate("Template_Image_Preview_View", u"Form", None))
        self.preview_template_label.setText("")
        self.raw_image_label.setText("")
        self.image_with_background_label.setText("")
        self.restart_capture_button.setText(QCoreApplication.translate("Template_Image_Preview_View", u"CAPTURE AGAIN", None))
        self.confirm_capture_button.setText(QCoreApplication.translate("Template_Image_Preview_View", u"OK", None))
        self.export_template_button.setText(QCoreApplication.translate("Template_Image_Preview_View", u"EXPORT TEMPLATE", None))
        self.image_info_label.setText(QCoreApplication.translate("Template_Image_Preview_View", u"IMAGE #...", None))
        self.preview_countdown_label.setText(QCoreApplication.translate("Template_Image_Preview_View", u"CONTINUE IN ...", None))
    # retranslateUi

