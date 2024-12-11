import pandas as pd
from utils import month_order


# def transform_kajabi_metrics(input_file):
#     # Read the CSV file
#     df = pd.read_csv(input_file, header=None)
    
#     num_months = len(df.columns) 
    
#     # Create month-year mapping
#     months, years = create_month_year_lists(9, 2024, num_months)
    
#     # Create the transformed dataframe
#     transformed_data = {
#         'Month': months,
#         'Year': years,
#         'Total_Subscribers': df.iloc[1, 1:].values,
#         'New_Subscribers': df.iloc[2, 1:].values,
#         'Unsubscribes': df.iloc[3, 1:].values,
#         'Net_Subscriber_Growth': df.iloc[4, 1:].values,
#     }
    
#     # Create new dataframe
#     transformed_df = pd.DataFrame(transformed_data)
    
#     # add a column for the previous month's total subscribers
#     transformed_df['Total_Subscribers_Previous_Month'] = [float('nan')] + list(df.iloc[1, 1:-1].values)
    
#     # Save the transformed data
#     transformed_df.to_csv('kajabi_metrics_transformed.csv', index=False)
    
#     return transformed_df

# # Transform the file
# df = transform_kajabi_metrics('kajabi_metrics.csv')
# print(df)


df = pd.read_csv('kajabi_metrics.csv')
df.rename(columns={'Unsubscribes (Last 30 days)': 'Unsubscribes', 'New Subscribes': 'New_Subscribers', 'Total Subscribers': 'Total_Subscribers'}, inplace=True)
# df.rename(columns={'Unsubscribes (Last 30 days)': 'Unsubscribes', 'New sub (Last 30 days)': 'New_Subscribers', 'total Subscribers': 'Total_Subscribers'}, inplace=True)


# rarrange data
df = df[['Month', 'Year', 'Total_Subscribers', 'New_Subscribers', 'Unsubscribes']]


df = df.melt(id_vars=['Month', 'Year'], value_vars=['Total_Subscribers', 'New_Subscribers', 'Unsubscribes'], var_name='Metric', value_name='Value')

# create a date column for date-time plotting
df['Date'] = pd.to_datetime(df['Month'] + ' 28 ' + df['Year'].astype(str))

df['Month'] = pd.Categorical(df['Month'], categories=month_order.keys(), ordered=True)
df = df.sort_values(['Year', 'Month'], ignore_index=True)


df.to_csv('transformed/kajabi_metrics_transformed.csv', index=False)
print(df)

