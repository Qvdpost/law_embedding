import zipfile
from bs4 import BeautifulSoup
import os
import re

DATA_FOLDER = "data/cases"
OUTPUT_FOLDER = "data/txt_cases"
TEMP = "data/tmp"

for folder in os.listdir(DATA_FOLDER):
    for f_name in os.listdir(os.path.join(DATA_FOLDER, folder)):
        if f_name.split('.')[-1] == 'zip':
            print(f_name)
            zip_ref = zipfile.ZipFile(os.path.join(
                DATA_FOLDER, folder, f_name), 'r')
            zip_ref.extractall(TEMP)
            zip_ref.close()

        for xml in os.listdir(TEMP):
            # output = f_name.split('.')[0] + ".txt"  # for annotated cases
            clean_f_name = xml.split('.')[0]
            clean_f_name = ":".join(clean_f_name.split('_'))
            output = clean_f_name + ".txt"

            if os.path.exists(os.path.join(OUTPUT_FOLDER, output)):
                print(xml, "already exists")
            else:
                with open(os.path.join(TEMP, xml), 'r') as f:
                    if xml.split('.')[-1] != 'xml':
                        continue
                    print(f"Parsing {xml}")

                    soup = BeautifulSoup(f.read(), 'lxml')
                    subs = soup.find_all('uitspraak')

                    if subs:
                        with open(os.path.join(OUTPUT_FOLDER, output), 'w') as output:
                            for feit in subs:
                                text = "".join(
                                    [sub for sub in feit.get_text().split('\n') if sub.strip() != ""])
                                text += '\n\n'

                                output.write(text)

            os.remove(os.path.join(TEMP, xml))
