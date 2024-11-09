

# import sys
# import os

# # Đường dẫn tới folder chứa module 
# package_model_path = os.path.abspath(os.path.join('..', 'AutoPhotoBoothApp'))
# if package_model_path not in sys.path:
#     sys.path.append(package_model_path)

import time
from multiprocessing import Process, Queue, Pipe
import platform as plf
from typing import Protocol, Callable
import cv2
from cv2.typing import MatLike
from Model.Camera_Configuration_Model import CameraConfigurationModel
from Model.Template_Model import TemplateModel
from Model.User_Model import User
from PIL import Image
import ast
import json
# Protocol có tác dụng xác định và ràng buộc những method giao tiếp giữa các bên vơi nhau
        

class ImageCaptureModel:
    def __init__(self) -> None:
        
        self.camera = CameraConfigurationModel()
        
        self.camera.init_camera()
        
        # self.preview_image_queue = Queue()
        # self.preview_image_process = None
        # self.preview_fps_queue = Queue()
        # self.capture_signal_queue = Queue()
        # self.image_captured_count = Queue()
        # self.number_of_images = Queue()
        
        self.preview_frame_count = 0
        self.preview_last_time = time.time()
        
        self.preview_fps = 0.0
        self.iamge_captured_count = 0
        self.number_of_images = 0
        

    
    def start_preview_process(self) -> None:
        
        # self.preview_image_process = Process(target=self.preview_update_frame_process, 
        #                                      args=(self.preview_fps_queue, 
        #                                            self.preview_image_queue, 
        #                                            self.capture_signal_queue,
        #                                             self.image_captured_count,
        #                                             self.number_of_images,
        #                                            self.camera)
        #                                      )
        # self.preview_image_process.start()
        
        pass
        
    
    
    def preview_update_frame_process(self) -> None:
        # camera.init_camera()
        
        # self.preview_frame_count = 0
        # self.preview_last_time = time.time()
        # capture_count_max = None

        # while True:
        frame = self.camera.capture_frame()
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #  [:, 140:500 ]
        self.calculate_preview_fps()
        # if not number_of_images.empty():
        #     capture_count_max = number_of_images.get()
        #     print(f"Max number of images = {capture_count_max}")
            
        # if (not capture_signal_queue.empty() and not image_captured_count.empty()):
        #     camera.captured_and_saved_images_count = image_captured_count.get()
        #     if camera.captured_and_saved_images_count < capture_count_max:
        #         self.camera.capture_and_save_image(capture_signal_queue.get())
        #     else:
        #         print("Out of images in template")
        return frame
       
    def capture_image(self, user_image_gallery_folder_path: str, image_captured_count: int) -> None:
        self.camera.captured_and_saved_images_count = image_captured_count
        self.camera.capture_and_save_image(user_image_gallery_folder_path)
                    
    def get_frame(self) -> MatLike:
        return self.preview_update_frame_process()
        
    
    def get_fps(self) -> float:
        return self.preview_fps

    def calculate_preview_fps(self) -> None:
        self.preview_frame_count += 1
        current_time = time.time()
        if current_time - self.preview_last_time >= 1.0:
            self.preview_fps = self.preview_frame_count
            self.preview_frame_count = 0
            self.preview_last_time = current_time

    def stop_preview_process(self) -> None:
        self.camera.stop_camera()
        # if self.preview_image_process is not None:
        #     self.camera.stop_camera()
        #     self.preview_image_process.terminate()
    
