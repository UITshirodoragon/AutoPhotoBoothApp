from __future__ import annotations
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QStackedWidget
from Model.Image_Processing_Model import ImageProcessingModel
from Model.User_Model import *
from View.Image_Capture_View import ImageCaptureView
from typing import Protocol
from cv2.typing import MatLike


class ImageCapturePresenter:
    def __init__(self, model: ImageProcessingModel,
                 view: ImageCaptureView,
                 stack_view: QStackedWidget,
                 user_control_model: UserModel
                 ) -> None:
        self.view = view
        self.model = model
        self.stack_view = stack_view
        self.user_control_model = user_control_model
        
        # Khởi động camera trong model
        self.model.start_preview_process()
        
        # Thiết lập QTimer để cập nhật frame liên tục
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_update_preview_image)
        self.timer.timeout.connect(self.handle_update_preview_fps)
        self.timer.start(10)
        
        self.view.ICV_back_button_signal.connect(self.handle_back_button_clicked)
        self.view.ICV_next_button_signal.connect(self.handle_next_button_clicked)
        self.view.ICV_capture_button_signal.connect(self.handle_capture_button_clicked)

    def handle_back_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(1)
        
    def handle_next_button_clicked(self) -> None:
        self.stack_view.setCurrentIndex(3) 
    
    def handle_capture_button_clicked(self) -> None:
        print(self.user_control_model.get_user().gallery_folder_path)
        self.model.capture_signal_queue.put(obj = self.user_control_model.get_user().gallery_folder_path)
    
    def handle_update_preview_image(self) -> None:
        frame = self.model.get_frame()
        if frame is not None:       
            self.view.update_preview_image_gui(frame)

    def handle_update_preview_fps(self) -> None:
        fps = self.model.get_fps()
        if fps is not None:
            self.view.update_preview_fps_gui(fps)
            
    def handle_stop_update_preview_image(self) -> None:
        self.model.stop_preview_process()
        
