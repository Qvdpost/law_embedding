from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import string


def format_filename(s):
    """Take a string and return a valid filename constructed from the string.
    Uses a whitelist approach: any characters not present in valid_chars are
    removed. Also spaces are replaced with underscores.

    Note: this method may produce invalid filenames such as ``, `.` or `..`
    When I use this method I prepend a date string like '2009_01_15_19_46_32_'
    and append a file extension like '.txt', so I avoid the potential of using
    an invalid filename.

    """
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    # filename = ''.join(c for c in s if c in valid_chars)
    filename = ''.join(c if c in valid_chars else '.' for c in s)
    filename = filename.replace(' ', '_')
    return filename

driver = webdriver.Firefox()
root_handle = driver.current_window_handle
wait = WebDriverWait(driver, 3)

driver.get("https://uitspraken.rechtspraak.nl/#zoekverfijn/idx=1&so=Relevance&ps[]=ps1&cs[]=cs1&rg[]=r15")

print("Getting items:")
button = driver.find_element_by_id("laadmeer")
while button.get_attribute('style') != "display: none;":
    button = driver.find_element_by_id("laadmeer")
    try:
        element = wait.until(EC.element_to_be_clickable((By.ID, 'laadmeer')))
        element.click()
    except:
        continue

items = driver.find_elements_by_class_name("zoekresultaatItem")
print(f"Processing {len(items)} items:")
for counter, item in enumerate(items):
    button = driver.find_element_by_id("laadmeer")
    titel_div = item.find_element_by_class_name("titel")
    link = titel_div.get_attribute('href')
    titel = titel_div.get_attribute('title')
    print(f"Item {counter}: {titel}")
    request = requests.get(link)
    with open(f"data/html/{format_filename(titel)}.html", "w") as f:
        f.write(request.text)
