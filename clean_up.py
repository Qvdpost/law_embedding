import os
import shutil


DATA_FOLDER = "data/cases"

for year in range(1913, 1981):
    folder = os.path.join(DATA_FOLDER, str(year))
    if os.path.exists(folder):
        print(folder, 'is being deleted')
        shutil.rmtree(folder)
