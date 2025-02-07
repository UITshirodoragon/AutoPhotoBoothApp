from PIL import Image

def remove_sRGB_profile(image_path, output_path):
    with Image.open(image_path) as img:
        data = list(img.getdata())
        img_without_profile = Image.new(img.mode, img.size)
        img_without_profile.putdata(data)
        img_without_profile.save(output_path)

# Sử dụng hàm này
input_image_path = 'Data\Template\graduation_day_template_2x2_2.png'
output_image_path = 'path/to/your/output/image.jpg'
remove_sRGB_profile(input_image_path, input_image_path)