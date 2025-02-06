from src.component.data_ingestion import DataIngestion
from src.component.data_ingestion import DataIngestionConfig


if __name__ =='__main__':
    data_ingestion_obj =DataIngestion()
    train_path,test_path =data_ingestion_obj.initiate_data_ingestion()
    print(train_path)
    print(test_path)