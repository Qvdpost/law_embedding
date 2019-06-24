from bs4 import BeautifulSoup
import os
import re

DATA_FOLDER = "data/cases"
OUTPUT_FOLDER = "data/txt_cases"


with open('annotated_data/no_facts.txt', 'w') as errors:
    for f_name in os.listdir(DATA_FOLDER):
        # output = f_name.split('.')[0] + ".txt"  # for annotated cases
        clean_f_name = f_name.split('_')[0]
        clean_f_name = ":".join(clean_f_name.split('.'))
        output = clean_f_name + ".txt"
        if os.path.exists(os.path.join(DATA_FOLDER, output)):
            continue
        with open(os.path.join(DATA_FOLDER, f_name), 'r') as f:

            if f_name.split('.')[-1] != 'html':
                continue
            print(f"Parsing {f_name}")

            soup = BeautifulSoup(f.read(), 'html.parser')
            output_name = f_name[:-5] + '.txt'
            subs = soup.find_all('h2')
            feiten = []
            for sub in subs:
                if sub.find(string=re.compile('feiten', re.IGNORECASE)):
                    feiten.append(sub)

            if not feiten:
                for sub in subs:
                    if sub.find(string=re.compile('geding', re.IGNORECASE)):
                        feiten.append(sub)

            if feiten:
                with open(os.path.join(OUTPUT_FOLDER, output), 'w') as output:
                    for feit in feiten:
                        text = "".join(
                            [sub for sub in feit.parent.get_text().split('\n') if sub.strip() != ""])
                        text += '\n\n'

                        output.write(text)
            else:
                errors.write(f_name + "\n")
