from src.component.data_ingestion import DataIngestion
from src.component.data_ingestion import DataIngestionConfig
from src.component.data_transformation import DataTransformation



if __name__ =='__main__':
    data_ingestion_obj =DataIngestion()
    train_path,test_path =data_ingestion_obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_path,test_path)
    