from cnnClassifier.enitity.config_entity import DataIngestionClass
import urllib.request as request
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
import zipfile
from pathlib import Path
import os


class DataIngestion:
    def __init__(self, config : DataIngestionClass):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename , headers = request.urlretrieve(url = self.config.source_URL,
                                                     filename= self.config.local_data_file)
            logger.info(f"{filename} downloaded successfully with following ingo : {headers}")
        else:
            filename= self.config.local_data_file
            logger.info(f"{filename} already downloaded of size : {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file , 'r') as zip_ref:
            zip_ref.extractall(unzip_path)