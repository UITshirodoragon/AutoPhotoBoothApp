from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QStackedWidget

from View.Template_Export_View import TemplateExportView
from Model.Template_Export_Model import TemplateExportModel


class TemplateExportPresenter:
    def __init__(self, model: TemplateExportModel, view: TemplateExportView, stack_view: QStackedWidget) -> None:
        self.model = model
        self.view = view
        self.stack_view = stack_view
        
        self.view.TEV_back_button_signal.connect(self.handle_back_button_clicked)
        self.view.TEV_restart_button_signal.connect(self.handle_restart_button_clicked)
        
    def handle_back_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(2)
        
    def handle_restart_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(0)
        