from __future__ import annotations
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage
from Model.Image_Processing_Model import ImageProcessingModel
from View.Image_Capture_View import ImageCaptureView
from typing import Protocol
from cv2.typing import MatLike


class ImageCaptureView(Protocol):
    def update_image_gui(self, frame: MatLike) -> None:
        ...
        
    def update_fps_gui(self, fps: float) -> None:
        ...
    
class ImageProcessingModel(Protocol):
    def start_preview_process(self) -> None:
        ...
        
    def stop_preview_process(self) -> None:
        ...
        
    def get_frame(self) -> MatLike:
        ...
        
    def get_fps(self) -> float:
        ... 


class ImageCapturePresenter:
    def __init__(self, view: ImageCaptureView, 
                 model: ImageProcessingModel
                 ) -> None:
        self.view = view
        self.model = model
        
        # Khởi động camera trong model
        self.model.start_preview_process()
        
        # Thiết lập QTimer để cập nhật frame liên tục
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_update_image)
        self.timer.timeout.connect(self.handle_update_fps)
        self.timer.start(10)  

    def handle_update_image(self) -> None:
        frame = self.model.get_frame()
        if frame is not None:
            
            self.view.update_image_gui(frame)

    def handle_update_fps(self) -> None:
        fps = self.model.get_fps()
        if fps is not None:
            self.view.update_fps_gui(fps)
            
    def handle_stop_update_image(self) -> None:
        self.model.stop_preview_process()
        
