#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime, timedelta, timezone
now = datetime.now()
print('---- EXECUTION STARTED at '+ str(now))

import pymysql
pymysql.install_as_MySQLdb()
import pandas as pd
from PIL import Image
import json

import subprocess
import numpy as np
from sqlalchemy import create_engine
import sys
from time import time
import sqlalchemy as sa



# In[261]:


# Import file names
file_names = pd.read_csv("XXX.csv", usecols=["Variable", "File"]) ## Attention to capital letters vs the files and sequence in form
file_names_list = file_names.to_dict('split')["data"]
file_names_dict = {k[0]: k[1:][0] for k in file_names_list}


# In[269]:



## Import beta testers


df_beta = pd.read_csv("XXX.csv", header=0)

df_beta_twitter = df_beta['q_1'].str.replace("@", "")


## SQL connection
pymysql.install_as_MySQLdb()

## SQL connection
conn2=pymysql.connect(host='XXX', password='XXX',port=int(3306),user='XXX',db='XXX')
cursor2 = conn2.cursor()

## Get individuation records
df_updates = pd.read_sql_query("SELECT * FROM XXX ",con=conn2)
df_updates = df_updates.sort_values(by=["iid", "date"], ascending=False)
df_updates = df_updates.drop_duplicates(subset=["iid"], keep='first')

if len(df_updates) == 1:
    update_list = "(" + str(tuple(df_updates['iid'].values)[0]) + ")"
    print(update_list)
    df_s=pd.read_sql_query("SELECT * FROM XXX WHERE iid in" + update_list,con=conn2)
    df_s = df_s.set_index('iid')
elif len(df_updates) > 1:
    update_list = str(tuple(df_updates['iid']))
    print(update_list)
    df_s=pd.read_sql_query("SELECT * FROM XXX WHERE iid in" + update_list,con=conn2)
    df_s = df_s.set_index('iid')
else:
    sys.exit("----------NO SOUL TO GENERATE")


## Close connection
conn2.close()

print(df_updates)

df_s = df_s.dropna(subset=['soul_1', 'soul_2'])
df_latest = df_s.copy()

df_latest['beta'] = np.nan
df_latest.loc[df_latest['twitter_name'].isin(df_beta_twitter), 'beta'] = 'True'



# Create dataframe with all 8 traits in sequence
dict_ind = {}
list_ind = []
sub = str(int(time()))


for i in range(len(df_latest)):
 dict_ind = {}
 dict_ind[1] = df_latest.iloc[i]['soul_1'].replace("_", " ").title()
 dict_ind[2] = df_latest.iloc[i]['soul_2'].replace("_", " ").title()
 dict_ind[3] = df_latest.iloc[i]['soul_3'].replace("_", " ").title()
 dict_ind[4] = df_latest.iloc[i]['soul_4'].replace("_", " ").title()
 dict_ind[5] = df_latest.iloc[i]['soul_5'].replace("_", " ").title()
 dict_ind[6] = df_latest.iloc[i]['soul_6'].replace("_", " ").title()
 dict_ind[7] = df_latest.iloc[i]['soul_7'].replace("_", " ").title()
 dict_ind[8] = df_latest.iloc[i]['soul_8'].replace("_", " ").title()
 dict_ind[9] = df_latest.iloc[i]['soul_9'].replace("_", " ").title()
 dict_ind[10] = df_latest.iloc[i]['soul_10'].replace("_", " ").title()
 dict_ind[11] = df_latest.iloc[i]['soul_11'].replace("_", " ").title()
 dict_ind[12] = df_latest.iloc[i]['soul_12'].replace("_", " ").title()
 dict_ind['Archetype'] = df_latest.iloc[i]['archetype'].replace("_", " ").title()
 dict_ind['TokenID'] = df_latest.iloc[i]['soul_id'].astype('int32')
 dict_ind['Type'] = df_latest.iloc[i]['soul_type'].astype('int32')
 dict_ind['Beta'] = df_latest.iloc[i]['beta']
 dict_ind['file_name'] = str(df_latest.iloc[i]['soul_id'].astype('int32')) + "_" + sub
 list_ind.append(dict_ind)

print(df_latest)
print(list_ind)
if len(list_ind)>0:
    soul_image = pd.DataFrame(list_ind)[['TokenID', 'Type', 'file_name']]
    soul_image.columns = ['soul_id', 'soul_type', 'file_name']
    print(soul_image)
else:
    soul_image = pd.DataFrame()


#### Generate Images

for item in list_ind:


