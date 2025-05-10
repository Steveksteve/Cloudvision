from PIL import Image
import io

def process_image(image_bytes: bytes):
    image = Image.open(io.BytesIO(image_bytes))
    # Traitement image ici
    return image
