from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QStackedWidget

from View.Template_Export_View import TemplateExportView
from Model.Template_Export_Model import TemplateExportModel
from Model.User_Model import *

class TemplateExportPresenter:
    def __init__(self, model: TemplateExportModel, view: TemplateExportView, stack_view: QStackedWidget, user_control_model: UserModel ) -> None:
        self.model = model
        self.view = view
        self.stack_view = stack_view
        self.user_control_model = user_control_model
        
        self.view.TEV_back_button_signal.connect(self.handle_back_button_clicked)
        self.view.TEV_restart_button_signal.connect(self.handle_restart_button_clicked)
        
    def handle_back_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(2)
        
    def handle_restart_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(0)
        self.user_control_model.delete_user()
        self.user_control_model.disable_user()
        self.user_control_model.get_user().image_count = 0
        