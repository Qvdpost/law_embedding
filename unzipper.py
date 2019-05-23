import zipfile
import os

DATA_FOLDER = "data_dump/"

for folder in os.listdir(DATA_FOLDER):
    for f_name in os.listdir(os.path.join(DATA_FOLDER, folder)):
        if f_name.split('.')[-1] == 'zip':
            print(f_name)
            zip_ref = zipfile.ZipFile(os.path.join(DATA_FOLDER, folder, f_name), 'r')
            zip_ref.extractall("xml_dump")
            zip_ref.close()
