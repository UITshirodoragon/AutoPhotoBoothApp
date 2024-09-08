from __future__ import annotations
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.uic import loadUi
from typing import Protocol
from cv2.typing import MatLike


class ImageCapturePresenter(Protocol):
    def handle_update_image(self) -> None:
        ...
    
    def handle_update_fps(self) -> None:
        ...


class ImageCaptureView(QWidget):
    def __init__(self) -> None:
        #super().__init__()
        super(ImageCaptureView, self).__init__()
        loadUi('Image_Capture_View.ui', self)
        '''self.setWindowTitle("Camera App with MVP Architecture")

        # Thiết lập các thành phần GUI
        self.image_1_label = QLabel(self)
        self.fps_1_label = QLabel(self)
        
        self.image_2_label = QLabel(self)
        self.fps_2_label = QLabel(self)
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_1_label)
        layout.addWidget(self.image_2_label)
        layout.addWidget(self.fps_1_label)
        layout.addWidget(self.fps_2_label)
        self.setLayout(layout)'''

    def update_image_gui(self, frame: MatLike) -> None:
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.preview_reigion.setPixmap(QPixmap.fromImage(image))
        #self.image_2_label.setPixmap(QPixmap.fromImage(image))


        
    def update_fps_gui(self, fps: float) -> None:
        self.fps.setText(f"FPS: {fps}")
        #self.fps_2_label.setText(f"FPS: {fps}")
