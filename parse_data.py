from bs4 import BeautifulSoup
import os
import re

DATA_FOLDER = "data/html"
OUTPUT_FOLDER = "data/"

with open(os.path.join(OUTPUT_FOLDER, "corpus.txt"), 'w') as output:
    for f_name in os.listdir(DATA_FOLDER):
        if f_name.split('.')[-1] != 'html':
            continue
        with open(os.path.join(DATA_FOLDER, f_name), 'r') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            output_name = f_name[:-5] + '.txt'
            subs = soup.find_all('h2')
            feiten = []
            for sub in subs:
                if sub.find(string=re.compile('feiten')):
                    feiten.append(sub)
            for feit in feiten:
                text = "".join([sub for sub in feit.parent.get_text().split('\n') if sub.strip() != ""])
                text += '\n\n'
                output.write(text)
