from __future__ import annotations
import time
from multiprocessing import Process, Queue
import platform as plf
from typing import Protocol, Callable
import numpy
import cv2
from cv2.typing import MatLike


class CameraConfigurationModel:
    def __init__(self) -> None:

        self.camera = None
        self.camera_is_ready: bool = False
        
    def init_camera(self) -> bool:
        try:
            if plf.system() == "Windows":
                self.camera = cv2.VideoCapture(0)
                self.camera.set(cv2.CAP_PROP_FPS, 60)  # Cài đặt FPS mong muốn
            if plf.system() == "Linux":
                pass
            
            self.camera_is_ready = True
            return True
        
        except Exception as error:
            print(f"Error {error}")
            return False


    def capture_frame(self) -> MatLike:
        try:
            if plf.system() == "Windows":
                ret, frame = self.camera.read()
                if ret:
                    return frame
            if plf.system() == "Linux":
                pass
        
        except Exception as error:
            print(f"Error {error}")
    

    def stop_camera(self) -> None:
        pass