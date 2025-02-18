import os
import torch
from datetime import datetime

# Common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
CLASSES = ["A+", "A-", "AB+", "AB-", "B+", "B-", "O+", "O-"]
APP_PORT = 8080
APP_HOST = "0.0.0.0"
UPLOAD_FOLDER = "static/uploads"
COMMAND = "export KAGGLE_CONFIG_DIR=/Users/adityachaudhary/Desktop/Important Projects/Data Science/BloodGroup-Detection-Using-Fingerprint/.kaggle"

# Data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR = os.path.join("artifacts", "DataIngestionArtifacts")
DATA_INGESTION_UNZIPED_ARTIFACTS_DIR = "dataset_blood_group"
SOURCE_URL = "https://www.kaggle.com/datasets/rajumavinmar/finger-print-based-blood-group-dataset/data"
CREDENTIAL = "rajumavinmar/finger-print-based-blood-group-dataset"
KAGGLE_CREDENTIAL_DIR = "/Users/adityachaudhary/Desktop/Important Projects/Data Science/BloodGroup-Detection-Using-Fingerprint/.kaggle"

# Data Transformation constants
DATA_TRANSFORMATION_ARTIFACTS_DIR = "DataTransformationArtifacts"
TRAIN_LOADER = "train_loader.pt"
VAL_LOADER = "val_loader.pt"
TEST_LOADER = "test_loader.pt"
IMAGE_SIZE = (64, 64)
BATCH_SIZE = 64
NUM_WORKERS = 4

# Model Trainer constants
MODEL_TRAINER_ARTIFACTS_DIR = "ModelTrainerArtifacts"
FINAL_MODEL_PATH = os.path.join("artifacts", "FinalModel")
EPOCH_MODEL = "epoch_model.pth"
FINAL_MODEL_AFTER_EVALUATION_NAME = "final_model_after_evaluation.pth"
FINAL_MODEL_AFTER_TRAINING_NAME = "final_model_after_training.pth"
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
PATIENCE = 5
EPOCHS = 50
LEARNING_RATE = 0.001