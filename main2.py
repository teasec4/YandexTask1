import pandas as pd

source_path = "all_data.csv"
data = pd.read_csv(source_path)
df = pd.DataFrame(data=data)


df2 = df.groupby('Uniq Adress').sum(['Price'])  # новая таблица с суммами
df2.reset_index(inplace=True)  # добавим индекс - выравниваем таблицы

resault = df2.merge(df[['Uniq Adress', 'Price']], how='outer',
                    on='Uniq Adress')

resault['compare'] = resault['Price_x'] != resault['Price_y']

answer = resault.loc[resault['compare'] == True]
a = answer.dropna(how='any')
b = a.drop_duplicates(subset=['Uniq Adress'])

b['Uniq Adress'].to_csv('final.csv')
