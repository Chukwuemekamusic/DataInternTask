import pandas as pd
from utils import month_order

file_name = 'lead_gen_metrics.csv'
df = pd.read_csv(file_name)

df = df.melt(id_vars=['Month', 'Year'], value_vars=['Linktree', 'Many Chat', 'Podcast', 'Direct from Website', 'Social ads', 'Affiliates'], var_name='Source', value_name='Growth')

df['Month'] = pd.Categorical(df['Month'], categories=month_order.keys(), ordered=True)
df = df.sort_values(['Year', 'Month'])

df.to_csv('transformed/lead_gen_metrics_transformed.csv', index=False)

print(df)