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
 df['Uniq Adress'] = df['Street'] + ' ' + df['PAON'] + ' ' +df['Locality']
 df2 = df.groupby('Uniq Adress').sum(['Price']) # новая таблица с суммами
 df1 = df.filter(['Uniq Adress', 'Price'], axis=1)
 df2 = df2.filter(['Uniq Adress', 'Price'], axis=1)
 df2.reset_index(inplace=True)  # добавим индекс - выравниваем таблицы
 #df_diff = pd.concat([df1, df2]).drop_duplicates(keep=False)

 resault = df2.merge(df1[['Uniq Adress', 'Price']], how='outer',
                     on='Uniq Adress')

 resault['compare'] = resault['Price_x'] != ['Price_y']

 answer = resault.loc[resault['compare'] == True]
 a = answer.dropna(how='any')
 b = a.drop_duplicates(subset=['Uniq Adress'])

 print('New chunk {0}'.format(i))
 print(b['Uniq Adress'])
 b.to_csv('resault/resault{0}.csv'.format(i))



