import os
import sys
import yaml
import base64
from src.exception import CustomException
from src.logger import logging

def read_yaml(file_path:str)->str:
    try:
        with open(file_path, 'rb') as yaml_reader:
            logging.info('Read yaml file successfully')
            return yaml.safe_load(yaml_reader)
    
    except Exception as e:
        raise CustomException(e, sys) from e
    

def write_yaml(file_path: str, content: object, replace: bool = False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully write into file")
    
    except Exception as e:
        raise CustomException(e, sys)
    

def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open("./data/"+filename, "wb") as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())