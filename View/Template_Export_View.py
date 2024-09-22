from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap

class TemplateExportView(QWidget):
    TEV_back_button_signal = pyqtSignal()
    TEV_restart_button_signal = pyqtSignal()
    
    
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Template export view")
        self.setGeometry(0,0,450,800)
        self.setMinimumSize(450,800)
        self.initUI()
        
    def initUI(self) -> None:
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.emit_back_button_clicked_signal)
        self.back_button.setGeometry(25,25,50,50)
        
        
        self.template_text_label = QLabel("Thank you", self)
        self.template_text_label.setGeometry(100,25,200,50)
        
        
        self.template_show_label = QLabel("Template show", self)
        self.template_show_label.setGeometry(25,100,400,300)
        template_pixmap = QPixmap("Data/Template/layout2.png")
        scaled_template_pixmap = template_pixmap.scaled(400,300)
        self.template_show_label.setPixmap(scaled_template_pixmap)
        
        
        self.template_scan_text_label = QLabel("Scan to download", self)
        self.template_scan_text_label.setGeometry(0,400,450,50)
        
        self.template_qr_code_image_label = QLabel("Qr code", self)
        self.template_qr_code_image_label.setGeometry(125,450,200,200)
        qr_code_image_pixmap = QPixmap("Data/ImageGallery/qr_code_google_drive.png")
        scaled_qr_code_image_pixmap = qr_code_image_pixmap.scaled(200,200)
        self.template_qr_code_image_label.setPixmap(scaled_qr_code_image_pixmap)
        
        self.restart_button = QPushButton("Tap to restart", self)
        self.restart_button.setGeometry(0,750,450,50)
        self.restart_button.clicked.connect(self.emit_restart_button_clicked_signal)
        
        
    #slot
    def emit_back_button_clicked_signal(self) -> None:
        self.TEV_back_button_signal.emit()
        
    def emit_restart_button_clicked_signal(self) -> None:
        self.TEV_restart_button_signal.emit()