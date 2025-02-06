from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap

from View.ui_Template_Menu_View import Ui_TemplateMenuView


class TemplateMenuView(QWidget, Ui_TemplateMenuView):
    TMV_back_button_signal = pyqtSignal()
    TMV_confirm_button_signal = pyqtSignal()
    TMV_touch_event_signal = pyqtSignal(str)
    
    def __init__(self) -> None:
        super().__init__()
        self.startPos = None
        self.current_index = 0
        self.labels = []
        self.template_path_list = []
        for i in range(1, 9):
            self.template_path_list.append(f"Data/Template/template{i}.png")
        
        self.setupUi(self)
        
        self.template_menu_container_widget = QWidget(self.template_menu_frame)
        
        
        template_pixmap = QPixmap("Data/Template/test_template_2x1.png")
        scaled_template_pixmap = template_pixmap.scaled(1030,1030, Qt.KeepAspectRatio)
        self.template_show_label.setPixmap(scaled_template_pixmap)
        
        self.back_button.clicked.connect(self.emit_back_button_clicked_signal)
        self.confirm_button.clicked.connect(self.emit_confirm_button_clicked_signal)
        
        
    
    # def handleMousePressEvent(self, event):
    #     """Capture the start position of the swipe"""
    #     if event.button() == Qt.LeftButton:
    #         self.start_pos = event.pos()

    # def mouseReleaseEvent(self, event):
    #     """Handle the swipe detection and animate the label update"""
    #     if self.start_pos:
    #         end_pos = event.pos()
    #         delta_x = end_pos.x() - self.start_pos.x()
            
    #         if delta_x <= -10:  # Swipe left
    #             self.TMV_touch_event_signal.emit("swipe left")
    #         elif delta_x >= 10:  # Swipe right
    #             self.TMV_touch_event_signal.emit("swipe right")
    #         else:
    #             self.TMV_touch_event_signal.emit("None touch")
    #     self.start_pos = None
    
    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.startPos = event.pos()
        
    # def handleMouseMoveEvent(self, event):
    #     if self.startPos:
    #         delta = event.pos() - self.startPos
    #         new_x = self.template_menu_container_widget.x() + delta.x()
    #         new_x = max(min(new_x, 0), -600)  # Ensure new_x is between -600 and 0
            
    #         self.template_menu_container_widget.move(new_x, self.template_menu_container_widget.y())
    #         self.startPos = event.pos()
    
    # def mouseReleaseEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         if self.startPos and (event.pos() - self.startPos).manhattanLength() <= 10:
    #             self.handle_touch(event.pos())
    #         self.startPos = None
    
    # def handle_touch(self, pos):
    #     for widget in self.widgets:
    #         if widget.geometry().contains(self.container.mapFromParent(pos)):
    #             self.info_widget.setStyleSheet(widget.styleSheet())
    #             break
    
    
    
    
    
    
    
    
    
    def update_template_show_label(self, template_path):
        pixmap = QPixmap(template_path)
        self.template_show_label.setPixmap(pixmap.scaled(1030, 1030, Qt.KeepAspectRatio))  # Kích thước lớn hơn

    
    #slot
    def emit_back_button_clicked_signal(self) -> None:
        self.TMV_back_button_signal.emit()
        
    def emit_confirm_button_clicked_signal(self) -> None:
        self.TMV_confirm_button_signal.emit()