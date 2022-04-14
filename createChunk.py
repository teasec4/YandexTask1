import pandas as pd

# Разбиение на Чанки

source_path='pp-complete (1).csv'

for i, chunk in enumerate(pd.read_csv(source_path, chunksize=100000,
                                      names=['Transaction unique identifier',
                                             'Price', 'Date of Transfer', 'Postcode',
                                             'Property Type', 'Old/New', 'Duration',
                                             'PAON', 'SAON', 'Street', 'Locality',
                                             'Town/City', 'District', 'Country',
                                             'PPD Category Type', 'Record Status-monthly file only']
                                      )):
    df = pd.DataFrame(data=chunk)
    df['Uniq Adress'] = df['Street'] + ' ' + df['PAON'] + ' ' + df['Country']
    df1 = df.filter(['Uniq Adress', 'Price'], axis=1)
    df1.to_csv('chunk/df{0}.csv'.format(i), index=False)

