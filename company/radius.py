import pandas as pd
import os
import glob
  
  
# use glob to get all the csv files
# in the folder
path = os.getcwd()
csv_files = glob.glob(("RADIUS2021"+ "/*.xlsx"))

frames = []

for f in csv_files:
  # read by default 1st sheet of an excel file

  print("""
  
  """)
  print(f)

  df = pd.read_excel(f)
  print(df)
#   remove_first_row = df.iloc[5:]
#   new_column_names = remove_first_row.rename(columns=df.iloc[4])


  print("""
  
  """)

#   print( new_column_names)
#   df.drop(df.index[0], inplace=True)
#   frames.append(remove_blanks)



# print("""

# ________

# """)

# result = pd.concat(frames, ignore_index=True)


# result.to_csv("glenraig combined.csv", index=False)

# # result.rename(columns={"DATE ": "date", "BUILDING ": "building", "LOCATION ": "location", "MAKE ": "make", "TEMP ": "temp" }, inplace=True)
# print(result)

# building_group = result.groupby('building')
# buildings_with_items = building_group.apply(lambda x: x['location'].unique())





# print(buildings_with_items)