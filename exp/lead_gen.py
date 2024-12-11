import pandas as pd
from utils import month_order

file_name = 'lead_gen_metrics.csv'
df = pd.read_csv(file_name)

df['Total Leads'] = df.iloc[:, 2:].sum(axis=1)

# Add cumulative leads
df['Cumulative Leads'] = df['Total Leads'].cumsum()

# create a date column for date-time plotting
df['Date'] = pd.to_datetime(df['Month'] + ' 28 ' + df['Year'].astype(str))

df['Month'] = pd.Categorical(df['Month'], categories=month_order.keys(), ordered=True)
df = df.sort_values(['Year', 'Month'], ignore_index=True)

# df.to_csv('transformed_wide/lead_gen_metrics.csv', index=False)

print(df)