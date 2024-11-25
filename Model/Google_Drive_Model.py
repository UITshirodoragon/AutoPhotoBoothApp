import qrcode
import pickle
import os
import time
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request



CLIENT_SECRET_FILE = 'Data/GoogleDriveAuth/client_secret.json'
API_SERVICE_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]
PICKLE_FILE = f'Data/GoogleDriveAuth/token_{API_SERVICE_NAME}_{API_VERSION}.pickle'

class GoogleDriveModel():
    folder_id = None
    def __init__(self) -> None:
        #Tạo dịch vụ google drive AP
        self.init()

    def init(self) -> None:
        cred = None
        # print(PICKLE_FILE)
        if os.path.exists(PICKLE_FILE):
            with open(PICKLE_FILE, 'rb') as token:
                cred = pickle.load(token)
        if not cred or not cred.valid:
            if cred and cred.expired and cred.refresh_token:
                cred.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
                cred = flow.run_local_server()
            with open(PICKLE_FILE, 'wb') as token:
                pickle.dump(cred, token)
        try:
            self.service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
            print(API_SERVICE_NAME, 'Service created successfully')
            self.folder_id = self.Make_Folder('PhotoBooth_Cloud_Drive')
            print("Folder created successfully.")
        except Exception as e:
            print('Unable to connect.')
            print(e)

    def reset_mail_auth(self):
        if os.path.exists(PICKLE_FILE):
            os.remove(PICKLE_FILE)
            self.init()
            print("Reset service successfully!")
        else:  
            print("Reset service unsuccessfully!")

    def Upload(self, file_name : str, file_path : str, parent_id = None) -> str: #Trả về id ảnh trên google drive
        if parent_id == 'cloud_drive_folder':
            
            file_metadata = {
                            'name' : file_name,
                            'parents' : [self.folder_id]
                            } 
        else:
            file_metadata = {
                            'name' : file_name,
                            'parents' : [parent_id]
                    }
        media = MediaFileUpload(file_path, mimetype='image/png',  resumable=True) #Định dạng ảnh PNG
        file = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        file_id = file.get('id')
        return file_id
    
    def Make_Folder(self, folder_name : str, parent_id : str = None) -> str:
        #Create a folder
        folder_metadata = {
            'name' : folder_name,
            'mimeType' : 'application/vnd.google-apps.folder',
            'parents' : [parent_id]
        }
        folder = self.service.files().create(body=folder_metadata, fields="id").execute()
        folder_id = folder.get('id')
        return folder_id

    def make_file_public(self, file_id : str) -> None:
        try:
            # Thiết lập quyền truy cập cho tệp
            permission = {
                'type': 'anyone',       # Bất kỳ ai đều có quyền truy cập
                'role': 'reader'        # Cấp quyền chỉ đọc
            }
            self.service.permissions().create(
                fileId=file_id,
                body=permission
            ).execute()
            print("Quyền truy cập công khai đã được cấp thành công.")
        except Exception as e:
            print(f"Đã xảy ra lỗi tại cấp quyền truy cập: {e}")

    def Create_QR(self, file_id : str, path : str) -> None:

        # Đường link Google Drive tới file ảnh 
        drive_link = 'https://drive.google.com/uc?export=download&id=' + file_id
        # https://drive.google.com/file/d/1-2CFr0rqL1izAj7jx2kUFx6jrSJAaDhp/view?usp=drive_link
        # Tạo QR code

        qr = qrcode.QRCode(
            version=1,  # Version QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(drive_link)
        qr.make(fit=True)

        # Tạo ảnh QR code
        img = qr.make_image(fill='black', back_color='white')

        # Lưu QR code vào file PNG
        img.save(path)

        print("QR code đã được tạo thành công.")

    def Delete(self, object_id : str) -> None:
        try:
            if object_id == 'cloud_drive_folder':
                object_id = self.folder_id
            self.service.files().delete(fileId=object_id).execute()
            print("File deleted successfully.")
        except Exception as e:
            print(f"An error occurred in delete: {e}")


if __name__ == "__main__":
    # gdrive = GoogleDriveModel()
    # # gdrive.reset_mail_auth()
    # file_id = gdrive.Upload('test.png', 'Data/ImageGallery/user_uit000_image_gallery/final.png', folder_id)
    
    # gdrive.make_file_public(file_id)
    # gdrive.Create_QR(file_id, 'Data/ImageGallery/user_uit000_image_gallery/qr_code_google_drive.png')
    # time.sleep(30)
    
    # gdrive.Delete(folder_id)
    pass