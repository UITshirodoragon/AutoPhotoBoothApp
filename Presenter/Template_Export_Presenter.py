from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QStackedWidget

from View.Template_Export_View import TemplateExportView

from Model.Template_Export_Model import TemplateExportModel
from Model.User_Model import UserModel, User
from Model.Template_Model import TemplateModel

from Presenter.Mediator import IMediator, ConcreteMediator

class TemplateExportPresenter:
    def __init__(self, model: TemplateExportModel, view: TemplateExportView, stack_view: QStackedWidget, user_control_model: UserModel, template_control_model: TemplateModel ) -> None:
        self.model = model
        self.view = view
        self.stack_view = stack_view
        self.user_control_model = user_control_model
        self.template_control_model = template_control_model
        self.mediator = None
        
        self.view.TEV_back_button_signal.connect(self.handle_back_button_clicked)
        self.view.TEV_restart_button_signal.connect(self.handle_restart_button_clicked)
        
    def set_mediator(self, mediator: IMediator) -> None:
        self.mediator = mediator    
    
    def handle_back_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(2)
        print(self.template_control_model.selected_template_id)
        
    def handle_restart_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(0)
        self.user_control_model.delete_user()
        self.user_control_model.disable_user()
        self.user_control_model.get_user().image_count = 0
    
    def handle_update_final_template_with_images(self) -> None:
        self.model.export_template_with_images(self.template_control_model.get_template_from_database(self.template_control_model.selected_template_id), self.user_control_model.get_user())
        self.view.update_final_template_with_images_gui(self.user_control_model.get_user().gallery_folder_path + '/final.png')