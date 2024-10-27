from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap

from View.ui_Template_Export_View import Ui_TemplateExportView


class TemplateExportView(QWidget, Ui_TemplateExportView):
    TEV_back_button_signal = pyqtSignal()
    TEV_restart_button_signal = pyqtSignal()
    
    
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.back_button.clicked.connect(self.emit_back_button_clicked_signal)
        
        template_pixmap = QPixmap("Data/Template/template1.png")
        scaled_template_pixmap = template_pixmap.scaled(1030,1030, Qt.KeepAspectRatio)
        self.template_show_label.setPixmap(scaled_template_pixmap)
        
  
        qr_code_image_pixmap = QPixmap("Data/ImageGallery/qr_code_google_drive.png")
        scaled_qr_code_image_pixmap = qr_code_image_pixmap.scaled(1030,500, Qt.KeepAspectRatio)
        self.qr_code_image_label.setPixmap(scaled_qr_code_image_pixmap)
 
        self.restart_button.clicked.connect(self.emit_restart_button_clicked_signal)
        
        
    #slot
    def emit_back_button_clicked_signal(self) -> None:
        self.TEV_back_button_signal.emit()
        
    def emit_restart_button_clicked_signal(self) -> None:
        self.TEV_restart_button_signal.emit()
        
    def update_final_template_with_images_gui(self, user_final_template_path) -> None:
        template_pixmap = QPixmap(user_final_template_path)
        scaled_template_pixmap = template_pixmap.scaled(1030, 1030, Qt.KeepAspectRatio)
        self.template_show_label.setPixmap(scaled_template_pixmap)