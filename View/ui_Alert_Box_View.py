# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Alert_Box_ViewnCPGoN.ui'
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

class Ui_AlertBoxView(object):
    def setupUi(self, AlertBoxView):
        if not AlertBoxView.objectName():
            AlertBoxView.setObjectName(u"AlertBoxView")
        AlertBoxView.resize(400, 200)
        AlertBoxView.setStyleSheet(u"")
        self.alert_box_container_widget = QWidget(AlertBoxView)
        self.alert_box_container_widget.setObjectName(u"alert_box_container_widget")
        self.alert_box_container_widget.setGeometry(QRect(0, 0, 400, 200))
        self.alert_box_container_widget.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.yes_button = QPushButton(self.alert_box_container_widget)
        self.yes_button.setObjectName(u"yes_button")
        self.yes_button.setGeometry(QRect(210, 125, 170, 50))
        self.no_button = QPushButton(self.alert_box_container_widget)
        self.no_button.setObjectName(u"no_button")
        self.no_button.setGeometry(QRect(20, 125, 170, 50))
        self.alert_title_label = QLabel(self.alert_box_container_widget)
        self.alert_title_label.setObjectName(u"alert_title_label")
        self.alert_title_label.setGeometry(QRect(25, 25, 350, 50))
        self.alert_content_label = QLabel(self.alert_box_container_widget)
        self.alert_content_label.setObjectName(u"alert_content_label")
        self.alert_content_label.setGeometry(QRect(25, 75, 350, 50))
        self.alert_content_label.setTextFormat(Qt.TextFormat.MarkdownText)
        self.alert_content_label.setScaledContents(True)
        self.alert_content_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.alert_content_label.setWordWrap(True)
        self.alert_content_label.setIndent(-1)

        self.retranslateUi(AlertBoxView)

        QMetaObject.connectSlotsByName(AlertBoxView)
    # setupUi

    def retranslateUi(self, AlertBoxView):
        AlertBoxView.setWindowTitle(QCoreApplication.translate("AlertBoxView", u"Form", None))
        self.yes_button.setText(QCoreApplication.translate("AlertBoxView", u"YES", None))
        self.no_button.setText(QCoreApplication.translate("AlertBoxView", u"NO", None))
        self.alert_title_label.setText(QCoreApplication.translate("AlertBoxView", u"ALERT TITLE", None))
        self.alert_content_label.setText(QCoreApplication.translate("AlertBoxView", u"Content of alert", None))
    # retranslateUi



