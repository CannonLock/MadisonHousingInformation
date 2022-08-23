import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

# I could not get the jupyter module working so imagine this like it is kinda a Jupyter Notebook

# This is where I grab the data from the DOR website

def grab_data():
    DOMAIN = "https://www.revenue.wi.gov"

    response = requests.get("https://www.revenue.wi.gov/pages/eretr/data-home.aspx")
    soup = BeautifulSoup(response.text)

    for section in soup.find_all(class_="dorContentPadding"):
        for a_tag in section.find_all('a'):

            file_url = urljoin(DOMAIN, a_tag.attrs['href'])

            data_response = requests.get(file_url)

            with open(f"./data/{os.path.basename(file_url)}", "wb") as fp:
                fp.write(data_response.content)

# Unzip all the files

def unzip_data():

    for zipfile_path in glob.glob("./data/*.zip"):

        with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
            zip_ref.extractall("./data/unzipped")

unzip_data()