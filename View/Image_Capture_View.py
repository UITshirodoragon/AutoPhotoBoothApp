from __future__ import annotations
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.uic import loadUi
from typing import Protocol
from cv2.typing import MatLike

from View.ui_Image_Capture_View import Ui_Image_Capture_View



class ImageCaptureView(QWidget, Ui_Image_Capture_View ):
    ICV_back_button_signal = pyqtSignal()
    ICV_next_button_signal = pyqtSignal()
    
    def __init__(self) -> None:
        super().__init__()
        # super(ImageCaptureView, self).__init__()
        # loadUi('View/Image_Capture_View.ui', self)
        # '''self.setWindowTitle("Camera App with MVP Architecture")

        # Thiết lập các thành phần GUI
        
        self.setupUi(self)
        # self.setWindowTitle("Image Capture View")
        # self.setGeometry(0,0,450,800)
        # self.setMinimumSize(450,800)
        # self.initUI()
        
        
        # def initUI(self) -> None:
        # self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.emit_back_button_clicked_signal)
        # self.back_button.setGeometry(25,25,50,50)
        
        # self.preview_image_label = QLabel(self)
        # self.preview_image_label.setGeometry(0,100,450,600)
        
        # self.preview_fps_label = QLabel(self)
        # self.preview_fps_label.setGeometry(25,700,50,50)
        
        # self.next_button = QPushButton("Next", self)
        # self.next_button.setGeometry(100,700,200,50)
        self.next_button.clicked.connect(self.emit_next_button_clicked_signal)

    #slot
    def emit_back_button_clicked_signal(self) -> None:
        self.ICV_back_button_signal.emit()
        
    def emit_next_button_clicked_signal(self) -> None:
        self.ICV_next_button_signal.emit() 

    def update_preview_image_gui(self, frame: MatLike) -> None:
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        # self.preview_reigion.setPixmap(QPixmap.fromImage(image))
        self.preview_image_label.setPixmap(QPixmap.fromImage(image).scaled(450,600))


    def update_preview_fps_gui(self, fps: float) -> None:
        # self.fps.setText(f"FPS: {fps}")
        self.preview_fps_label.setText(f"FPS: {fps}")
