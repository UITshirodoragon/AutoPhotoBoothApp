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
    finished = pyqtSignal()
    error = pyqtSignal(str)
    

    def __init__(self, image_path=None):
        super().__init__()
        self.image_result_dir = 'AI_Test\\test_results'
        self.model_name = "isnet-general-use"
        self.session = new_session(model_name=self.model_name)
        self.image_path = image_path
        self.process_image_queue = Queue()
        self.is_processing = False
        
    
    def run(self):
        print("Worker started")
        
    def remove_background(self):
        input = cv2.imread(self.image_path)
    
        output = remove(input, session=self.session, 
                        alpha_matting=True, 
                        alpha_matting_foreground_threshold=240, 
                        alpha_matting_background_threshold=30,
                        alpha_matting_erode_size=20)
        
        cv2.imwrite(self.image_result_dir + '\\' + os.path.basename(self.image_path), output)

        self.finished.emit()
          
          
    @pyqtSlot(str)  
    def receive_image_path(self, data):
        self.process_image_queue.put(data)
        
            
    @pyqtSlot()
    def start_remove_background(self):
        while not self.process_image_queue.empty() and not self.is_processing:
            self.is_processing = True
            self.image_path = self.process_image_queue.get()
            self.remove_background()
            self.is_processing = False
        
        
    
        
        
