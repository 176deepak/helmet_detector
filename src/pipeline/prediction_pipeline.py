import os
from ultralytics import YOLO


model = YOLO(r'models\trained_models\best.pt')
image_dir = r"app\static\uploads"
pred_dir = r"E:\Projects\helmet_detection\runs\detect\predict"

def image_pred(image_name):
    image_path = os.path.join(image_dir, image_name)
    model.predict(image_path, save=True)
    path = os.path.join(pred_dir, image_name)
    return path
