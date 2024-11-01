from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QListWidgetItem, QProgressBar
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
        
        # template_pixmap = QPixmap("Data/Template/template1.png")
        # scaled_template_pixmap = template_pixmap.scaled(1030,1030, Qt.KeepAspectRatio)
        # self.template_show_label.setPixmap(scaled_template_pixmap)
        self.process_export_final_template_progress_bar = QProgressBar(self)
        self.process_export_final_template_progress_bar.setGeometry(25, 910, 1030, 100)
        self.process_export_final_template_progress_bar.setMaximum(100)
        self.process_export_final_template_progress_bar.setTextVisible(False)
        
        # Increase font size of percentage text
  
        # qr_code_image_pixmap = QPixmap("Data/ImageGallery/qr_code_google_drive.png")
        # scaled_qr_code_image_pixmap = qr_code_image_pixmap.scaled(1030,500, Qt.KeepAspectRatio)
        # self.qr_code_image_label.setPixmap(scaled_qr_code_image_pixmap)
 
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
        
    def hide_all_widgets(self) -> None:
        self.scan_text_label.hide()
        self.thanks_text_label.hide()
        self.template_show_label.hide()
        self.qr_code_image_label.hide()
        self.restart_button.hide()
        self.back_button.hide()
        self.process_export_final_template_progress_bar.show()
        
    def show_all_widgets(self) -> None:
        self.thanks_text_label.show()
        self.scan_text_label.show()
        self.template_show_label.show()
        self.qr_code_image_label.show()
        self.restart_button.show()
        self.back_button.show()
        self.process_export_final_template_progress_bar.hide()
        
    def update_process_export_final_template_progress_bar_gui(self, value) -> None:
        print(value)
        self.process_export_final_template_progress_bar.setValue(value)