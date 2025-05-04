from ultralytics import YOLO
import numpy as np

model = YOLO("yolov8n.pt")  # Or yolov8s.pt for better accuracy
model.to("cpu")

def detect_cars(image):
    results = model(image)
    boxes = []
    count = 0

    for r in results:
        for box in r.boxes.data.tolist():
            cls_id = int(box[5])
            if model.names[cls_id] in ['car', 'truck', 'bus']:
                count += 1
                x1, y1, x2, y2 = map(int, box[:4])
                boxes.append((x1, y1, x2, y2))

    return count, boxes