from Model.Template_Model import TemplateModel
from PIL import Image
from Model.User_Model import User
import json


class TemplateExportModel:
    def __init__(self) -> None:
        pass
    
    def export_template_with_images(self, template: dict, user: User ) -> None:
        img_index = 0
        background = Image.open(template['path'])
        img_pos_list = json.loads(template['image_positions_list'])     # type list of list
        for pos in img_pos_list:
                img = Image.open(user.gallery_folder_path + f"/image{img_index}.png").resize(tuple(json.loads(template['image_size'])))
                background.paste(img, tuple(pos))   # change list to tuple
                img_index += 1

        background.save(user.gallery_folder_path +'/final.png')
        