## Add other layers:
    imbg = Image.open(f'/home/sumusic/trait_layers/background/bg.png').convert('RGBA')
    imc = Image.open(f'/home/sumusic/trait_layers/position_C/{file_names_dict["C_"+item["Archetype"]]}.png').convert('RGBA')
    im1 = Image.open(f'/home/sumusic/trait_layers/position_1/{file_names_dict["1_"+item[1]]}.png').convert('RGBA')
    im2 = Image.open(f'/home/sumusic/trait_layers/position_2/{file_names_dict["2_"+item[2]]}.png').convert('RGBA')
    im3 = Image.open(f'/home/sumusic/trait_layers/position_3/{file_names_dict["3_"+item[3]]}.png').convert('RGBA')
    im4 = Image.open(f'/home/sumusic/trait_layers/position_4/{file_names_dict["4_"+item[4]]}.png').convert('RGBA')
    im5 = Image.open(f'/home/sumusic/trait_layers/position_5/{file_names_dict["5_"+item[5]]}.png').convert('RGBA')
    im6 = Image.open(f'/home/sumusic/trait_layers/position_6/{file_names_dict["6_"+item[6]]}.png').convert('RGBA')
    im7 = Image.open(f'/home/sumusic/trait_layers/position_7/{file_names_dict["7_"+item[7]]}.png').convert('RGBA')
    im8 = Image.open(f'/home/sumusic/trait_layers/position_8/{file_names_dict["8_"+item[8]]}.png').convert('RGBA')




    #Create each composite
    com1 = Image.alpha_composite(imbg, imc)
    com2 = Image.alpha_composite(com1, im1)
    com3 = Image.alpha_composite(com2, im2)
    com4 = Image.alpha_composite(com3, im3)
    com5 = Image.alpha_composite(com4, im4)
    com6 = Image.alpha_composite(com5, im5)
    com7 = Image.alpha_composite(com6, im6)
    com8 = Image.alpha_composite(com7, im7)
    com9 = Image.alpha_composite(com8, im8)



    #Convert to RGB
    rgb_im = com9.convert('RGBA')
    file_name = str(item["TokenID"]) + ".png"
    rgb_im.save("XXX" + file_name)
    subprocess.call("mv XXX" + file_name + " XXX", shell=True)
    subprocess.call("cp XXX" + file_name + " XXX" + str(item["file_name"]) + ".png", shell=True)
#### Generate metadata

IMAGES_BASE_URI = "https://XXX"
PROJECT_NAME = "SOUL"


def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in list_ind:
    token_id = str(i['TokenID'])
    token = {
      "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' #' + str(token_id),
        "description": "NYX Soulmate is an experiment utilizing game theory, a proprietary AI and hard science to make introductions in web3 based on who people are, not how they look. Soul NFTs are unique representations of who you are. The chances of two Souls being the same is 1 in 7,194,667,451,811,840,000.",
        "attributes": []
    }

    #if i['Type'] == 1:
    #    token["attributes"].append(getAttribute("Soul Type", "Genesis"))
    #elif i['Type'] == 2:
    #    token["attributes"].append(getAttribute("Soul Type", "Lite"))
    token["attributes"].append(getAttribute("State", "Soulbind"))
    if (i['TokenID'] <= 308) and (i['TokenID'] not in [81, 130]):
        token["attributes"].append(getAttribute("Soul Type", "Genesis"))
        token["attributes"].append(getAttribute("Ferry", "Oblivion"))
    token["attributes"].append(getAttribute("Main Kind", i["Archetype"]))
    token["attributes"].append(getAttribute("1", i[1]))
    token["attributes"].append(getAttribute("2", i[2]))
    token["attributes"].append(getAttribute("3", i[3]))
    token["attributes"].append(getAttribute("4", i[4]))
    token["attributes"].append(getAttribute("5", i[5]))
    token["attributes"].append(getAttribute("6", i[6]))
    token["attributes"].append(getAttribute("7", i[7]))
    token["attributes"].append(getAttribute("8", i[8]))
    token["attributes"].append(getAttribute("9", i[9]))
    token["attributes"].append(getAttribute("10", i[10]))
    token["attributes"].append(getAttribute("11", i[11]))
    token["attributes"].append(getAttribute("12", i[12]))
    if i['Beta'] == 'True':
        token["attributes"].append(getAttribute("Beta", i['Beta']))


    with open('XXX' + str(token_id) + '.json', 'w', encoding='utf8') as outfile:
        json.dump(token, outfile, indent=4, ensure_ascii=False)
    subprocess.call("mv XXX" + str(token_id) + ".json" + " XXX", shell=True)

    import time
    time.sleep(2)

## in opensea prod
    subprocess.call("curl https://api.opensea.io/asset/XXX"+  str(token_id) + "/?force_update=true", shell=True)

## in test
    # subprocess.call("curl https://testnets-api.opensea.io/api/v1/asset/XXX"+  str(token_id) + "/?force_update=true", shell=True)


### DELETE AUX TABLE

## Delete rows from aux_indiv_trigger table
conn2=pymysql.connect(host='XXX', password='XXX',port=int(3306),user='XXX',db='XXX')
cursor2 = conn2.cursor()

for i in list(df_updates.index):
    iid_i = "'" + str(df_updates.loc[i, 'iid']) + "'"
    date_i = "'" + str(df_updates.loc[i, 'date']) + "'"
    sql = "DELETE FROM XXX WHERE iid = " + iid_i + " AND date = " + date_i
    cursor2.execute(sql)
    conn2.commit()

conn2.close()


db_name="XXX"
db_user="XXX"
db_pwd="XXX"
db_host="XXX"
db_client="XXX"

db_data = sa.engine.URL.create(
    drivername=db_client,
    username=db_user,
    password=db_pwd,
    host=db_host,
    database=db_name)

engine = create_engine(db_data)

if not soul_image.empty:
    soul_image.to_sql(name='XXX', con=engine, if_exists='append', index=False)

engine.dispose()


now = datetime.now()
print('---- EXECUTION FINISHED at '+ str(now))
