import os
import pandas as pd

files = [file for file in os.listdir('./resault')]
#merging data
all_data = pd.DataFrame()
for file in files:
    df = pd.read_csv('./resault/' + file)
    all_data = pd.concat([all_data, df])

all_data.to_csv('all_data.csv', index=False)