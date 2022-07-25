


import gspread
import pandas as pd
import time
import datetime
import base64
import yaml
from PIL import Image



gc = gspread.service_account(filename='./cred.json')
sheet1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1iudlYSDTvHLjEa0q04ebYmVnb8cV1xD7qJMUBj0rxFs/edit?usp=sharing')
sh = sheet1.get_worksheet(0)
df_gsheet = pd.DataFrame(data=sh.get_all_records())


with open('./questions.yaml') as file:
    qconfig = yaml.safe_load(file)


#ask for week to run
#get list of questions and their answers and points
#for each row that is for that week and question, check if choice is in correct answer array, record points

week = input("Enter the week you want to add points to: ")

for i, row in df_gsheet.iterrows():
    if int(week) == int(row["Week"]):
        print('write')
        if str(row["Choice"]) in qconfig["weeks"][week]["bets"][str(row["Question"])]["correctanswer"]:
            sh.update_cell(i+2,5,qconfig["weeks"][week]["bets"][str(row["Question"])]["points"])
        else:
            sh.update_cell(i+2,5,0)
        time.sleep(2)
        if i%20 == 19:
            print('wait')
            time.sleep(20)
