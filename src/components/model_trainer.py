import os
import sys
import zipfile
import shutil
from ultralytics import YOLO
from src.exception import CustomException
from src.logger import logging
from src.entity.artifacts_entity import ModelTrainerArtifact
from src.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, model_trainer_config = ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config
    

    def initiate_model_trainer(self,)->ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class.")

        try:
            logging.info("Pretrained model downloading starts!")
            logging.info("Model training starts!")
            os.system(f"yolo task=detect mode=train model={self.model_trainer_config.weight_name} data=src\config\data.yaml epochs={self.model_trainer_config.no_epochs} imgsz=640 save=true")

            os.makedirs(
                self.model_trainer_config.model_trainer_dir, exist_ok=True
            )
            
            shutil.copy(r"E:\Projects\helmet_detection\runs\detect\train5\weights\best.pt", self.model_trainer_config.model_trainer_dir)

            model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path="artifacts/model_trainer/best.pt")

            logging.info("Exited initiate_model_trainer method of ModelTrainer class.")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            raise CustomException(e, sys) 
        

