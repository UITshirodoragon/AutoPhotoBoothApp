from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap

from View.ui_Template_Menu_View import Ui_TemplateMenuView


class TemplateMenuView(QWidget, Ui_TemplateMenuView):
    TMV_back_button_signal = pyqtSignal()
    TMV_confirm_button_signal = pyqtSignal()
    
    def __init__(self) -> None:
        super().__init__()
        self.current_index = 0
        self.labels = []
        self.template_path_list = []
        for i in range(1, 9):
            self.template_path_list.append(f"Data/Template/template{i}.png")
        
        self.setupUi(self)
        print(self.template_widget_stack.count())
        
        for i in range(len(self.template_path_list) // 4 + 1):
            widget = QWidget()
            widget_layout = QHBoxLayout()
            for j in range(4):
                if self.current_index < len(self.template_path_list):
                    label = QLabel()
                    pixmap = QPixmap(self.template_path_list[self.current_index])
                    label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))  # Kích thước nhỏ hơn
                    label.mousePressEvent = self.create_click_handler(self.current_index)  # Thiết lập sự kiện click
                    widget_layout.addWidget(label)
                    self.labels.append(label)
                    self.current_index += 1
            widget.setLayout(widget_layout)
            self.template_widget_stack.addWidget(widget)
        
        
        
        
        # self.setWindowTitle("Template menu view")
        # self.setGeometry(0,0,450,800)
        # self.setMinimumSize(450,800)
        # self.initUI()
        
        # def initUI(self) -> None:
        # self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.emit_back_button_clicked_signal)
        # self.back_button.setGeometry(25,25,50,50)
        
        
        # self.template_text_label = QLabel("Choose your template", self)
        # self.template_text_label.setGeometry(100,25,200,50)
        
        
        # self.template_show_label = QLabel("Template show", self)
        # self.template_show_label.setGeometry(25,100,400,300)
        template_pixmap = QPixmap("Data/Template/template1.png")
        scaled_template_pixmap = template_pixmap.scaled(400,300)
        self.template_show_label.setPixmap(scaled_template_pixmap)
        
        
        # self.confirm_button = QPushButton("Confirm", self)
        # self.confirm_button.setGeometry(0,700,450,50)
        self.confirm_button.clicked.connect(self.emit_confirm_button_clicked_signal)
        
    def create_click_handler(self, index):
        def handler(event):
            pixmap = QPixmap(self.template_path_list[index])
            self.template_show_label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))  # Kích thước lớn hơn
        return handler
    
    # def show_previous(self):
    #     if self.template_widget_stack.currentIndex() > 0:
    #         self.template_widget_stack.setCurrentIndex(self.template_widget_stack.currentIndex() - 1)

    # def show_next(self):
    #     if self.template_widget_stack.currentIndex() < self.template_widget_stack.count() - 1:
    #         self.template_widget_stack.setCurrentIndex(self.template_widget_stack.currentIndex() + 1)
    
    def mousePressEvent(self, event):
        """Capture the start position of the swipe"""
        self.start_pos = event.pos()

    def mouseReleaseEvent(self, event):
        """Handle the swipe detection and animate the label update"""
        if self.start_pos:
            end_pos = event.pos()
            delta_x = end_pos.x() - self.start_pos.x()

            if delta_x < -50:  # Swipe left
                self.update_labels('left')
            elif delta_x > 50:  # Swipe right
                self.update_labels('right')

        self.start_pos = None
    
    def update_labels(self, direction):
        """Update the visible labels based on the swipe direction"""
        if direction == 'left' and self.template_widget_stack.currentIndex() > 0:
            self.template_widget_stack.setCurrentIndex(self.template_widget_stack.currentIndex() - 1)
        elif direction == 'right' and self.template_widget_stack.currentIndex() < self.template_widget_stack.count() - 1:
            self.template_widget_stack.setCurrentIndex(self.template_widget_stack.currentIndex() + 1)
    
    #slot
    def emit_back_button_clicked_signal(self) -> None:
        self.TMV_back_button_signal.emit()
        
    def emit_confirm_button_clicked_signal(self) -> None:
        self.TMV_confirm_button_signal.emit()