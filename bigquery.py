import pandas as pd
from pandas.io import gbq

query = """SELECT * FROM `source-data-314320.Store_Data.All_Data`"""
All_Data = gbq.read_gbq(query, project_id = "source-data-314320")
print(All_Data)