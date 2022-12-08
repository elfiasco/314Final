import requests
from bs4 import BeautifulSoup
import datetime
from datetime import date, timedelta
import pandas as pd
import time


url = "https://raw.githubusercontent.com/elfiasco/314Final/main/clean_data.csv"
big_data = pd.read_csv(url, index_col=0)
# print(big_data.head())

format = '%m/%d/%Y'  # The format
##7 1 2022
july_1 = datetime.datetime(2022, 7, 1)

def biographicalInfo(player_id):
    url = 'https://www.mlb.com/player/'+str(player_id)
    page = requests.get(url)
    html = BeautifulSoup(page.text, "html.parser")
    data = html.find("ul").get_text(' ').replace(' ', '').splitlines( )

    throw_hand=(data[2][-1])
    weight = int(data[3].split('/')[1])
    height_feet_and_inches = (data[3].split('/')[0].replace('"', '').split("'"))
    height=int(height_feet_and_inches[0])*12+int(height_feet_and_inches[1])
    ##Get Birthday
    table = html.find("div", {"class": "player-bio"})
    s = ""
    l = table.findAll("li")
    
    for d in l:
        
        s=s+(d.get_text(' ').replace(' ', ''))
        
    name = (s.split('Fullname:')[1].split('Nickname')[0].split('Born')[0])
    birth_date=(s.split('Born:')[1].splitlines( )[0])
    birth_date = (july_1-datetime.datetime.strptime(birth_date, format)).days/365.25
    return [player_id, name, throw_hand, height, weight, birth_date]


unique_ids = big_data["pitcher"].unique()
df = pd.DataFrame(columns=["pitcher", "name", "throw_hand", "height", "weight", "age_on_july_1"])


start_time = time.time()

for i in range(len(unique_ids)):
    df.loc[len(df.index)] = biographicalInfo(unique_ids[i])
    print(str(i+1)+" out of "+str(len(unique_ids))+str("  --- %s seconds ---" % (time.time() - start_time)))

grouped_multiple = big_data.groupby('pitcher').agg({'release_speed': 'mean', 'release_pos_x': 'mean', 'release_pos_z': 'mean', 'pfx_x': 'mean', 'pfx_z': 'mean', 'release_spin_rate': 'mean', 'release_extension': 'mean', 'spin_axis': 'mean', 'swinging_strike': 'mean'})
grouped_multiple = grouped_multiple.reset_index()
df_cd = pd.merge(grouped_multiple, df, on='pitcher')
df_cd.to_csv('pitchers.csv')

print(grouped_multiple.head())
