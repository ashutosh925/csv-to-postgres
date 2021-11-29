# import OS module
import os
import pandas as pd
# print("\nWe are listing out only the directories in current directory -")s
companyFolder = list(filter(os.path.isdir, os.listdir(os.curdir)))
# print(directories)

# for company in companyFolder:
#     buildings = os.listdir(company)
#     for building in buildings:
#         if(os.path.isdir(company+"/"+building)):
#             locations = os.listdir(company + "/" +building + "/")
#             for location in locations:
#                 print(company + "/" +building + "/"+location)
                # current_execel = pd.read_excel(company + "/" +building + "/"+location,engine='openpyxl')
                # print(current_execel.head(1))