from __future__ import annotations
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QMainWindow, QPushButton, QHBoxLayout, QSizePolicy, QFrame, QGraphicsOpacityEffect
from PyQt5.QtCore import pyqtSignal, Qt, QSize, QRect, QPropertyAnimation, QTimer, QSequentialAnimationGroup
from PyQt5.QtGui import QPixmap, QImage, QIcon, QPalette
from PyQt5.uic import loadUi
from typing import Protocol
from cv2.typing import MatLike

from View.ui_Image_Capture_View import Ui_Image_Capture_View



class ImageCaptureView(QWidget, Ui_Image_Capture_View ):
    ICV_back_button_signal = pyqtSignal()
    ICV_next_button_signal = pyqtSignal()
    ICV_capture_button_signal = pyqtSignal()
    
    def __init__(self) -> None:
        super().__init__()
        
        self.setupUi(self)
        
        self.image_gallery_container_widget = QWidget(self.image_gallery_frame)       
        self.image_gallery_container_widget.setGeometry(0, 0, 30, 200)
        self.image_gallery_container_layout = QHBoxLayout()
        self.image_gallery_container_widget.setLayout(self.image_gallery_container_layout)
       
        self.back_button.clicked.connect(self.emit_back_button_clicked_signal)
        self.next_button.clicked.connect(self.emit_next_button_clicked_signal)
        self.capture_button.clicked.connect(self.emit_capture_button_clicked_signal)

    #slot
    def emit_back_button_clicked_signal(self) -> None:
        self.ICV_back_button_signal.emit()
        
    def emit_next_button_clicked_signal(self) -> None:
        self.ICV_next_button_signal.emit() 
        
    def emit_capture_button_clicked_signal(self) -> None:
        self.ICV_capture_button_signal.emit() 
        

    def update_preview_image_gui(self, frame: MatLike) -> None:
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        # self.preview_reigion.setPixmap(QPixmap.fromImage(image))
        self.preview_image_label.setPixmap(QPixmap.fromImage(image).scaled(1080,1440, Qt.KeepAspectRatio))


    def update_preview_fps_gui(self, fps: float) -> None:
        # self.fps.setText(f"FPS: {fps}")
        self.preview_fps_label.setText(f"FPS: {fps}")
        
    def update_number_of_captured_images_gui(self, number_of_captured_images: int, number_of_images_in_template: int) -> None:
        if(number_of_images_in_template != 0):
            if(number_of_captured_images == number_of_images_in_template):
                self.number_of_captured_images_label.setStyleSheet("color: green")
            else:
                self.number_of_captured_images_label.setStyleSheet("color: red")
            self.number_of_captured_images_label.setText(f"{number_of_captured_images}/{number_of_images_in_template}")
        else:
            self.number_of_captured_images_label.setStyleSheet("color: red")
            self.number_of_captured_images_label.setText("NA/NA")
            
    def update_countdown_number_label_gui(self, countdown_number_icon_path: str) -> None:
        self.countdown_number_label.setPixmap(QPixmap(countdown_number_icon_path).scaled(360,360, Qt.KeepAspectRatio))
        
    def animate_countdown_number_label_gui(self):
        
        # # Animate the size
        # self.size_animation = QPropertyAnimation(self.label, b"geometry")
        # self.size_animation.setDuration(1000)
        # self.size_animation.setStartValue(QRect(self.label.x(), self.label.y(), self.label.width(), self.label.height()))
        # self.size_animation.setEndValue(QRect(self.label.x() - 50, self.label.y() - 50, self.label.width() + 100, self.label.height() + 100))
        
        # Animate the opacity
        self.opacity_effect = QGraphicsOpacityEffect(self.countdown_number_label)
        self.countdown_number_label.setGraphicsEffect(self.opacity_effect)
        self.opacity_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.opacity_animation.setDuration(1000)
        self.opacity_animation.setStartValue(0.0)
        self.opacity_animation.setEndValue(1.0)
        
        # # Group animations
        self.animation_group = QSequentialAnimationGroup()
        # self.animation_group.addAnimation(self.size_animation)
        self.animation_group.addAnimation(self.opacity_animation)
        
        # # Start animations
        self.animation_group.start()
    
    def clear_countdown_number_label_gui(self):
        self.countdown_number_label.clear()
        self.capture_button.setEnabled(True)