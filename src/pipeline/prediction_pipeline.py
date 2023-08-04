import os
from ultralytics import YOLO


model = YOLO(r'models\trained_models\best.pt')
image_dir = r"static\uploads"

def image_pred(image_name):
    image_path = os.path.join(image_dir, image_name)
    model.predict(image_path, save=True)
    
    