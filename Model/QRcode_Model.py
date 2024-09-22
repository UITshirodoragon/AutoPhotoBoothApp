import qrcode

# Đường link Google Drive tới file ảnh 
drive_link = 'https://drive.google.com/uc?export=download&id=1-2CFr0rqL1izAj7jx2kUFx6jrSJAaDhp'
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
img.save('qr_code_google_drive.png')

print("QR code đã được tạo thành công.")
