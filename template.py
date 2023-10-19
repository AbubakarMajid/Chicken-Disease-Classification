import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO , format = "[%(asctime)s]: %(message)s")


project_name = "Chicken-Disease-Classcification"

list_files = [
    ".github/worflows/.gitkeep", 
    f"src/{project_name}/.__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py"
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/enitity/__init__.py", 
    f"src/{project_name}/constants/__init__.py", 
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
]

for file in list_files:
    filepath = Path(file)
    filedir , filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory '{filedir}' for the file '{filename}'")
    if (not os.path.exists(filepath)) or os.path.getsize(filepath)== 0:
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty File '{filepath}'")
    else:
        logging.info(f"{filename} already exists")


    
