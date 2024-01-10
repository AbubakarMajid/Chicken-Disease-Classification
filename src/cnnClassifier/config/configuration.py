from cnnClassifier.utils.common import *
from cnnClassifier.constants import *
from cnnClassifier.enitity.config_entity import DataIngestionClass

class configurationnManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH, params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_ingestion_config(self) -> DataIngestionClass:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionClass(root_dir= config.root_dir, source_URL= config.source_URL, local_data_file= config.local_data_file,
                                                   unzip_dir= config.unzip_dir)
        
        return data_ingestion_config
