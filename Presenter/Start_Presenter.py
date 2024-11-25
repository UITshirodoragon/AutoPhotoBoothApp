from __future__ import annotations
from typing import Protocol

import sys
import os

from PyQt5.QtWidgets import QStackedWidget, QApplication


from Model.Start_Model import StartModel
from Model.Google_Drive_Model import GoogleDriveModel
from Model.User_Model import UserModel, User
from Model.Image_Model import ImageModel


from View.Start_View import StartView

from Presenter.Mediator import IMediator

# Presenter class
class StartPresenter:
    def __init__(self, model: StartModel, 
                 view: StartView, 
                 stack_view: QStackedWidget, 
                 user_control_model: UserModel,
                 google_drive_model: GoogleDriveModel,
                 app: QApplication,
                 image_control_model: ImageModel
                 ) -> None:
        self.model = model
        self.view = view
        self.stack_view = stack_view
        self.user_control_model = user_control_model
        self.google_drive_model = google_drive_model
        self.image_control_model = image_control_model
        self.app = app
        self.mediator = None

        self.view.SV_quit_button_signal.connect(self.handle_quit_button_clicked)
        self.view.SV_start_button_signal.connect(self.handle_start_button_clicked)

    def set_mediator(self, mediator: IMediator) -> None:
        self.mediator = mediator

    def handle_start_button_clicked(self) -> None:
        self.mediator.notify('start_presenter', 'image_capture_presenter', 'start_preview_process')
        self.stack_view.setCurrentIndex(1)
        self.user_control_model.create_user()
        
        self.image_control_model.set_image_database_path(self.user_control_model.get_user().image_database_path)
        self.image_control_model.create_table_in_database()

    def handle_quit_button_clicked(self) -> None:
        self.mediator.notify('start_presenter', 'image_capture_presenter', 'stop_preview_process')
        self.google_drive_model.Delete('cloud_drive_folder')
        self.view.close()
        self.app.quit()
        os._exit(0)

    # def start_button_clicked(self):
    #     self.templates = self.model.get_templates()
    #     self.view.show_template_screen(self.templates)
        
    # def template_selected(self, index: int):
    #     selected_template = self.templates[index]
    #     print(f"Selected Template: {selected_template}")
    #     # Here, add logic to proceed with the selected template

    