import pandas as pd
from utils import month_order

file_name = 'social_metrics.csv'
df = pd.read_csv(file_name)

df = df.melt(id_vars=['Month', 'Year'], value_vars=['Net Follower Growth', 'Number of Followers', 'Total Engagement', 'Total Impressions', 'Total Video Views'], var_name='Metric', value_name='Value')

# create a date column for date-time plotting
df['Date'] = pd.to_datetime(df['Month'] + ' 28 ' + df['Year'].astype(str))

df['Month'] = pd.Categorical(df['Month'], categories=month_order.keys(), ordered=True)
df = df.sort_values(['Year', 'Month'], ignore_index=True)

df.to_csv('transformed/social_metrics_transformed.csv', index=False)

print(df)