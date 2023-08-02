'''

filename: template.py

This template.py file will be used for creating entire project folder structure in just one command based on Techniques(Machine Learning, Deep Learning, Computer Vision or Natural Language Processing).
Just create this file or copy and paste source code and enter below command in your terminal or cmd to create folder structure.

Command:- python template.py
'''


# required modules 
import os
from pathlib import Path
from datetime import datetime
import logging

# project name 
project_name = "helmet_detector"

# file for recording logs while creating folders of project
log_file = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOGS_PATH = os.path.join(os.getcwd(), 'LOGS/template/')
if not os.path.exists(LOGS_PATH):
    os.makedirs(LOGS_PATH)

log_file_path = os.path.join(LOGS_PATH, log_file)
with open(log_file_path, 'w') as f:
    pass

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")

# all required folders and files in Project
paths = [
    '.github/workflows/.gitkeep',
    'data/',  
    'models/pretrained_models/',
    'models/trained_models/',
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/utils/__init__.py",
    f"src/config/__init__.py",
    f"src/config/configuration.py",
    f"src/pipeline/__init__.py",
    f"src/entity/__init__.py",
    f"src/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    'setup.py',
    "notebooks/research.ipynb",
    'app/templates/index.html',
    'app/static/CSS/style.css',
    'app/static/javascript/script.js',
    'app/static/images/',
    'requirements.txt',
    'README.md',
]

# creating files and folders
for filepath in paths:
    path = filepath
    filepath = Path(filepath)

    if os.path.exists(filepath):
        logging.info(f"{filepath} already exists!")

    else:
        # This will check whether a filepath is ending with a slash. If yes, then this is a directory for empty folder creation not a file.
        if path[-1] == "/":                    
            os.makedirs(filepath, exist_ok=True)
            logging.info(f"Creating a empty {filepath} folder directory.")
        else:
            # splits the path in folder and filename
            filedir, filename = os.path.split(filepath)

            # if folder not exists, create first folder for further files.
            if filedir != "":
                os.makedirs(filedir, exist_ok=True)
                logging.info(f"Creating directory: {filedir} for the file: {filename}")

            # if any files doesn't contains anything in it...
            if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
                with open(filepath, 'w') as f:
                    pass
                    logging.info(f"Creating empty file: {filepath}")
            else:
                logging.info(f"{filename} is already exists")