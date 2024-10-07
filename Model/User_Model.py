import os
import shutil
import time
class User:
    
    def __init__(self):
        self.id = None
        self.name = None
        self.email = None
        self.is_working = True
        self.gallery_folder_path = None
        
    def delete(self):
        del self
        
    def work(self):
        print(f"user {self.id} is working")
        
class UserModel:
    
    def __init__(self):
        self.user_limit_count = 2
        self.user_id_count = 0
        self.user_count = 0
        self.user_list = []
        self.base_image_gallery_path = "Data/ImageGallery"
        
        
        
    def create_user(self):
        if self.user_count == 0:
            print("create current user")
            self.current_user = User()
            self.current_user.id = f"uit{self.user_id_count:03}"
            self.user_list.append(self.current_user)
            self.user_count += 1
            self.user_id_count += 1
            self.create_user_image_gallery()
        elif not self.current_user.is_working:
            print("create current user")
            self.current_user = User()
            self.current_user.id = f"uit{self.user_id_count:03}"
            self.user_list.append(self.current_user)
            self.user_count += 1
            self.user_id_count += 1
            self.create_user_image_gallery()
        else:
            print("current user is working can't create new user")
          
    
    def enable_user(self, index = -1):
        if not self.user_list[index].is_working:
            self.user_list[index].is_working = True
        
    
    def disable_user(self, index = -1):
        if self.user_list[index].is_working:
            self.user_list[index].is_working = False
    
    
    def delete_user(self):
        if self.current_user.is_working:
            
            #delete previous user
            self.head_user = self.user_list[0]
            if not self.head_user.is_working and self.user_count > self.user_limit_count:
                self.user_list.remove(self.head_user)
                self.delete_user_image_gallery(self.head_user)
                self.user_count -= 1
                print(f"delete user {self.head_user.id}")
                self.head_user.delete()
        else:
            pass
        
    def get_user(self, index = -1) -> User:
        return self.user_list[index]
    
    def create_user_image_gallery(self):
        
        self.folder_name = os.path.join(self.base_image_gallery_path, f"user_{self.current_user.id}_image_gallery")  # Tạo đường dẫn thư mục đầy đủ
        if os.path.exists(self.folder_name):
            shutil.rmtree(self.folder_name)
        os.makedirs(self.folder_name, exist_ok=True)  # Tạo thư mục
        self.current_user.gallery_folder_path = self.folder_name.replace('\\','/')
        
    def delete_user_image_gallery(self, user):
        
        if os.path.exists(user.gallery_folder_path):
            shutil.rmtree(user.gallery_folder_path)  # Xóa thư mục và tất cả nội dung bên trong
            print(f"Deleted folder: {user.gallery_folder_path}")
        else:
            print(f"Folder {user.gallery_folder_path} does not exist.")
        

# test

# user_controller = User_Controller()


# for i in range(0, 10):
#     print(i)
#     user_controller.create_user()
    
#     if i == 2:
#         user_controller.create_user()
        
#     user_controller.get_user().work()
#     time.sleep(5)
#     print(user_controller.get_user().is_working)
#     print(user_controller.get_user().gallery_folder_path)
#     user_controller.delete_user()
#     user_controller.disable_user()
    

# for i in range(0, user_controller.user_count):
#     print(user_controller.user_list[i].is_working)





