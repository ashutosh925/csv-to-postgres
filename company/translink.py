import pandas as pd
import os
import glob
import pprint
  
# use glob to get all the csv files
# in the folder
path = os.getcwd()
csv_files = glob.glob(("TRANSLINK2021"+ "/*.xlsx"))

frames = []

for f in csv_files:
  # read by default 1st sheet of an excel file
  df = pd.read_excel(f)

  remove_first_row = df.iloc[1: , :-1]

  new_column_names = remove_first_row.rename(columns=df.iloc[1]).iloc[1: , :]
  df.drop(df.index[0], inplace=True)
  frames.append(new_column_names.dropna())
  print("""
  
  """)
  print(new_column_names.dropna())


result = pd.concat(frames, ignore_index=True)

result.rename(columns={"DATE ": "date", "BUILDING ": "building", "LOCATION ": "location", "MAKE ": "make", "TEMP ": "temp" }, inplace=True)
# print(result)

building_group = result.groupby('building')
buildings_with_items = building_group.apply(lambda x: x['location'].unique())

for col in df:
    print(result[col].unique())
    print("""
  
    """)


# df_buildings = {building: result[result['building'] == building] for building in result['building'].unique()}
# dict_of_companies = dict(tuple(result.groupby("building")))

# pprint.pprint(dict_of_companies)
# for x in buildings_with_items: 
#   print(x)
#   print("""
  
  
#   """)