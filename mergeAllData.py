import os
import pandas as pd

files = [file for file in os.listdir('./chunk')]
#merging data
all_data = pd.DataFrame()
for file in files:
    df = pd.read_csv('./chunk/' + file)
    all_data = pd.concat([all_data, df])

#drop NAN
all_data = all_data.dropna(how='any')
all_data.to_csv('all_data.csv', index=False)