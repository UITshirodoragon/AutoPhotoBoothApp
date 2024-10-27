from __future__ import annotations
from typing import Protocol

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap

from View.ui_Start_View import Ui_Start_View

# View class
class StartView(QWidget, Ui_Start_View):
    # SV mean StartView
    SV_start_button_signal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.start_button.clicked.connect(self.emit_start_button_clicked_signal)    

    # slots
    def emit_start_button_clicked_signal(self) -> None:
        self.SV_start_button_signal.emit()

