import pandas as pd

# Разбиение на Чанки

source_path='pp-complete (1).csv'

for i, chunk in enumerate(pd.read_csv(source_path, chunksize=10000)):
    chunk.to_csv('chunk/chunk{0}.csv'.format(i), index=False)

