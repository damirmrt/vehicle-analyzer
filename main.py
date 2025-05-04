from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from utils.detect import detect_cars
from utils.captioning import generate_caption
from utils.color_utils import count_red_cars
from PIL import Image
import io

app = FastAPI()

@app.post("/analyze-image")
async def analyze_image(image: UploadFile = File(...)):
    image_bytes = await image.read()
    image_pil = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    total_cars, car_boxes = detect_cars(image_pil)
    red_cars = count_red_cars(image_pil, car_boxes)
    description = generate_caption(image_pil)

    return JSONResponse(content={
        "total_cars": total_cars,
        "red_cars": red_cars,
        "description": description
    })