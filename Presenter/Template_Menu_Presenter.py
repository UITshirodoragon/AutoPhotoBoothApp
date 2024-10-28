from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap

from View.Template_Menu_View import TemplateMenuView

from Presenter.Mediator import IMediator, ConcreteMediator



from Model.Template_Menu_Model import TemplateMenuModel
from Model.User_Model import UserModel, User
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
        self.mediator = None
        
        self.current_index = 1
        self.small_template_labels = []
        self.start_pos = None
        self.selected_template_id = 1
        self.touch_event: str = "Touch"

        
        self.number_of_templates = self.template_control_model.count_templates_from_database()
        
        self.view.TMV_back_button_signal.connect(self.handle_back_button_clicked)
        self.view.TMV_confirm_button_signal.connect(self.handle_confirm_button_clicked)
        
        self.handle_template_menu_label()
        # self.view.TMV_touch_event_signal.connect(self.handle_update_small_template_labels_in_menu)
        
    def set_mediator(self, mediator: IMediator) -> None:
        self.mediator = mediator    
        
    def handle_back_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(0)
        
        
    def handle_confirm_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(2)
        # confirm final
        self.template_control_model.selected_template_id = self.selected_template_id
        

    def handle_template_menu_label(self):
        self.view.template_menu_container_widget.setGeometry(0, 0, self.number_of_templates * 250, 250)
        self.view.template_menu_frame.mousePressEvent = self.handle_mouse_press_event_small_template_label_in_menu_frame()
        self.view.template_menu_frame.mouseMoveEvent = self.handle_mouse_move_event_small_template_label_in_menu_frame()
        # self.view.template_menu_frame.mouseReleaseEvent = self.handle_mouse_release_event_small_template_label_in_menu_frame()   
        container_layout = QHBoxLayout()
        for i in range(1, self.number_of_templates + 1):
            small_template_label = QLabel()
            small_template_label.setMinimumSize(200, 200)
            small_template_label.setMaximumSize(250, 250)
            template_pixmap = QPixmap(self.template_control_model.get_template_with_field_from_database(i, 'path'))
            small_template_label.setPixmap(template_pixmap.scaled(200, 200, Qt.KeepAspectRatio))
            # small_template_label.mousePressEvent = self.handle_mouse_press_event_small_template_label_in_menu()  # Thiết lập sự kiện click
            small_template_label.mouseReleaseEvent = self.handle_mouse_release_event_small_template_label_in_menu(self.current_index)
            # small_template_label.mouseMoveEvent = self.handle_mouse_move_event_small_template_label_in_menu()
            container_layout.addWidget(small_template_label)
            self.small_template_labels.append(small_template_label)
            self.current_index += 1
        self.view.template_menu_container_widget.setLayout(container_layout)
        
        
        
    
    # overide mouse event method for small template in menu for template menu frame
    def handle_mouse_press_event_small_template_label_in_menu_frame(self):
        def handler(event):
            if event.button() == Qt.LeftButton:
                self.start_pos = event.pos()
        return handler
    
    def handle_mouse_move_event_small_template_label_in_menu_frame(self):
        def handler(event):
            if self.start_pos:
                delta = event.pos() - self.start_pos
                new_x = self.view.template_menu_container_widget.x() + delta.x()
                if self.view.template_menu_container_widget.width() >= 1030:
                    new_x = max(min(new_x, 0), (1030 - self.view.template_menu_container_widget.width()))  # Ensure new_x is between -600 and 0
                else:
                    new_x = 0
                self.view.template_menu_container_widget.move(new_x, self.view.template_menu_container_widget.y())
                self.start_pos = event.pos()  
                if delta.x() > 5:
                    self.touch_event = "Swipe right"
                elif delta.x() < -5:
                    self.touch_event = "Swipe left"
            
        return handler
    
    def handle_mouse_release_event_small_template_label_in_menu_frame(self):
        def handler(event):
            pass
        return handler
    
    
    # overide mouse event method for small template in menu for template menu label
    def handle_mouse_press_event_small_template_label_in_menu(self):
        def handler(event):
            pass
            
            
        return handler
    
    def handle_mouse_move_event_small_template_label_in_menu(self):
        def handler(event):
            pass
        return handler
    
    
    def handle_mouse_release_event_small_template_label_in_menu(self, index):
        
        def handler(event):
            if event.button() == Qt.LeftButton:
                if self.touch_event == "Touch":
                    
                    for label in self.small_template_labels:
                        if label.geometry().contains(self.view.template_menu_container_widget.mapFromParent(event.pos())):
                            self.view.update_template_show_label(self.template_control_model.get_template_with_field_from_database(index, 'path'))  # Kích thước lớn hơn
                            self.selected_template_id = index
                            break
                    # self.view.TMV_touch_event_signal.emit("Touch")
                elif self.touch_event == "Swipe right":
                    pass
                    # self.view.TMV_touch_event_signal.emit("Swipe right")
                elif self.touch_event == "Swipe left":
                    pass
                    # self.view.TMV_touch_event_signal.emit("Swipe left")
                print(self.touch_event)
            self.touch_event = "Touch"
        return handler
