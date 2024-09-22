from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QStackedWidget

from View.Template_Menu_View import TemplateMenuView
from Model.Template_Menu_Model import TemplateMenuModel


class TemplateMenuPresenter:
    def __init__(self, model: TemplateMenuModel, view: TemplateMenuView, stack_view: QStackedWidget) -> None:
        self.model = model
        self.view = view
        self.stack_view = stack_view
        
        self.view.TMV_back_button_signal.connect(self.handle_back_button_clicked)
        self.view.TMV_confirm_button_signal.connect(self.handle_confirm_button_clicked)
        
    def handle_back_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(0)
        
    def handle_confirm_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(2)
        