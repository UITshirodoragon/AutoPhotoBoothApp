# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Template_Export_ViewEeQBKO.ui'
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

class Ui_TemplateExportView(object):
    def setupUi(self, TemplateExportView):
        if not TemplateExportView.objectName():
            TemplateExportView.setObjectName(u"TemplateExportView")
        TemplateExportView.resize(1080, 1920)
        self.back_button = QPushButton(TemplateExportView)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(25, 25, 100, 100))
        icon = QIcon()
        icon.addFile(u":/View/Icon/left_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QSize(100, 100))
        self.thanks_text_label = QLabel(TemplateExportView)
        self.thanks_text_label.setObjectName(u"thanks_text_label")
        self.thanks_text_label.setGeometry(QRect(150, 25, 780, 100))
        self.thanks_text_label.setTextFormat(Qt.TextFormat.AutoText)
        self.thanks_text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.template_show_label = QLabel(TemplateExportView)
        self.template_show_label.setObjectName(u"template_show_label")
        self.template_show_label.setGeometry(QRect(25, 150, 1030, 1030))
        self.template_show_label.setStyleSheet(u"background-color: rgb(125, 125, 125);")
        self.template_show_label.setScaledContents(False)
        self.template_show_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scan_text_label = QLabel(TemplateExportView)
        self.scan_text_label.setObjectName(u"scan_text_label")
        self.scan_text_label.setGeometry(QRect(25, 1200, 1030, 50))
        self.scan_text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.qr_code_image_label = QLabel(TemplateExportView)
        self.qr_code_image_label.setObjectName(u"qr_code_image_label")
        self.qr_code_image_label.setGeometry(QRect(25, 1275, 1030, 500))
        self.qr_code_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.restart_button = QPushButton(TemplateExportView)
        self.restart_button.setObjectName(u"restart_button")
        self.restart_button.setGeometry(QRect(25, 1795, 1030, 100))
        icon1 = QIcon()
        icon1.addFile(u":/View/Icon/restart_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restart_button.setIcon(icon1)
        self.restart_button.setIconSize(QSize(30, 30))

        self.retranslateUi(TemplateExportView)

        QMetaObject.connectSlotsByName(TemplateExportView)
    # setupUi

    def retranslateUi(self, TemplateExportView):
        TemplateExportView.setWindowTitle(QCoreApplication.translate("TemplateExportView", u"Form", None))
        self.back_button.setText("")
        self.thanks_text_label.setText(QCoreApplication.translate("TemplateExportView", u"Thanks for using our service", None))
        self.template_show_label.setText("")
        self.scan_text_label.setText(QCoreApplication.translate("TemplateExportView", u"Scan QR code to download", None))
        self.qr_code_image_label.setText("")
        self.restart_button.setText(QCoreApplication.translate("TemplateExportView", u"TAP TO RESTART", None))
    # retranslateUi

