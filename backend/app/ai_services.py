from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Chargement du modèle et processor Hugging Face (image captioning)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def analyze_image(image: Image.Image) -> dict:
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return {"caption": caption}
