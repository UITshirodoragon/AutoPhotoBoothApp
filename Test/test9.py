from PIL import Image

def get_png_metadata(image_path):
    image = Image.open(image_path)
    metadata = image.info  # This will contain the text chunks and other info

    if not metadata:
        return "No metadata found"

    return metadata

image_path = 'Test/template1.png'
metadata = get_png_metadata(image_path)

if isinstance(metadata, dict):
    for key, value in metadata.items():
        print(f"{key}: {value}")
else:
    print(metadata)