import pandas as pd
from utils import month_order
import os

file_name = 'kajabi_metrics.csv'
df = pd.read_csv(file_name)

#reorder columns
df = df[['Month', 'Year', 'New Subscribes', 'Unsubscribes', 'Net Subscriber Growth', 'Total Subscribers']]

df['Total_Subscribers_Last_Month'] = df['Total Subscribers'].shift(1)

# create a date column for date-time plotting
df['Date'] = pd.to_datetime(df['Month'] + ' 28 ' + df['Year'].astype(str))

df['Month'] = pd.Categorical(df['Month'], categories=month_order.keys(), ordered=True)
df = df.sort_values(['Year', 'Month'], ignore_index=True)

if not os.path.exists('transformed_wide'):
    os.makedirs('transformed_wide', exist_ok=True)

try:
    df.to_csv('transformed_wide/kajabi_metrics.csv', index=False)
except Exception as e:
    print(f"Error saving file: {e}")

print(df)