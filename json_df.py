import pandas as pd
import os 
import json 

path = r"C:\Users\dolanl\Projects\Altmetric_MD_PhD_Trainees\json_data"

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

# Read xlsx file into dataframe
#df = pd.read_excel('m_test.xlsx')
#dfs = [df.set_index('doi') for df in dflist]

#works
#a = dflist[0]
#b = dflist[1]
#test = pd.concat([a,b], sort=False)

#all_df = pd.concat(dflist, ignore_index=True)

#works but with 0 in each cell 
all_df = pd.DataFrame.from_dict(map(dict,dflist))
writer = pd.ExcelWriter('output.xlsx')

all_df.to_excel(writer, index=False)

writer.save()
print(all_df)
