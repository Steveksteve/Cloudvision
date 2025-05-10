history = []  # pour l'instant, stocké en RAM
from fastapi import APIRouter, UploadFile, File
from PIL import Image
import io
from .ai_services import analyze_image
from .image_processing import process_image

router = APIRouter()

import boto3
from botocore.client import Config
import uuid

s3 = boto3.client(
    's3',
    endpoint_url="http://minio:9000",
    aws_access_key_id="admin",
    aws_secret_access_key="password",
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)

BUCKET = "images"
s3.create_bucket(Bucket=BUCKET)  # safe to call again, idempotent

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()
    
    # Enregistrement dans S3 (MinIO)
    filename = f"{uuid.uuid4()}.jpg"
    s3.put_object(Bucket=BUCKET, Key=filename, Body=contents)

    # Traitement
    image = Image.open(io.BytesIO(contents))
    result = analyze_image(image)

    # Enregistrement historique (exemple simple en mémoire)
    history.append({"filename": filename, "result": result})

    return {"filename": filename, "result": result}

@router.get("/history")
def get_history():
    return {"history": history}
