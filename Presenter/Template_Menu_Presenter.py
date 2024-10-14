from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap

from View.Template_Menu_View import TemplateMenuView
from Model.Template_Menu_Model import TemplateMenuModel
from Model.User_Model import *
from Model.Template_Model import TemplateModel

class TemplateMenuPresenter:
    def __init__(self, model: TemplateMenuModel, 
                 view: TemplateMenuView, 
                 stack_view: QStackedWidget, 
                 user_control_model: UserModel,
                 template_control_model: TemplateModel
                 ) -> None:
        self.model = model
        self.view = view
        self.stack_view = stack_view
        self.template_control_model = template_control_model
        
        self.current_index = 1
        self.small_template_labels = []
        self.start_pos = None
        self.selected_template_id = 1
        
        self.view.TMV_back_button_signal.connect(self.handle_back_button_clicked)
        self.view.TMV_confirm_button_signal.connect(self.handle_confirm_button_clicked)
        
        self.handle_template_menu_label()
        self.view.TMV_touch_event_signal.connect(self.handle_update_small_template_labels_in_menu)
        
    def handle_back_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(0)
        
        
    def handle_confirm_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(2)
        # confirm final
        self.template_control_model.selected_template_id = self.selected_template_id
        
    def handle_template_menu_label(self):
        for i in range(self.template_control_model.count_templates_from_database() // 4 + 1):
            widget = QWidget()
            widget_layout = QHBoxLayout()
            for j in range(1,5):
                if self.current_index <= self.template_control_model.count_templates_from_database():
                    small_template_label = QLabel()
                    template_pixmap = QPixmap(self.template_control_model.get_template_from_database(self.current_index)['path'])
                    small_template_label.setPixmap(template_pixmap.scaled(100, 100, Qt.KeepAspectRatio))  # Kích thước nhỏ hơn
                    small_template_label.mousePressEvent = self.handle_mouse_press_event_small_template_label_in_menu()  # Thiết lập sự kiện click
                    small_template_label.mouseReleaseEvent = self.handle_mouse_release_event_small_template_label_in_menu(self.current_index)
                    widget_layout.addWidget(small_template_label)
                    self.small_template_labels.append(small_template_label)
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
                self.view.update_template_show_label(self.template_control_model.get_template_from_database(index)['path'])  # Kích thước lớn hơn
                self.selected_template_id = index
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