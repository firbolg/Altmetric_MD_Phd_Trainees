#import urllib
import urllib.request
from urllib.error import HTTPError
import json 
import csv
import pandas as pd
import os 
from functools import reduce 

# Read xlsx file
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

path = r"C:\Users\Levi\source\repos\Altmetric_MD_PhD_Trainees\json_data"

os.chdir(path)

dflist = []

for file in os.listdir():
    file_path = f"{path}\{file}"
    with open(file_path, "r") as f:
        data = json.loads(f.read())
        df_flat = pd.json_normalize(data)
        dflist.append(df_flat)

# TODO merge list of dataframes with NaN values retained
#df = reduce(lambda x, y: pd.merge(x, y, on = 'doi'), dflist)    
# https://stackoverflow.com/questions/38089010/merge-a-list-of-pandas-dataframes/38089112    
# TODO match normalized json dataframe rows to dataframe of original csv by identifier and merge
# TODO output final xlsx with all info 

