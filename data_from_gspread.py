import gspread as gs
import pandas as pd

# python_key.json is the same key for all shared files with the IAM user.
gc = gs.service_account(filename='python_key.json')


# new sheets are added on with different gsheets ID's
sh1 = gc.open_by_key('1AkmronHQmdAfpOTwS8MLHGwje9piovifUaddOOnWfZg')
sh2 = gc.open_by_key('1uBI4lewtubaJ5Qg1pKPIUAt8WGJMdJ94Ls_bKZWpLzs')
sh3 = gc.open_by_key('1_canBLlCjw7vwCQmFvBN_Vw9X8Io-X8wWZAHpX2B1kk')
sh4 = gc.open_by_key('1xbyoVL-_QhDf2RbAXVhs9u5vhFRIoXCNlVKKE6DPgLM')
sh5 = gc.open_by_key('18lsuVQXnaK1JMNV8ic3efkgKK2mLw8vBawoxs-6KlEM')
sh6 = gc.open_by_key('1cRt0hUm56iZt2bl4-74R6VbYxp32EANaiqDf6mWQYDw')


# name the sheets here.
ws1 = sh1.worksheet('Centro')
ws2 = sh2.worksheet('Segovia')
ws3 = sh3.worksheet('Patria')
ws4 = sh4.worksheet('Pasaje')
ws5 = sh5.worksheet('Vallardo')
ws6 = sh6.worksheet('VA_en_linea')


# named sheets below with each "ws_" from above will go get all records as python dictionary
Centro = pd.DataFrame(ws1.get_all_records())
Segovia = pd.DataFrame(ws2.get_all_records())
Patria = pd.DataFrame(ws3.get_all_records())
Pasaje = pd.DataFrame(ws4.get_all_records())
Vallardo = pd.DataFrame(ws5.get_all_records())
VA_en_linea = pd.DataFrame(ws6.get_all_records())

frames = [Centro, Segovia, Patria, Pasaje, Vallardo, VA_en_linea]

print(frames)