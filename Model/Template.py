
import json

class Template:
    def __init__(self, user_id, path, style, number_of_images, images_position_list, stickers_position_list, frame_path):
        self.user_id = user_id
        self.path = path
        self.style = style
        self.number_of_images = number_of_images
        self.images_position_list = images_position_list
        self.stickers_position_list = stickers_position_list
        self.frame_path = frame_path

        self.width = None
        self.height = None
        self.image_size = None

    def getStickersPosition(self):
        return self.stickers_position_list

    def getFramePath(self):
        return self.frame_path

    def getImageSize(self):
        return self.image_size
    
    def getImagePositionList(self):
        return self.images_position_list

    def setStickersPosition(self, stickers_position_list):
        self.stickers_position_list = stickers_position_list


class Template_2grids(Template):
    def __init__(self):
        self.width = 1500
        self.height = 1100
        self.number_of_images = 2
        self.image_size = (676, 507)
        self.images_position_list = [(52,68), (780, 508)]


class Template_4grids(Template):
    def __init__(self):
        self.width = 1500
        self.height = 1100
        self.number_of_images = 4
        self.image_size = (588, 441)
        self.images_position_list = [(143,53), (143, 525), 
                                     (766, 53), (766, 525)]

class Template_6grids(Template):
    def __init__(self):
        self.width = 1500
        self.height = 1000
        self.number_of_images = 6
        self.image_size = (552, 414)
        self.images_position_list = [(39, 58), (624, 58), (1209, 58), 
                                     (39, 621), (624, 621), (1209, 621)]
        
class Template_8grids(Template):
    def __init__(self):
        self.width = 1100
        self.height = 1500
        self.number_of_images = 8
        self.image_size = (592, 444)
        self.images_position_list = [(92, 48), (720, 48),
                                     (92, 528), (720, 528),
                                     (92, 1010), (720, 1010),
                                     (92, 1490), (720, 1490)]

              