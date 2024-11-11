from Model.Template_Model import TemplateModel
from Model.Google_Drive_Model import GoogleDriveModel



from PIL import Image
from Model.User_Model import User
import json
import time
from PyQt5.QtCore import pyqtSignal, QThread
import datetime


class TemplateExportModel(): 
    def __init__(self) -> None:
        
        pass
    
    def export_template_with_images(self, template: dict, 
                                    user: User , 
                                    progress_emit_signal_function = None, 
                                    finished_emit_signal_function = None
                                    ) -> None:
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
                progress_emit_signal_function((img_index)*100//(template['number_of_images'])-25)
                # time.sleep(0.5)
                # value = (img_index)*100//(template['number_of_images'])
                
            
        
        background.save(user.gallery_folder_path + f'/final_user_{user.id}.png')
         
        # if finished_emit_signal_function is not None:
        #     finished_emit_signal_function()
        
    def export_template_with_a_image(self, template: dict, 
                                     image: dict, 
                                     progress_emit_signal_function = None, 
                                     finished_emit_signal_function = None
                                     ) -> None:
        background = Image.open(template['path'])
        img_pos_list = json.loads(template['image_positions_list'])
        
        print(f"add image {image['path']} to template {template['path']}")
        
        img = Image.open(image['path']).resize(tuple(json.loads(template['image_size'])))
        background.paste(img, tuple(img_pos_list[image['id'] - 1]))   # change list to tuple
        background.save(image['template_with_image_path'])
        
class TemplateExportWorker(QThread):
    TEW_progress_signal = pyqtSignal(int)
    TEW_finished_signal = pyqtSignal()

    def __init__(self, 
                 template_export_model: TemplateExportModel,
                 google_drive_model: GoogleDriveModel,
                 template: dict, 
                 user: User):
        super().__init__()
        self.template: dict = template
        self.user: User = user
        self.template_export_model = template_export_model
        self.GoogleDriveModel = google_drive_model
        
    def set_template(self, template: dict):
        self.template = template
        
    def set_user(self, user: User):
        self.user = user
        
    def run(self):
        self.template_export_model.export_template_with_images(self.template, self.user, self.TEW_progress_signal.emit, self.TEW_finished_signal.emit)
        current_time = datetime.datetime.now()
        template_drive_file_id = self.GoogleDriveModel.Upload(f'final_user_{self.user.id}_{current_time.strftime('%d%m%Y_%H%M%S')}.png', self.user.gallery_folder_path + f'/final_user_{self.user.id}.png', 'cloud_drive_folder')
        self.TEW_progress_signal.emit(80)
        
        self.GoogleDriveModel.make_file_public(template_drive_file_id)
        self.TEW_progress_signal.emit(90)
        
        self.GoogleDriveModel.Create_QR(template_drive_file_id, self.user.gallery_folder_path + f'/qr_code_google_drive_user_{self.user.id}.png')
        self.TEW_progress_signal.emit(100)
        time.sleep(1)
        self.TEW_finished_signal.emit()
        
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