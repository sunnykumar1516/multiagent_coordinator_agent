import os
from pathlib import Path
import logging

PROJECTNAME = "AI_AGENT_RESUME_SELECTOR"
list_files =[
    ".github/workflows/.gitkeep",
    f"src/{PROJECTNAME}/__init__.py",
    f"src/{PROJECTNAME}/components/__init__.py",
    f"src/{PROJECTNAME}/utilities/__init__.py",
    f"src/{PROJECTNAME}/utilities/common.py",
    f"src/{PROJECTNAME}/configurations/__init__.py",
    f"src/{PROJECTNAME}/configurations/config.py",
    f"src/{PROJECTNAME}/entity/__init__.py",
    f"src/{PROJECTNAME}/entity/projectEntity.py",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "research/research.ipynb",
    "data/raw/__init__.py",
    "data/cleaned/__init__.py"
]

for filepath in list_files:
    filepath = Path(filepath)
    dir,filename = os.path.split(filepath)
    if dir!= "":
        os.makedirs(dir,exist_ok=True)
        logging.info(f">>>>>> creating directory {dir}")
    if (not os.path.exists(filepath) ) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f">>>>>> creating file {filepath}")
