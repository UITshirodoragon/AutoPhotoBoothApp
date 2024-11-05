from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QScrollArea, QLabel, QPushButton, QProgressBar
from PyQt5.QtCore import pyqtSignal, QThread


from View.Template_Export_View import TemplateExportView

from Model.Template_Export_Model import TemplateExportModel, TemplateExportWorker
from Model.User_Model import UserModel, User
from Model.Template_Model import TemplateModel
from Model.Google_Drive_Model import GoogleDriveModel

from Presenter.Mediator import IMediator, ConcreteMediator

class TemplateImagePreviewPresenter:
    def __init__(self, model: TemplateExportModel,
                    view: TemplateExportView,
                    stack_view: QStackedWidget,
                    user_control_model: UserModel,
                    template_control_model: TemplateModel
                    ) -> None:
            self.model = model
            self.view = view
            self.stack_view = stack_view
            self.user_control_model = user_control_model
            self.template_control_model = template_control_model
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
        
    