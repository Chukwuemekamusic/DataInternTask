import pandas as pd
import calendar

def extract_metrics(file_path):
    # Read the CSV file, skipping the first row
    df = pd.read_csv(file_path, header=0)
    
    
    # Find the start indices for each section
    kajabi_start = df[df.iloc[:, 0] == 'Kajabi Database Metrics'].index[0]
    lead_gen_start = df[df.iloc[:, 0] == 'Lead Gen Metrics (total monthly growth)'].index[0]
    email_start = df[df.iloc[:, 0] == 'Email Metrics'].index[0]
    social_start = df[df.iloc[:, 0] == 'Social Metrics - insta'].index[0]
    website_start = df[df.iloc[:, 0] == 'Website Metrics'].index[0]
    podcast_start = df[df.iloc[:, 0] == 'Podcast Metrics'].index[0]
    
    # Get months from the header
    months = df.iloc[0, 1:].dropna().tolist()
    # Determine the year for each month (assuming the CSV structure remains similar)
    years = ['2024' if i < 4 else '2025' for i in range(len(months))]
    month_order = {month: index for index, month in enumerate(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'], 1)}
       
    def clean_section(start_idx, end_idx, skip_rows=1):
        # Extract the section
        section = df.iloc[start_idx+skip_rows:end_idx-1].dropna(how='all', axis=1)
        # Clean up the metrics names
        section.iloc[:, 0] = section.iloc[:, 0].str.strip()
        # Set the first column as index
        section.set_index(section.columns[0], inplace=True)
        
        # Create a clean DataFrame with Month and Year columns
        clean_data = []
        for col, month, year in zip(section.columns, months[:len(section.columns)], years[:len(section.columns)]):
            data = section[col].dropna()
            if not data.empty:
                for metric_name, value in data.items():
                    clean_data.append({
                        'Month': month,
                        'Year': year,
                        'Metric': metric_name,
                        'Value': value
                    })
        
           # Create DataFrame and sort by year and month order
        result_df = pd.DataFrame(clean_data)
        
        
        return result_df

    # Extract each section
    kajabi_df = clean_section(kajabi_start, lead_gen_start)
    print('kajabi_df', kajabi_df)
    lead_gen_df = clean_section(lead_gen_start, email_start)
    print('lead_gen_df', lead_gen_df)
    email_df = clean_section(email_start, social_start)
    social_df = clean_section(social_start, website_start)
    website_df = clean_section(website_start, podcast_start)
    podcast_df = clean_section(podcast_start, df.shape[0])  # Until the end of file

     
    # Pivot the DataFrames to get the desired format
    def pivot_and_save(df, filename, month_order=month_order):
        if not df.empty:
            pivoted = df.pivot_table(
                index=['Month', 'Year'],
                columns='Metric',
                values='Value',
                aggfunc='first'
            ).reset_index()
        
            
            # Add a month order column for sorting
        pivoted['month_order'] = pivoted['Month'].map(month_order)
        
        # Sort by year and month order
        pivoted = pivoted.sort_values(['Year', 'month_order'])
        
        # Remove the temporary sorting column
        pivoted = pivoted.drop('month_order', axis=1)
        
        print('pivoted', pivoted)
        # Save to CSV
        pivoted.to_csv(filename, index=False)
        return pivoted

    # Save each DataFrame to a separate CSV file
    pivot_and_save(kajabi_df, 'kajabi_metrics.csv')
    pivot_and_save(lead_gen_df, 'lead_gen_metrics.csv')
    pivot_and_save(email_df, 'email_metrics.csv')
    pivot_and_save(social_df, 'social_metrics.csv')
    pivot_and_save(website_df, 'website_metrics.csv')
    pivot_and_save(podcast_df, 'podcast_metrics.csv')

# Call the function with your file path
file_path = 'Mock Monthly Metrics - Monthly Data Tracking.csv'
extract_metrics(file_path)