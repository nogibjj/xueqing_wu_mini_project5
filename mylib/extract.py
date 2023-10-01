"""
Extract a dataset from a URL like Kaggle or data.gov. 
JSON or CSV formats tend to work well
food dataset
"""
import requests
import os

def extract(url=
            "https://github.com/fivethirtyeight/data/blob/master/births/US_births_2000-2014_SSA.csv?raw=true ", 
             # Add ?raw=true so only run the csv not the html
            file_path="data/US_births_2000-2014_SSA.csv", 
            # when data come into "data" directory, save as US_births_2000-2014_SSA.csv
            directory="data"):
             # where to put the data when the github data come in
    """"Extract a url to a file path"""


    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path



