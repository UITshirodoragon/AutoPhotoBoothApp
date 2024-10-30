# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Template_Menu_ViewRvXrJf.ui'
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
from PyQt5.QtWidgets import (QApplication, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QWidget, QFrame)
import View.UI_ViewResource_rc

class Ui_TemplateMenuView(object):
    def setupUi(self, TemplateMenuView):
        if not TemplateMenuView.objectName():
            TemplateMenuView.setObjectName(u"TemplateMenuView")
        TemplateMenuView.resize(1080, 1920)
        TemplateMenuView.setMaximumSize(QSize(1080, 1920))
        TemplateMenuView.setBaseSize(QSize(1080, 1920))
        self.back_button = QPushButton(TemplateMenuView)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(25, 25, 100, 100))
        icon = QIcon()
        icon.addFile(u":/View/Icon/left_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QSize(100, 100))
        self.confirm_button = QPushButton(TemplateMenuView)
        self.confirm_button.setObjectName(u"confirm_button")
        self.confirm_button.setGeometry(QRect(440, 1520, 200, 100))
        self.template_show_label = QLabel(TemplateMenuView)
        self.template_show_label.setObjectName(u"template_show_label")
        self.template_show_label.setGeometry(QRect(25, 150, 1030, 1030))
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        self.template_show_label.setFont(font)
        self.template_show_label.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.template_show_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.template_menu_box = QGroupBox(TemplateMenuView)
        self.template_menu_box.setObjectName(u"template_menu_box")
        self.template_menu_box.setGeometry(QRect(15, 1200, 1050, 300))
        self.template_menu_frame = QFrame(self.template_menu_box)
        self.template_menu_frame.setObjectName(u"template_menu_frame")
        self.template_menu_frame.setGeometry(QRect(10, 25, 1030, 250))
        self.template_menu_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.template_menu_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.retranslateUi(TemplateMenuView)

        QMetaObject.connectSlotsByName(TemplateMenuView)
    # setupUi

    def retranslateUi(self, TemplateMenuView):
        TemplateMenuView.setWindowTitle(QCoreApplication.translate("TemplateMenuView", u"Form", None))
        self.back_button.setText("")
        self.confirm_button.setText(QCoreApplication.translate("TemplateMenuView", u"CONFIRM", None))
        self.template_show_label.setText(QCoreApplication.translate("TemplateMenuView", u"SELECT YOUR TEMPLATE", None))
        self.template_menu_box.setTitle(QCoreApplication.translate("TemplateMenuView", u"TEMPLATE MENU", None))
    # retranslateUi


