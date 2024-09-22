from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap

# View class
class StartView(QWidget):
    # SV mean StartView
    SV_start_button_signal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Start View")
        self.setGeometry(0,0,450,800)
        self.setMinimumSize(450,800)
        self.initUI()

    def initUI(self):
        self.start_button = QPushButton("Tap to start", self)
        self.start_button.clicked.connect(self.emit_start_button_clicked_signal)
        self.start_button.setGeometry(0,100,450,600)
        

    # slots
    def emit_start_button_clicked_signal(self) -> None:
        self.SV_start_button_signal.emit()


    # def show_template_screen(self, templates: list):
    #     # Kiểm tra xem đã có layout chưa
    #     old_layout = self.layout()
    #     if old_layout is not None:
    #         # Xóa tất cả các widget con trong layout cũ
    #         while old_layout.count():
    #             item = old_layout.takeAt(0)
    #             widget = item.widget()
    #             if widget is not None:
    #                 widget.deleteLater()
    #         # Gỡ bỏ layout cũ
    #         QWidget().setLayout(old_layout)  # Phá layout cũ bằng cách gán nó vào một widget tạm

    #     # Tạo layout mới
    #     self.template_label = QLabel("CHOOSE YOUR TEMPLATE", self)
    #     self.template_list = QListWidget(self)
    #     self.template_list.setGeometry(0,700,200,400)

    #     # Thêm QLabel để hiển thị ảnh lớn
    #     self.large_image_label = QLabel(self)
    #     self.large_image_label.setGeometry(0,0,500,500)
    #     self.large_image_label.setScaledContents(True)
    #     # self.large_image_label.setStyleSheet("border: 1px solid black;")  # Đặt border cho QLabel để dễ thấy


    #     for index, template in enumerate(templates):
    #         # Tạo QListWidgetItem cho mỗi template
    #         item = QListWidgetItem()
    #         item.setIcon(QIcon(template))  # Gán hình ảnh template bằng QIcon
    #         item.setText(f"Template {index + 1}")  # Thêm mô tả hoặc số thứ tự cho template
    #         item.setData(Qt.UserRole, template)  # Lưu đường dẫn hình ảnh vào UserRole
    #         self.template_list.addItem(item)

    #     self.template_list.currentRowChanged.connect(self.on_template_selected)
        
    #     confirm_button = QPushButton("CONFIRM", self)
    #     confirm_button.clicked.connect(self.on_confirm_button_clicked)

    #     layout = QGridLayout()
        
    #     layout.addWidget(self.template_label, 0, 0)
    #     layout.addWidget(self.large_image_label, 1, 0)
    #     layout.addWidget(self.template_list, 2, 0)
    #     layout.addWidget(confirm_button,3, 0)

    #     self.setLayout(layout)  # Gán layout mới


    # def on_template_selected(self, index: int):
    # # Lấy item đã chọn
    #     item = self.template_list.item(index)
    #     if item:
    #         # Lấy đường dẫn hình ảnh từ item
    #         selected_template_path = item.data(Qt.UserRole)
    #         # Tạo QPixmap và load ảnh từ đường dẫn
    #         pixmap = QPixmap(selected_template_path)
            
    #         pixmap.scaled(400, 300)
    #         self.large_image_label.setPixmap(pixmap)
    #         self.large_image_label.setGeometry(0,100,500,500)
    #         self.large_image_label.setScaledContents(True)
                

    #     self.template_signal.emit(index)
        

    # def on_confirm_button_clicked(self):
    #     selected_template_index = self.template_list.currentRow()
    #     self.template_signal.emit(selected_template_index)
