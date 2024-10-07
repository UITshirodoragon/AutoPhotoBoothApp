from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QStackedWidget

from Model.Start_Model import StartModel
from Model.User_Model import *
from View.Start_View import StartView

# Presenter class
class StartPresenter:
    def __init__(self, model: StartModel, view: StartView, stack_view: QStackedWidget, user_control_model: UserModel):
        self.model = model
        self.view = view
        self.stack_view = stack_view
        self.user_control_model = user_control_model

        
        self.view.SV_start_button_signal.connect(self.handle_start_button_clicked)

    def handle_start_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(1)
        self.user_control_model.create_user()



    # def start_button_clicked(self):
    #     self.templates = self.model.get_templates()
    #     self.view.show_template_screen(self.templates)
        
    # def template_selected(self, index: int):
    #     selected_template = self.templates[index]
    #     print(f"Selected Template: {selected_template}")
    #     # Here, add logic to proceed with the selected template

    