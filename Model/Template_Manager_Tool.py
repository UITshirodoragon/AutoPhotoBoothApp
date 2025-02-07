from Template_Model import TemplateModel

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QListWidget, QLabel, QLineEdit, QHBoxLayout, QMessageBox, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class TemplateManagerTool(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.template_control_model = TemplateModel()
        
        
        
        self.setWindowTitle("Template Manager Tool")
        self.setGeometry(100, 100, 1600, 800)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QHBoxLayout(self.central_widget)
        self.layout.setContentsMargins(10, 10, 10, 10)
        
        self.list_layout = QVBoxLayout()
        self.layout.addLayout(self.list_layout)
        
        
        self.template_list = QListWidget()
        self.template_list.itemClicked.connect(self.display_template_details)
        self.list_layout.addWidget(self.template_list)
        
        self.template_image = QLabel()
        self.template_image.setAlignment(Qt.AlignCenter)
        self.template_image.setFixedSize(800, 800)
        self.layout.addWidget(self.template_image)
        
        self.template_info_layout = QGridLayout()
        self.template_info_layout.setVerticalSpacing(5)
        
        self.template_id_label = QLabel("ID:")
        self.template_id_edit = QLineEdit()
        self.template_id_edit.setReadOnly(True)
        self.template_info_layout.addWidget(self.template_id_label, 0, 0)
        self.template_info_layout.addWidget(self.template_id_edit, 0, 1)
        
        self.template_path_label = QLabel("Path:")
        self.template_path_edit = QLineEdit()
        self.template_info_layout.addWidget(self.template_path_label, 1, 0)
        self.template_info_layout.addWidget(self.template_path_edit, 1, 1)
        
        self.template_style_label = QLabel("Style:")
        self.template_style_edit = QLineEdit()
        self.template_info_layout.addWidget(self.template_style_label, 2, 0)
        self.template_info_layout.addWidget(self.template_style_edit, 2, 1)
        
        self.template_number_of_images_label = QLabel("Number of Images:")
        self.template_number_of_images_edit = QLineEdit()
        self.template_info_layout.addWidget(self.template_number_of_images_label, 3, 0)
        self.template_info_layout.addWidget(self.template_number_of_images_edit, 3, 1)
        
        self.template_image_positions_label = QLabel("Image Positions List:")
        self.template_image_positions_edit = QLineEdit()
        self.template_info_layout.addWidget(self.template_image_positions_label, 4, 0)
        self.template_info_layout.addWidget(self.template_image_positions_edit, 4, 1)
        
        self.template_size_label = QLabel("Size:")
        self.template_size_edit = QLineEdit()
        self.template_info_layout.addWidget(self.template_size_label, 5, 0)
        self.template_info_layout.addWidget(self.template_size_edit, 5, 1)
        
        self.template_image_size_label = QLabel("Image Size:")
        self.template_image_size_edit = QLineEdit()
        self.template_info_layout.addWidget(self.template_image_size_label, 6, 0)
        self.template_info_layout.addWidget(self.template_image_size_edit, 6, 1)
        
        self.template_image_ratio_label = QLabel("Image Ratio:")
        self.template_image_ratio_edit = QLineEdit()
        self.template_info_layout.addWidget(self.template_image_ratio_label, 7, 0)
        self.template_info_layout.addWidget(self.template_image_ratio_edit, 7, 1)
        
        
        self.layout.addLayout(self.template_info_layout)
        
        
        
        self.button_layout = QHBoxLayout()
        
        self.add_button = QPushButton("Add Template")
        self.add_button.clicked.connect(self.add_template)
        self.list_layout.addWidget(self.add_button)
        
        self.update_button = QPushButton("Update Template")
        self.update_button.clicked.connect(self.update_template)
        self.list_layout.addWidget(self.update_button)
        
        self.delete_button = QPushButton("Delete Template")
        self.delete_button.clicked.connect(self.delete_template)
        self.list_layout.addWidget(self.delete_button)
        
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_fields)
        self.list_layout.addWidget(self.clear_button)
        
        
        self.load_templates()
    
    def load_templates(self):
        self.template_list.clear()
        templates = self.template_control_model.get_all_templates_from_database()
        for template in templates:
            self.template_list.addItem(f"{template['id']}: {template['style']}")
        
    def clear_fields(self):
        self.template_image.clear()
        self.template_id_edit.clear()
        self.template_path_edit.clear()
        self.template_style_edit.clear()
        self.template_number_of_images_edit.clear()
        self.template_image_positions_edit.clear()
        self.template_size_edit.clear()
        self.template_image_size_edit.clear()
        self.template_image_ratio_edit.clear()
        
    
    
    
    def display_template_details(self, item):
        template_id = item.text().split(":")[0]
        template = self.template_control_model.get_template_from_database(template_id)
        
        self.template_id_edit.setText(str(template['id']))
        
        self.template_path_edit.setText(template['path'])
        
        self.template_style_edit.setText(template['style'])
        
        self.template_number_of_images_edit.setText(str(template['number_of_images']))
        
        self.template_image_positions_edit.setText(str(template['image_positions_list']))
        
        self.template_size_edit.setText(str(template['size']))
        
        self.template_image_size_edit.setText(str(template['image_size']))
        
        self.template_image_ratio_edit.setText(str(template['image_ratio']))
        
        pixmap = QPixmap(template['path']).scaled(800, 800, Qt.KeepAspectRatio)
        self.template_image.setPixmap(pixmap)
    
    def add_template(self):    
        path = self.template_path_edit.text()
        style = self.template_style_edit.text()
        number_of_images = eval(self.template_number_of_images_edit.text())
        image_positions_list = eval(self.template_image_positions_edit.text())
        size = eval(self.template_size_edit.text())
        image_size = eval(self.template_image_size_edit.text())
        image_ratio = self.template_image_ratio_edit.text()
        
        
        self.template_control_model.insert_template_into_database(path = path, 
                                                                  style = style,
                                                                  number_of_images = number_of_images,
                                                                  image_positions_list = image_positions_list,
                                                                  size = size,
                                                                  image_size = image_size,
                                                                  image_ratio = image_ratio
                                                                  )
        
        self.load_templates()
    
    def update_template(self):
        current_item = self.template_list.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Warning", "No template selected")
            return
        
        template_id = current_item.text().split(":")[0]
        old_path = self.template_control_model.get_template_from_database(template_id)['path']
        path = self.template_path_edit.text()
        style = self.template_style_edit.text()
        number_of_images = eval(self.template_number_of_images_edit.text())
        image_positions_list = eval(self.template_image_positions_edit.text())
        size = eval(self.template_size_edit.text())
        image_size = eval(self.template_image_size_edit.text())
        image_ratio = self.template_image_ratio_edit.text()
        
        self.template_control_model.update_template_in_database(id = template_id,
                                                                path = path,
                                                                style = style,
                                                                number_of_images = number_of_images,
                                                                image_positions_list = image_positions_list,
                                                                size = size,
                                                                image_size = image_size,
                                                                image_ratio = image_ratio
                                                                
                                                                ) # more
        
        if path != old_path:
            try:
                os.rename(old_path, path)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to rename file: {e}")
                return
            
        
        
        self.load_templates()
    
    def delete_template(self):
        
        current_item = self.template_list.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Warning", "No template selected")
            return
        
        template_id = current_item.text().split(":")[0]
        
        self.template_control_model.delete_template_from_database(template_id)
        
        self.load_templates()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TemplateManagerTool()
    window.show()
    sys.exit(app.exec_())