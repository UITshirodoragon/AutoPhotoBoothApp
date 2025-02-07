from Template_Model import TemplateModel

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QListWidget, QLabel, QLineEdit, QHBoxLayout, QMessageBox, QGridLayout, QStackedLayout
from PyQt5.QtGui import QPixmap, QImage, QIntValidator
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTabWidget, QSlider, QFileDialog
from PIL import Image

class TemplateManagerTool(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.template_control_model = TemplateModel()
        
        self.selected_template_id: int= None
        self.folder_path = "Data/Template/"
        
        self.setWindowTitle("Template Manager Tool")
        self.setGeometry(100, 100, 1600, 800)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
    #     self.tab_widget = QTabWidget()
    #     self.layout = QVBoxLayout(self.central_widget)
    #     self.layout.addWidget(self.tab_widget)
        
    #     self.template_tab = QWidget()
    #     self.background_tab = QWidget()
        
    #     self.tab_widget.addTab(self.template_tab, "Template")
    #     self.tab_widget.addTab(self.background_tab, "Background")
        
    #     self.init_template_tab()
    #     self.init_background_tab()
        
    #     self.load_templates()
    
    # def init_template_tab(self):
        self.template_layout = QHBoxLayout(self.central_widget)
        self.template_layout.setContentsMargins(10, 10, 10, 10)
        
        self.list_layout = QVBoxLayout()
        self.template_layout.addLayout(self.list_layout)
        
        self.template_list = QListWidget()
        self.template_list.itemClicked.connect(self.display_template_details)
        self.list_layout.addWidget(self.template_list)
        
        
        
        self.template_display = QLabel()
        self.template_display.setAlignment(Qt.AlignCenter)
        self.template_display.setFixedSize(800, 800)
        
        self.background_image = QLabel(self.template_display)
        self.background_image.setAlignment(Qt.AlignCenter)
        self.background_image.setGeometry(0, 0, 800, 800)
        self.background_image.setFixedSize(800, 800)
        
        self.template_image = QLabel(self.template_display)
        self.template_image.setAlignment(Qt.AlignCenter)
        self.background_image.setGeometry(0, 0, 800, 800)
        self.template_image.setFixedSize(800, 800)
        
        self.template_layout.addWidget(self.template_display)
        
        self.tab_widget = QTabWidget()
        self.template_layout.addWidget(self.tab_widget)
        
        self.template_tab = QWidget()
        self.background_tab = QWidget()
        
        self.tab_widget.addTab(self.template_tab, "Template")
        self.tab_widget.addTab(self.background_tab, "Background")
        
        self.init_template_tab()
        self.init_background_tab()
        
        self.load_templates()
        
    def init_template_tab(self):
        
        self.template_info_layout = QGridLayout(self.template_tab)
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
        
        self.template_background_path_label = QLabel("Background:")
        self.template_background_path_edit = QLineEdit()
        self.template_info_layout.addWidget(self.template_background_path_label, 8, 0)
        self.template_info_layout.addWidget(self.template_background_path_edit, 8, 1)
        
        self.add_button = QPushButton("Add Template")
        self.add_button.clicked.connect(self.add_template)
        self.template_info_layout.addWidget(self.add_button, 9, 0, 1, 2)
        
        self.update_button = QPushButton("Update Template")
        self.update_button.clicked.connect(self.update_template)
        self.template_info_layout.addWidget(self.update_button, 10, 0, 1, 2)
        
        self.delete_button = QPushButton("Delete Template")
        self.delete_button.clicked.connect(self.delete_template)
        self.template_info_layout.addWidget(self.delete_button, 11, 0, 1, 2)
        
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_fields)
        self.template_info_layout.addWidget(self.clear_button, 12, 0, 1, 2)
        
        self.template_layout.addLayout(self.template_info_layout)
        
        
    
    def init_background_tab(self):
        self.background_layout = QGridLayout(self.background_tab)
        
        self.background_name_label = QLabel("Name:")
        self.background_name_edit = QLineEdit()
        self.background_layout.addWidget(self.background_name_label, 0, 0)
        self.background_layout.addWidget(self.background_name_edit, 0, 1, 1, 2)
        
        self.background_path_lable = QLabel("Path:")
        self.background_path_edit = QLineEdit()
        self.background_layout.addWidget(self.background_path_lable, 1, 0)
        self.background_layout.addWidget(self.background_path_edit, 1, 1, 1, 1)
        
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_background_file)
        self.background_layout.addWidget(self.browse_button, 1, 2)
         
        self.color_code_label = QLabel("Color Code:")
        self.color_code_edit = QLineEdit()
        self.color_code_edit.setPlaceholderText("#FFFFFF")
        self.color_code_edit.textChanged.connect(self.update_sliders_from_color_code)
        self.background_layout.addWidget(self.color_code_label, 2, 0)
        self.background_layout.addWidget(self.color_code_edit, 2, 1, 1, 2)
        
        
        self.rgba_sliders = {}
        self.rgba_values = {}
        for i, color in enumerate(['R', 'G', 'B', 'A']):
            label = QLabel(f"{color}:")
            slider = QSlider(Qt.Horizontal)
            slider.setRange(0, 255)
            slider.setValue(255)
            slider.valueChanged.connect(self.update_background_color)
            self.rgba_sliders[color] = slider
            
            value_edit = QLineEdit("255")
            value_edit.setFixedWidth(40)
            value_edit.setValidator(QIntValidator(0, 255))
            value_edit.textChanged.connect(lambda value, c=color: self.update_slider_from_edit(c, value))
            self.rgba_values[color] = value_edit
            
            self.background_layout.addWidget(label, 3 + i, 0)
            self.background_layout.addWidget(slider, 3 + i, 1)
            self.background_layout.addWidget(value_edit, 3 + i, 2)
        
        self.save_background_button = QPushButton("Save Background")
        self.save_background_button.clicked.connect(self.save_background)
        self.background_layout.addWidget(self.save_background_button, 7, 0, 1, 3)

        self.set_default_background_button = QPushButton("Set Default Background")
        self.set_default_background_button.clicked.connect(self.set_default_background)
        self.background_layout.addWidget(self.set_default_background_button, 8, 0, 1, 3)
        

        self.reset_button = QPushButton("Reset All")
        self.reset_button.clicked.connect(self.reset_all)
        self.background_layout.addWidget(self.reset_button, 9, 0, 1, 3)
    
    def set_default_background(self):
        self.save_background()
        self.template_control_model.update_template_in_database(id = self.selected_template_id, 
                                                                background_path = self.folder_path + self.background_name_edit.text() + ".png")
        self.load_templates()
     
    def reset_all(self):
        self.background_name_edit.clear()
        self.background_path_edit.clear()
        self.color_code_edit.setText("#FFFFFF")
        for color in ['R', 'G', 'B', 'A']:
            self.rgba_sliders[color].setValue(255)
            self.rgba_values[color].setText("255")
        self.background_image.clear()
    
    
    def browse_background_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Background File", "", "Images (*.png *.jpg *.bmp)")
        if file_name:
            self.background_path_edit.setText(file_name)
            self.background_name_edit.setText(file_name.split("/")[-1].split(".")[0])
            image = QPixmap(file_name).scaled(800, 800, Qt.KeepAspectRatio)
            self.background_image.setPixmap(image)
    
    def update_slider_from_edit(self, color, value):
        if value.isdigit():
            self.rgba_sliders[color].setValue(int(value))
    
    def update_sliders_from_color_code(self):
        color_code = self.color_code_edit.text()
        if not color_code.startswith("#") or len(color_code) != 7:
            return
        
        r = int(color_code[1:3], 16)
        g = int(color_code[3:5], 16)
        b = int(color_code[5:7], 16)
        
        self.rgba_sliders['R'].setValue(r)
        self.rgba_sliders['G'].setValue(g)
        self.rgba_sliders['B'].setValue(b)
        
        self.update_background_color()
    
    def update_background_color(self):
        r = self.rgba_sliders['R'].value()
        g = self.rgba_sliders['G'].value()
        b = self.rgba_sliders['B'].value()
        a = self.rgba_sliders['A'].value()
        
        self.color_code_edit.setText(f"#{r:02X}{g:02X}{b:02X}")
        
        for color, slider in self.rgba_sliders.items():
            self.rgba_values[color].setText(str(slider.value()))
        
        size = self.template_control_model.get_template_with_field_from_database(self.selected_template_id, "size")
        if size:
            image = Image.new("RGBA", size, (r, g, b, a))
            image = QImage(image.tobytes("raw", "RGBA"), image.width, image.height, QImage.Format_RGBA8888)
            image_qt = QPixmap.fromImage(image)
            self.background_image.setPixmap(image_qt.scaled(800, 800, Qt.KeepAspectRatio))
    
    def save_background(self):
        
        file_name = self.background_name_edit.text()
        file_path = self.background_path_edit.text()
        
        if not file_name or not file_path:
            QMessageBox.warning(self, "Warning", "No file provided")
            return
        
        if os.path.exists(self.folder_path + file_name + ".png") or os.path.exists(file_path):
            QMessageBox.warning(self, "Warning", "File already exists")
            return
        
        r = self.rgba_sliders['R'].value()
        g = self.rgba_sliders['G'].value()
        b = self.rgba_sliders['B'].value()
        a = self.rgba_sliders['A'].value()
        
        size = self.template_control_model.get_template_with_field_from_database(self.selected_template_id, "size")
        if size:
            image = Image.new("RGBA", size, (r, g, b, a))
            if file_name:
                image.save(self.folder_path + file_name + ".png")
            else:
                image.save(file_path)
    







    
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
        self.template_background_path_edit.clear()
        
    
    
    
    def display_template_details(self, item):
        self.selected_template_id = item.text().split(":")[0]
        template = self.template_control_model.get_template_from_database(self.selected_template_id)
        
        self.template_id_edit.setText(str(template['id']))
        
        self.template_path_edit.setText(template['path'])
        
        self.template_style_edit.setText(template['style'])
        
        self.template_number_of_images_edit.setText(str(template['number_of_images']))
        
        self.template_image_positions_edit.setText(str(template['image_positions_list']))
        
        self.template_size_edit.setText(str(template['size']))
        
        self.template_image_size_edit.setText(str(template['image_size']))
        
        self.template_image_ratio_edit.setText(str(template['image_ratio']))
        
        self.template_background_path_edit.setText(template['background_path'])
        
        self.background_name_edit.setText(template['background_path'].split("/")[-1].split(".")[0])
        
        self.background_path_edit.setText(template['background_path'])
        
        template_pixmap = QPixmap(template['path']).scaled(800, 800, Qt.KeepAspectRatio)
        self.template_image.setPixmap(template_pixmap)
        background_pixmap = QPixmap(template['background_path']).scaled(800, 800, Qt.KeepAspectRatio)
        self.background_image.setPixmap(background_pixmap)
    
    def add_template(self):    
        path = self.template_path_edit.text()
        style = self.template_style_edit.text()
        number_of_images = eval(self.template_number_of_images_edit.text())
        image_positions_list = eval(self.template_image_positions_edit.text())
        size = eval(self.template_size_edit.text())
        image_size = eval(self.template_image_size_edit.text())
        image_ratio = self.template_image_ratio_edit.text()
        background_path = self.template_background_path_edit.text()
        
        
        self.template_control_model.insert_template_into_database(path = path, 
                                                                  style = style,
                                                                  number_of_images = number_of_images,
                                                                  image_positions_list = image_positions_list,
                                                                  size = size,
                                                                  image_size = image_size,
                                                                  image_ratio = image_ratio,
                                                                    background_path = background_path
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
        background_path = self.template_background_path_edit.text()
        
        self.template_control_model.update_template_in_database(id = template_id,
                                                                path = path,
                                                                style = style,
                                                                number_of_images = number_of_images,
                                                                image_positions_list = image_positions_list,
                                                                size = size,
                                                                image_size = image_size,
                                                                image_ratio = image_ratio,
                                                                background_path = background_path
                                                                
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
        self.template_control_model.reset_template_ids_in_database()
        self.load_templates()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TemplateManagerTool()
    window.show()
    sys.exit(app.exec_())