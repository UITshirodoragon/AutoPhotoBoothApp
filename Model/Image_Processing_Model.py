from __future__ import annotations

# import sys
# import os

# # Đường dẫn tới folder chứa module 
# package_model_path = os.path.abspath(os.path.join('..', 'AutoPhotoBoothApp'))
# if package_model_path not in sys.path:
#     sys.path.append(package_model_path)

import time
from multiprocessing import Process, Queue
import platform as plf
from typing import Protocol, Callable
import cv2
from cv2.typing import MatLike
from Model.Camera_Configuration_Model import CameraConfigurationModel



# Protocol có tác dụng xác định và ràng buộc những method giao tiếp giữa các bên vơi nhau

class ImageCapturePresenter(Protocol):
    def handle_update_image(self) -> None:
        ...
    
    def handle_update_fps(self) -> None:
        ...
        

class ImageProcessingModel:
    def __init__(self) -> None:
        
        self.camera = CameraConfigurationModel()
        
        self.preview_image_queue = Queue()
        self.preview_image_process = None
        self.preview_fps_queue = Queue()
        

    
    def start_preview_process(self) -> None:
        self.preview_image_process = Process(target=self.preview_update_frame_process, 
                                             args=(self.preview_fps_queue, 
                                                   self.preview_image_queue, 
                                                   self.camera)
                                             )
        self.preview_image_process.start()
    
    
    def preview_update_frame_process(self, 
                                     fps_queue: Queue, 
                                     frame_queue: Queue, 
                                     camera: CameraConfigurationModel
                                     ) -> None:
        camera.init_camera()
        self.preview_frame_count = 0
        self.preview_last_time = time.time()
        while True:
            frame = camera.capture_frame()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (450, 600))
            frame_queue.put(frame)
            self.calculate_preview_fps(fps_queue)
        
    def get_frame(self) -> MatLike:
        if not self.preview_image_queue.empty():
            return self.preview_image_queue.get()
        return None
    
    def get_fps(self) -> float:
        if not self.preview_fps_queue.empty():
            return self.preview_fps_queue.get()
        return None

    def calculate_preview_fps(self, fps_queue: Queue) -> None:
        self.preview_frame_count += 1
        current_time = time.time()
        if current_time - self.preview_last_time >= 1.0:
            fps = self.preview_frame_count
            self.preview_frame_count = 0
            self.preview_last_time = current_time
            fps_queue.put(fps)

    def stop_preview_process(self) -> None:
        if self.preview_image_process is not None:
            self.preview_image_process.terminate()
            
    