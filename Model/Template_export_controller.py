from PIL import Image
import sys
import os

# Đường dẫn tới folder chứa module 
package_controller_path = os.path.abspath(os.path.join('..', 'PhotoBoothApp'))
if package_controller_path not in sys.path:
    sys.path.append(package_controller_path)
from Model.Template import *

class  Template_Export_Controller():
   def __init__(self):
      self.list_export_image_paths = None
      self.final_export_base_path = None

   def export_template(self, num):
      template = None
      match num:
         case 2:
            template = Template_2grids()
         case 4:
            template = Template_4grids()
         case 6:
            template = Template_6grids()
         case 8:
            template = Template_8grids()

      img_index = 0
      background = Image.open(f'DataStorage/Templates/template{int(num/2)}.png')
      img_pos_list = template.getImagePositionList()
      for pos in img_pos_list:
            img = Image.open(self.list_export_image_paths[img_index]).resize(template.getImageSize())
            background.paste(img, pos)
            img_index += 1

      background.save(self.final_export_base_path +'/final.png')