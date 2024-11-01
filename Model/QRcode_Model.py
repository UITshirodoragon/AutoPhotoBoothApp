import qrcode
import pickle
import os
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
import datetime

class GoogleDriveAPI():
    def __init__(self):
        #Tạo đối tượng xác thực để có quyền truy cập google drive
        #Tạo dịch vụ google drive API
        client_secret_file = "Data/client_secret.json"
        api_name = "drive"
        api_version = "v3"
        scope = "https://www.googleapis.com/auth/drive"
        CLIENT_SECRET_FILE = client_secret_file
        API_SERVICE_NAME = api_name
        API_VERSION = api_version
        SCOPES = scope
        cred = None
        pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
        # print(pickle_file)
        if os.path.exists(pickle_file):
            with open(pickle_file, 'rb') as token:
                cred = pickle.load(token)
        if not cred or not cred.valid:
            if cred and cred.expired and cred.refresh_token:
                cred.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
                cred = flow.run_local_server()
            with open(pickle_file, 'wb') as token:
                pickle.dump(cred, token)
        try:
            self.service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
            print(API_SERVICE_NAME, 'service created successfully')
        except Exception as e:
            print('Unable to connect.')
            print(e)

    def Upload(self, image_name : str, image_path : str) -> str: #Trả về id ảnh trên google drive
        image_metadata = {'name' : image_name} #Đặt tên file
        media = MediaFileUpload(image_path, mimetype='image/png',  resumable=True) #Định dạng ảnh PNG
        image = self.service.files().create(
            body=image_metadata,
            media_body=media,
            fields='id'
        ).execute()
        image_id = image.get('id')
        self.make_file_public(image_id)
        return image_id
    
    def make_file_public(self, image_id : str) -> None:
        try:
            # Thiết lập quyền truy cập cho tệp
            permission = {
                'type': 'anyone',       # Bất kỳ ai đều có quyền truy cập
                'role': 'reader'        # Cấp quyền chỉ đọc
            }
            self.service.permissions().create(
                fileId=image_id,
                body=permission
            ).execute()
            print("Quyền truy cập công khai đã được cấp thành công.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")

    def Create_QR(self, image_id : str, path : str) -> None:
       # Đường link Google Drive tới file ảnh 
        drive_link = 'https://drive.google.com/uc?export=download&id=' + image_id
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

    def Delete(self, image_id : str) -> None:
        try:
            self.service.files().delete(fileId=image_id).execute()
            print("File deleted successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")



if __name__ == "__main__":
    API = GoogleDriveAPI()
    image_name = 'final.png'
    image_path = 'Data/ImageGallery/user_uit000_image_gallery/final.png'
    QR_path = 'Data/qr.png'
    try:
        image_id = API.Upload(image_name, image_path)
        API.Create_QR(image_id, QR_path)
    except Exception as e:
        print(e)