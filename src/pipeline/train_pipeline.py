import sys
from src.exception import CustomException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TrainPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        try:
            logging.info(">>>> Training Pipeline Started <<<<")

            # Step 1: Data Ingestion
            data_ingestion = DataIngestion()
            train_data, test_data = data_ingestion.initiate_data_ingestion()
            logging.info("Data Ingestion completed")

            # Step 2: Data Transformation
            data_transformation = DataTransformation()
            train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
                train_data, test_data
            )
            logging.info("Data Transformation completed")

            # Step 3: Model Training
            model_trainer = ModelTrainer()
            r2_square = model_trainer.initiate_model_trainer(train_arr, test_arr)
            logging.info(f"Model Training completed with R2 score: {r2_square}")

            logging.info(">>>> Training Pipeline Completed <<<<")

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    pipeline = TrainPipeline()
    pipeline.run_pipeline()
