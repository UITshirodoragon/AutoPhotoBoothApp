from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QScrollArea, QLabel, QPushButton, QProgressBar
from PyQt5.QtCore import pyqtSignal, QThread


from View.Template_Image_Preview_View import TemplateImagePreviewView

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
            
            
            self.view.TIPV_export_template_button_clicked_signal.connect(self.handle_export_template_button_clicked)
            self.view.TIPV_restart_capture_button_clicked_signal.connect(self.handle_restart_capture_button_clicked)
            self.view.TIPV_confirm_capture_button_clicked_signal.connect(self.handle_confirm_capture_button_clicked)
            
            
            
    def set_mediator(self, mediator: IMediator) -> None:
        self.mediator = mediator
        
    def handle_export_template_button_clicked(self) -> None:
        pass
    
    def handle_restart_capture_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(2)
        
    def handle_confirm_capture_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(2)
        
    def handle_update_raw_image(self, selected_image_id: int) -> None:
        self.view.update_raw_image_gui(self.image_control_model.get_image_with_field_from_database(selected_image_id, "path"))
        
    def handle_update_template_with_a_image(self, selected_image_id: int) -> None:
        self.view.update_preview_template_gui(self.image_control_model.get_image_with_field_from_database(selected_image_id, "template_with_image_path"))