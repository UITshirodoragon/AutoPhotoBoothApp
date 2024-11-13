from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QListWidgetItem, QProgressBar
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap

from View.ui_Template_Image_Preview_View import Ui_Template_Image_Preview_View
from View.Alert_Box_View import AlertBoxView

class TemplateImagePreviewView(QWidget, Ui_Template_Image_Preview_View):
    TIPV_restart_capture_button_clicked_signal = pyqtSignal()
    TIPV_confirm_capture_button_clicked_signal = pyqtSignal()
    TIPV_export_template_button_clicked_signal = pyqtSignal()
    
    
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        self.hide_preview_countdown_label_gui()

        self.restart_capture_button.clicked.connect(self.emit_restart_capture_button_clicked_signal)
        self.confirm_capture_button.clicked.connect(self.emit_confirm_capture_button_clicked_signal)
        self.export_template_button.clicked.connect(self.emit_export_template_button_clicked_signal)

    def emit_restart_capture_button_clicked_signal(self) -> None:
        self.TIPV_restart_capture_button_clicked_signal.emit()
    
    def emit_confirm_capture_button_clicked_signal(self) -> None:
        self.TIPV_confirm_capture_button_clicked_signal.emit()
        
    def emit_export_template_button_clicked_signal(self) -> None:
        self.TIPV_export_template_button_clicked_signal.emit()
        
    def update_preview_template_gui(self, preview_template_path: str) -> None:
        preview_template_pixmap = QPixmap(preview_template_path)
        scaled_preview_template_pixmap = preview_template_pixmap.scaled(1030, 1030, Qt.KeepAspectRatio)
        self.preview_template_label.setPixmap(scaled_preview_template_pixmap)
        
    def update_raw_image_gui(self, raw_image_path: str) -> None:
        raw_image_pixmap = QPixmap(raw_image_path)
        scaled_raw_image_pixmap = raw_image_pixmap.scaled(500, 500, Qt.KeepAspectRatio)
        self.raw_image_label.setPixmap(scaled_raw_image_pixmap)
        
    def update_image_with_background_gui(self, image_with_background_path: str) -> None:
        image_with_background_pixmap = QPixmap(image_with_background_path)
        scaled_image_with_background_pixmap = image_with_background_pixmap.scaled(500, 500, Qt.KeepAspectRatio)
        self.image_with_background_label.setPixmap(scaled_image_with_background_pixmap)
        
    def update_image_info_label_gui(self, image_info: str) -> None:
        self.image_info_label.setText(image_info)
        
    def update_preview_countdown_label_gui(self, preview_countdown: str) -> None:
        self.preview_countdown_label.setText(preview_countdown)
        
    def show_preview_countdown_label_gui(self) -> None:
        self.preview_countdown_label.show()
        
    def hide_preview_countdown_label_gui(self) -> None:
        self.preview_countdown_label.hide()
        
    def show_dialog_alert_to_restart_capture(self) -> None:
        alert_go_back_box = AlertBoxView(self)
        alert_go_back_box.setGeometry(340, 860, 400, 200)
        alert_go_back_box.set_alert_title_label("Restart Capture")
        alert_go_back_box.set_alert_content_label("Are you sure you want to restart the capture?")
        reply = alert_go_back_box.exec_()
        return reply