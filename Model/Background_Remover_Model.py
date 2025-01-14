from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PIL import Image
import io
import cv2
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import QThread

import os

import logging
from rembg import remove, new_session
from queue import Queue

class BackgroundRemoverWorker(QObject):
    finished_signal = pyqtSignal(int)
    error_signal = pyqtSignal(str)
    

    def __init__(self, image_path=None):
        super().__init__()
        # self.image_result_dir = 'AI_Test\\test_results'
        self.model_name = "u2net_human_seg"
        # isnet-general-use
        # u2net_human_seg
        # u2netp
        # silueta
        # birefnet-general-lite
        # birefnet-portrait
        
        self.session = new_session(model_name=self.model_name)
        self.image_path = image_path
        self.process_image_queue = Queue()
        self.is_processing = False
        
    
    def run(self):
        print("Worker started")
        
    def remove_background(self, image_info: dict):
        input = cv2.imread(image_info['path'])
    
        output = remove(input, session=self.session,
                        alpha_matting=True, 
                        alpha_matting_foreground_threshold=220, 
                        alpha_matting_background_threshold=10,
                        alpha_matting_erode_size=10,
                        post_process_mask=True)
        
        cv2.imwrite(image_info['removed_background_image_path'], output)

        self.finished_signal.emit(image_info['id'])
          
          
    @pyqtSlot(dict)  
    def receive_image_info(self, data : dict):
        self.process_image_queue.put(data)
        
            
    @pyqtSlot()
    def start_remove_background(self):
        while not self.process_image_queue.empty() and not self.is_processing:
            self.is_processing = True
            self.remove_background(self.process_image_queue.get())
            self.is_processing = False
        
        
    
        
        
