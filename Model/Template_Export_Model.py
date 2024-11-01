from Model.Template_Model import TemplateModel
from PIL import Image
from Model.User_Model import User
import json
import time
from PyQt5.QtCore import pyqtSignal, QThread



class TemplateExportModel(): 
    def __init__(self) -> None:
        
        pass
    
    def export_template_with_images(self, template: dict, user: User , progress_emit_signal_function = None, finished_emit_signal_function = None) -> None:
        value: int = 0
        img_index = 0
       
        background = Image.open(template['path'])
        img_pos_list = json.loads(template['image_positions_list'])     # type list of list
        for pos in img_pos_list:
            
            print(user.gallery_folder_path + f"/image{img_index}.png")
            img = Image.open(user.gallery_folder_path + f"/image{img_index}.png").resize(tuple(json.loads(template['image_size'])))
            background.paste(img, tuple(pos))   # change list to tuple
            
            img_index += 1
            if progress_emit_signal_function is not None:
                # for num in range(value, min((img_index)*100//(template['number_of_images'])), 99):
                    # print((img_index+1)*100//(template['number_of_images']))
                progress_emit_signal_function((img_index)*100//(template['number_of_images']))
                # time.sleep(0.5)
                # value = (img_index)*100//(template['number_of_images'])
                
            
        
        background.save(user.gallery_folder_path +'/final.png')
         
        if finished_emit_signal_function is not None:
            finished_emit_signal_function()
        
        
        
class TemplateExportWorker(QThread):
    TEW_progress_signal = pyqtSignal(int)
    TEW_finished_signal = pyqtSignal()

    def __init__(self, template_export_model: TemplateExportModel, template: dict, user: User):
        super().__init__()
        self.template: dict = template
        self.user: User = user
        self.template_export_model = template_export_model
        
    def set_template(self, template: dict):
        self.template = template
        
    def set_user(self, user: User):
        self.user = user
        
    def run(self):
        self.template_export_model.export_template_with_images(self.template, self.user, self.TEW_progress_signal.emit, self.TEW_finished_signal.emit)
        # img_index = 0
        # background = Image.open(self.template['path'])
        # img_pos_list = json.loads(self.template['image_positions_list'])  # type list of list
        # for pos in img_pos_list:
        #     img = Image.open(self.user.gallery_folder_path + f"/image{img_index}.png").resize(tuple(json.loads(self.template['image_size'])))
        #     background.paste(img, tuple(pos))  # change list to tuple
        #     self.progress.emit((img_index + 1) * 100 // self.template['number_of_images'])
        #     img_index += 1
        # background.save(self.user.gallery_folder_path + '/final.png')
        # self.finished.emit()