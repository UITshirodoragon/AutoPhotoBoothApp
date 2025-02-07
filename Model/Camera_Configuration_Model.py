from __future__ import annotations
import time
from multiprocessing import Process, Queue
import platform as plf
from typing import Protocol, Callable
import numpy
import cv2
from cv2.typing import MatLike

from Model.Template_Model import TemplateModel

try:
    if plf.system() == "Linux":
        from picamera2 import Picamera2
        import libcamera
except ImportError as e:
    print(f"Lỗi {e}")
    


class CameraConfigurationModel:
    def __init__(self) -> None:

        self.camera = None
        self.camera_is_ready: bool = False
        
        self.just_captured_image_path: str = None
        self.captured_and_saved_images_count: int = 1
        
        self.template_control_model: TemplateModel = None
        
        # camera dell precision 3520 with resolution 640x480 (width x height)
        self.window_camera_ratio_resolution_config: dict = {
            "4:3": {
            "position": (0, 0),
            "size": (640, 480)
            },
            "3:4": {
            "position": (140, 0),
            "size": (360, 480)
            },
            "1:1": {
            "position": (80, 0),
            "size": (480, 480)
            },
            "2:3": {
            "position": (160, 0),
            "size": (320, 480)
            }
        }
        
        
        # pi camera v1 with resolution 2592x1944
        self.linux_camera_ratio_resolution_config: dict = {
            "4:3": {
            "position": (0, 0),
            "size": (1034, 768)
            },
            "3:4": {
            "position": (224, 0),
            "size": (576, 480)
            },
            "1:1": {
            "position": (128, 0),
            "size": (768, 768)
            },
            "2:3": {
            "position": (256, 0),
            "size": (512, 480)
            }
        }
        
    def init_camera(self) -> bool:
        try:
            if plf.system() == "Windows":
                self.camera = cv2.VideoCapture(1)
                # self.camera.set(cv2.CAP_PROP_FPS, 60)  # Cài đặt FPS mong muốn
            if plf.system() == "Linux":
                # init camera from Picamera2
                self.Picamera = Picamera2()

                self.nw_adjust_position_y = -84
                # preview_config = self.Picamera.create_preview_configuration()
                # capture_config = self.Picamera.create_preview_configuration(lores= {"size" : (1024, 600), "format" : "RGB888"}, main= {"size" : (2592,1944), "format" : "RGB888"}, display="lores")
                
                # self.Picamera.preview_configuration.sensor.output_size = (2560, 1500)
                # self.Picamera.preview_configuration.sensor.bit_depth = 10
                # self.Picamera.preview_configuration.enable_raw()
                # self.Picamera.preview_configuration.raw.size = (2560,1500)
                # self.Picamera.preview_configuration.format = "SBGGR10"
                self.Picamera.preview_configuration.main.size = (1024, 768) # set size for preview
                self.Picamera.preview_configuration.main.format = "BGR888" # set format color
                self.Picamera.preview_configuration.controls.FrameRate = 60.0 # set FPS
                self.Picamera.still_configuration.main.size = (2592,1944)
                self.Picamera.still_configuration.main.format = "XRGB8888"
                # self.Picamera.preview_configuration.align() # set align
                # self.Picamera.preview_configuration.enable_lores()
                # self.Picamera.preview_configuration.lores.size = (1024, 768)
                # self.Picamera.preview_configuration.lores.format = "BGR888"
                self.Picamera.preview_configuration.align()
                self.Picamera.still_configuration.align()
                
                # self.preview_config = self.Picamera.preview_configuration_
                # self.still_config = self.Picamera.still_configuration_
                
                self.Picamera.configure("preview") # configuration for preview
                
                                            #'Sharpness': 1.0, # (0.0, 16.0, 1.0)
                                            #'ExposureValue': 0.0, #(-8.0, 8.0, 0.0)
                                            #'AeConstraintMode': 0, #(0, 3, 0)
                                            #'ScalerCrop': (0, 0, 2592, 1944), # ((0, 0, 130, 98), (0, 0, 2592, 1944), (0, 0, 2592, 1944))
                                            #'AnalogueGain': 1.0, #(1.0, 63., None)
                                            #'NoiseReductionMode': 0, #(0, 4, 0)
                                            #'AeMeteringMode': 0, #(0, 3, 0)
                                            #'ExposureTime': 33333, #(92, 760636, None)
                                            #'HdrMode': 1, #(0, 4, 0)
                                            #'AwbEnable': False, #(False, True, None)
                                            #'Saturation': 1.0, #(0.0, 32.0, 1.0)
                                            #'Contrast': 1.0, #(0.0, 32.0, 1.0)
                                            #'ColourGains': 1.0, #(0.0, 32.0, None)
                                            #'Brightness': 1.0, #(-1.0, 1.0, 0.0)
                                            #'FrameDurationLimits': 23123,# (23123, 760729, None)
                                            #'AeFlickerPeriod': 10000, #(100, 1000000, None)
                                            #'AwbMode': 0, #(0, 7, 0)
                                            #'AeFlickerMode': 0, #(0, 1, 0)
                                            #'AeExposureMode': 0, #(0, 3, 0)
                                            #'StatsOutputEnable': 0, #(False, True, False)
                                            #'AeEnable': False #(False, True, None)
                
                self.Picamera.set_controls({'Brightness': 0.05, 'Sharpness': 1.0})
                
                self.Picamera.start() # start Pi
            
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
                    frame = cv2.flip(frame, 1)
                    frame = self.crop_image(frame, 
                                            self.template_control_model.get_template_with_field_from_database(self.template_control_model.selected_template_id, 'image_ratio'),
                                            "Windows"
                                            )
                    
            if plf.system() == "Linux":
                frame = self.Picamera.capture_array("main")
                
                ##frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                # frame = cv2.flip(frame, 1)
                # frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            return frame
        except Exception as error:
            print(f"Error {error}")
            
    def capture_and_save_image(self, user_image_gallery_folder_path, index_of_image: int = None):
        if index_of_image is None:
            
            self.just_captured_image_path = user_image_gallery_folder_path + f"/image{self.captured_and_saved_images_count}.png"
        else:
            self.just_captured_image_path = user_image_gallery_folder_path + f"/image{index_of_image}.png"
        
        try:
            
            if plf.system() == 'Windows':
                
                _, image = self.camera.read()
                
                image = self.crop_image(image, 
                                            self.template_control_model.get_template_with_field_from_database(self.template_control_model.selected_template_id, 'image_ratio'),
                                            "Windows"
                                            )
                cv2.imwrite(self.just_captured_image_path, image)
                
            elif plf.system() == 'Linux':
                
                # image = self.Picamera.capture_array("main")
                image_job = self.Picamera.switch_mode_and_capture_array(camera_config="still",
                                                                         name= "main",
                                                                         wait= False)
                
                # Nhận ảnh
                image = self.Picamera.wait(image_job)
                # image = self.Picamera.switch_mode_and_capture_array(camera_config="still",
                                                                        # name= "main")
                # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
                image = cv2.flip(image, 1)
                cv2.imwrite(self.just_captured_image_path, image)
                # self.Picamera.capture_file(f'DataStorage/ImageGallery/image{self.Captured_numbers}.png')     
        
        except Exception as e:
            # thay the bang log sau
            print(f"Lỗi: {e}") 
        # self.captured_and_saved_images_count += 1
    
    def crop_image(self, image: MatLike, ratio: str, camera: str) -> MatLike:
        x: int = 0
        y: int = 0
        w: int = 0
        h: int = 0
        if camera == "Windows":
            x, y = self.window_camera_ratio_resolution_config[ratio]["position"]
            w, h = self.window_camera_ratio_resolution_config[ratio]["size"]
            cropped_image: MatLike = image[y:y+h, x:x+w]
            cropped_image.shape = (h, w, 3)
            return cropped_image
        elif camera == "Linux":
            # dev later
            return image
            
    

    def stop_camera(self) -> None:
        pass