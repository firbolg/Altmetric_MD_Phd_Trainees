import urllib.request
from urllib.error import HTTPError
import json 
import csv
import pandas as pd


# Read xlsx file into dataframe
df = pd.read_excel('m_test.xlsx')


# Enumerate through the DOIs, getting all open Altmetric data for each article as json objects, 
# writing each json object to a file, and incrementing the filename by 1 each loop.
e = 0

def get_json(doi):
    try:
        url = ('https://api.altmetric.com/v1/doi/' + doi)
        json_obj = urllib.request.urlopen(url)
        data = json.load(json_obj)
        with open('{0}_altmetric_data.json'.format(e), 'w') as jsonfile:
            json.dump(data, jsonfile)
    except HTTPError as err:
        if err.code == 404:
            pass
        else:
            raise 


doi_list = df['DOI'].tolist()

for i in doi_list:
    get_json(i)
    e+=1
