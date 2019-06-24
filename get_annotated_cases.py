from bs4 import BeautifulSoup
import urllib.request as request
import urllib.error as url_error
import csv
import os


with open('annotated_data/kanton_cases.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        case = line[0]
        if os.path.exists(f"annotated_data/cases/{case}.html"):
            print("duplicate: ", case)
            continue
        if "".join(case[0:2]) == "AR":
            case = "_".join(["AR", "".join(case[2:6]), case[-4:]])
            url = f"https://www.ar-updates.nl/samenvatting/{case}"
        else:
            url = f"https://uitspraken.rechtspraak.nl/inziendocument?id={case}"
        try:
            contents = request.urlopen(url).read()
        except url_error.HTTPError:
            print("Case not found: ", case)
            continue
        soup = BeautifulSoup(contents, 'html.parser')
        text = soup.find(id='Main')
        with open(f"annotated_data/cases/{case}.html", 'w') as output:
            output.write(str(text))
