import os 
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd  # type: ignore
from dataclasses import dataclass
from sklearn.model_selection import train_test_split  # type: ignore

@dataclass
class DataIngestionConfig:
    train_data_path :str = os.path.join('artifacts','train.csv')
    test_data_path :str = os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):        
        self.ingestion_config = DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or componet")
        try:
            df = pd.read_csv('Dataset\winequality-red.csv')
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path),exist_ok=True)
            logging.info('Train Test Split initiated')
            train_set,test_set  = train_test_split(df,test_size=0.30,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index =False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header = True )
            logging.info('Ingestion of the data is completed')
            return  (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e :
            raise CustomException(e,sys)
