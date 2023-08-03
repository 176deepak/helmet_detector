ARTIFACTS_DIR:str = "artifacts"

DATA_INGESTION_DIR_NAME:str = "data"

DATA_INGESTION_EXTRACETED_DATA_DIR:str = "unzipped_data"

DATA_INGESTION_PROCESSED_DATA_DIR:str = "processed_data"

DATA_DOWNLOAD_URL:str = "https://drive.google.com/file/d/1E1kTZu8C64F2h01gtSvCPLWibOk1QlSb/view?usp=sharing"


DATA_VALIDATION_DIR_NAME:str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["images", "labels"]


MODEL_TRAINER_DIR_NAME:str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME:str = "yolov8n.pt"

MODEL_TRAINER_NO_EPOCHS:int = 5

MODEL_TRAINER_BATCH_SIZE:int = 16