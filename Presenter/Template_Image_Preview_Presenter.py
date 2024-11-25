from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QScrollArea, QLabel, QPushButton, QProgressBar
from PyQt5.QtCore import pyqtSignal, QThread, QTimer


from View.Template_Image_Preview_View import TemplateImagePreviewView
from View.Alert_Box_View import AlertBoxView

from Model.Template_Export_Model import TemplateExportModel, TemplateExportWorker
from Model.User_Model import UserModel, User
from Model.Template_Model import TemplateModel
from Model.Google_Drive_Model import GoogleDriveModel
from Model.Image_Model import ImageModel

from Presenter.Mediator import IMediator, ConcreteMediator

class TemplateImagePreviewPresenter:
    def __init__(self, model: TemplateExportModel,
                    view: TemplateImagePreviewView,
                    stack_view: QStackedWidget,
                    user_control_model: UserModel,
                    template_control_model: TemplateModel,
                    image_control_model: ImageModel
                    ) -> None:
            self.model = model
            self.view = view
            self.stack_view = stack_view
            self.user_control_model = user_control_model
            self.template_control_model = template_control_model
            self.image_control_model = image_control_model
            self.mediator = None
            
            self.currun_image_id = None
            
            self.time_left = 3
            self.countdown_time = self.time_left
            
            self.view.TIPV_export_template_button_clicked_signal.connect(self.handle_export_template_button_clicked)
            self.view.TIPV_restart_capture_button_clicked_signal.connect(self.handle_restart_capture_button_clicked)
            self.view.TIPV_confirm_capture_button_clicked_signal.connect(self.handle_confirm_capture_button_clicked)
            
            self.view.export_template_button.hide()
            
            
    def handle_start_countdown(self):
        self.view.show_preview_countdown_label_gui()
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.handle_update_countdown)
        self.countdown_timer.start(1000)

    def handle_update_countdown(self):
        if self.time_left > 0:
            self.view.update_preview_countdown_label_gui(f"Continue in {self.time_left}s")
            self.time_left -= 1
        else:
            self.countdown_timer.stop()
            self.time_left = self.countdown_time
            
            self.mediator.notify(sender = 'template_image_preview_presenter', receiver = 'image_capture_presenter', event = 'start_capture_countdown')  
            
            self.view.hide_preview_countdown_label_gui()
            
            
            if self.user_control_model.get_user().image_count < self.template_control_model.get_template_with_field_from_database(self.template_control_model.selected_template_id, "number_of_images"):
                self.stack_view.setCurrentIndex(2)
            else:
                self.stack_view.setCurrentIndex(2)
            # updating
            # self.handle_capture_button_clicked()
            # self.view.capture_button.setEnabled(True)  # Enable the button
    
            
    def set_mediator(self, mediator: IMediator) -> None:
        self.mediator = mediator
        
    def handle_export_template_button_clicked(self) -> None:
        pass
    
    def handle_restart_capture_button_clicked(self) -> None:
        if self.view.show_dialog_alert_to_restart_capture():
            self.mediator.notify(sender = 'template_image_preview_presenter', receiver = 'image_capture_presenter', event = 'restart_capture_image', data = {'deleted_image_id': self.currun_image_id})
            self.stack_view.setCurrentIndex(2)
        
    def handle_confirm_capture_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(2)
        
    def handle_update_raw_image(self, selected_image_id: int) -> None:
        self.view.update_raw_image_gui(self.image_control_model.get_image_with_field_from_database(selected_image_id, "path"))
        
    def handle_update_template_with_a_image(self, selected_image_id: int) -> None:
        self.view.update_preview_template_gui(self.image_control_model.get_image_with_field_from_database(selected_image_id, "template_with_image_path"))
        self.view.update_raw_image_gui(self.image_control_model.get_image_with_field_from_database(selected_image_id, "path"))
        self.view.update_image_info_label_gui(f"Image #{selected_image_id}")
        self.currun_image_id = selected_image_id