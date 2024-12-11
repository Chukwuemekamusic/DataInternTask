import pandas as pd
from utils import month_order

file_name = 'email_metrics.csv'
df = pd.read_csv(file_name)

df = df.melt(id_vars=['Month', 'Year'], value_vars=['Av. Click Through Rate', 'Average Open Rate', 'No. of emails sent'], var_name='Metric', value_name='Value')
# # Correct the month abbreviation for September
# df['Month'] = df['Month'].replace({'Sept': 'Sep'})

# create a date column for date-time plotting
df['Date'] = pd.to_datetime(df['Month'] + ' 28 ' + df['Year'].astype(str))

df['Month'] = pd.Categorical(df['Month'], categories=month_order.keys(), ordered=True)
df = df.sort_values(['Year', 'Month'], ignore_index=True)

df.to_csv('transformed/email_metrics_transformed.csv', index=False)

print(df)