from cnnClassifier.config.configuration import configurationnManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

stage_name = "Data Ingestion Stage"


class DataIngestionPipeline:

    def __init__(self):
        pass


    def main(self):
        config = configurationnManager()
        data_ingestion_config = config.get_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e