import pandas as pd
from utils import month_order
import os

file_name = 'website_metrics.csv'
df = pd.read_csv(file_name)

#reorder columns
df = df[['Month', 'Year', 'Webpage Views', 'Session Time (mins)', 'No. of Subscribers Through Website', 'Bounce Rate (Left without taking an action)']]

#rename columns
df.columns = ['Month', 'Year', 'Views', 'Session Time (mins)', 'No. of Subscribers', 'Bounce Rate'] 

df['Cummulative  Views'] = df['Views'].cumsum()

# create a date column for date-time plotting
df['Date'] = pd.to_datetime(df['Month'] + ' 28 ' + df['Year'].astype(str))

df['Month'] = pd.Categorical(df['Month'], categories=month_order.keys(), ordered=True)
df = df.sort_values(['Year', 'Month'], ignore_index=True)

if not os.path.exists('transformed_wide'):
    os.makedirs('transformed_wide', exist_ok=True)

try:
    df.to_csv('transformed_wide/website_metrics.csv', index=False)
except Exception as e:
    print(f"Error saving file: {e}")

print(df)