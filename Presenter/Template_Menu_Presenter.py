from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap

from View.Template_Menu_View import TemplateMenuView
from Model.Template_Menu_Model import TemplateMenuModel
from Model.User_Model import *

class TemplateMenuPresenter:
    def __init__(self, model: TemplateMenuModel, view: TemplateMenuView, stack_view: QStackedWidget, user_control_model: UserModel) -> None:
        self.model = model
        self.view = view
        self.stack_view = stack_view
        
        self.current_index = 0
        self.labels = []
        self.start_pos = None
        
        self.view.TMV_back_button_signal.connect(self.handle_back_button_clicked)
        self.view.TMV_confirm_button_signal.connect(self.handle_confirm_button_clicked)
        
        self.handle_template_menu_label()
        self.view.TMV_touch_event_signal.connect(self.handle_update_small_template_labels_in_menu)
        
    def handle_back_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(0)
        
    def handle_confirm_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(2)
        
    def handle_template_menu_label(self):
        for i in range(len(self.model.template_path_list) // 4 + 1):
            widget = QWidget()
            widget_layout = QHBoxLayout()
            for j in range(4):
                if self.current_index < len(self.model.template_path_list):
                    label = QLabel()
                    pixmap = QPixmap(self.model.template_path_list[self.current_index])
                    label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))  # Kích thước nhỏ hơn
                    label.mousePressEvent = self.handle_mouse_press_event_small_template_label_in_menu()  # Thiết lập sự kiện click
                    label.mouseReleaseEvent = self.handle_mouse_release_event_small_template_label_in_menu(self.current_index)
                    widget_layout.addWidget(label)
                    self.labels.append(label)
                    self.current_index += 1
            widget.setLayout(widget_layout)
            self.view.template_widget_stack.addWidget(widget)

    
    # overide mouse event method for small template in menu
    def handle_mouse_press_event_small_template_label_in_menu(self):
        def handler(event):
            self.start_pos = event.pos()
        return handler
    
    def handle_mouse_release_event_small_template_label_in_menu(self, index):
        def handler(event):
            delta_x = None
            if self.start_pos:
                end_pos = event.pos()
                delta_x = end_pos.x() - self.start_pos.x()
            
            
            if delta_x is None:
                pass 
            elif delta_x > -50 and delta_x < 50: 
                self.view.update_template_show_label(self.model.template_path_list[index])  # Kích thước lớn hơn
            elif delta_x >= 50:
                self.view.TMV_touch_event_signal.emit("swipe right")
            elif delta_x <= -50:
                self.view.TMV_touch_event_signal.emit("swipe left")
            self.start_pos = None
        return handler
    
    def handle_update_small_template_labels_in_menu(self, touch_event):
        """Update the visible labels based on the swipe direction"""
        if touch_event == 'swipe left' and self.view.template_widget_stack.currentIndex() > 0:
            self.view.template_widget_stack.setCurrentIndex(self.view.template_widget_stack.currentIndex() - 1)
        elif touch_event == 'swipe right' and self.view.template_widget_stack.currentIndex() < self.view.template_widget_stack.count() - 1:
            self.view.template_widget_stack.setCurrentIndex(self.view.template_widget_stack.currentIndex() + 1)