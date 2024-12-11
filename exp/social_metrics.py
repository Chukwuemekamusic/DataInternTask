import pandas as pd
from utils import month_order
import os

file_name = 'social_metrics.csv'
df = pd.read_csv(file_name)

#reorder columns
df = df[['Month', 'Year', 'Number of Followers', 'Net Follower Growth', 'Total Engagement', 'Total Impressions', 'Total Video Views']]

df['Number of Followers Previous Month'] = df['Number of Followers'].shift(1)
df['Net Follower Growth'] = df['Number of Followers'] - df['Number of Followers Previous Month']

# create a date column for date-time plotting
df['Date'] = pd.to_datetime(df['Month'] + ' 28 ' + df['Year'].astype(str))

df['Month'] = pd.Categorical(df['Month'], categories=month_order.keys(), ordered=True)
df = df.sort_values(['Year', 'Month'], ignore_index=True)


if not os.path.exists('transformed_wide'):
    os.makedirs('transformed_wide', exist_ok=True)

# Then try to save the file
try:
    df.to_csv('transformed_wide/social_metrics.csv', index=False)
except Exception as e:
    print(f"Error saving file: {e}")

print(df)