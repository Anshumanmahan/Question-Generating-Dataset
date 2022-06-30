import pandas as pd
df = pd.read_parquet('/N/u/anshdixi/Carbonate/Sherlock/sherlock-project-master/data/data/raw/train_labels.parquet', engine='pyarrow')

df.reset_index(inplace = True)
x = df[df['type'] == 'birth Date']
li = x['index'].tolist()

df1 = pd.read_parquet('/N/u/anshdixi/Carbonate/Sherlock/sherlock-project-master/data/data/raw/train_values.parquet', engine='pyarrow')
#for i in df['values']:
#    print(i)

#print(df[df['type'] == 'day'])
df1.reset_index(inplace = True)

import time

for i in li:
    print(df1[df1['index'] == i])
    time.sleep(0.5)
