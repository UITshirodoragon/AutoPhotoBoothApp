from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap

class TemplateMenuView(QWidget):
    TMV_back_button_signal = pyqtSignal()
    TMV_confirm_button_signal = pyqtSignal()
    
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Template menu view")
        self.setGeometry(0,0,450,800)
        self.setMinimumSize(450,800)
        self.initUI()
        
    def initUI(self) -> None:
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.emit_back_button_clicked_signal)
        self.back_button.setGeometry(25,25,50,50)
        
        
        self.template_text_label = QLabel("Choose your template", self)
        self.template_text_label.setGeometry(100,25,200,50)
        
        
        self.template_show_label = QLabel("Template show", self)
        self.template_show_label.setGeometry(25,100,400,300)
        template_pixmap = QPixmap("Data/Template/layout2.png")
        scaled_template_pixmap = template_pixmap.scaled(400,300)
        self.template_show_label.setPixmap(scaled_template_pixmap)
        
        
        self.confirm_button = QPushButton("Confirm", self)
        self.confirm_button.setGeometry(0,700,450,50)
        self.confirm_button.clicked.connect(self.emit_confirm_button_clicked_signal)
        
        
        
        
    #slot
    def emit_back_button_clicked_signal(self) -> None:
        self.TMV_back_button_signal.emit()
        
    def emit_confirm_button_clicked_signal(self) -> None:
        self.TMV_confirm_button_signal.emit()