import pandas as pd

source_path = "pp-complete (1).csv"
chunksize = 500000

for i, chunk in enumerate(pd.read_csv(source_path, chunksize=chunksize,
                                      names=['Transaction unique identifier',
                                             'Price', 'Date of Transfer', 'Postcode',
                                             'Property Type', 'Old/New', 'Duration',
                                             'PAON', 'SAON', 'Street', 'Locality',
                                             'Town/City', 'District', 'Country',
                                             'PPD Category Type', 'Record Status-monthly file only']
                                      )):
 df = pd.DataFrame(data=chunk)
 df['Uniq Adress'] = df['Street'] + ' ' + df['PAON']
 df2 = df.groupby('Uniq Adress').sum()
 df1 = df.filter(['Uniq Adress', 'Price'], axis=1)
 df2 = df2.filter(['Uniq Adress', 'Price'], axis=1)
 df2.reset_index(inplace=True)  # выравниваем таблицы
 df_diff = pd.concat([df1, df2]).drop_duplicates(keep=False)
 print('New chunk {0}'.format(i))
 print(df_diff['Uniq Adress'])
 df_diff.to_csv('resault/resault{0}'.format(i))



