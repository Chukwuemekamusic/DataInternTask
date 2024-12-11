import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a clean, professional style for the visualizations
# plt.style.use('seaborn')

def load_and_prepare_data(file_path):
    """
    Load the CSV file and prepare the data for analysis.
    
    Args:
        file_path (str): Path to the CSV file
    
    Returns:
        pandas.DataFrame: Processed dataframe
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Create a pivot table for easier visualization
    pivot_df = df.pivot_table(
        index=['Month', 'Year', 'Date'], 
        columns='Metric', 
        values='Value'
    ).reset_index()
    
    return pivot_df

def visualize_subscriber_growth(df):
    """
    Create visualizations for subscriber growth trends.
    
    Args:
        df (pandas.DataFrame): Processed dataframe
    """
    plt.figure(figsize=(12, 6))
    
    # Line plot for Number of Followers
    followers_data = df[df['Metric'] == 'Number of Followers']
    plt.plot(followers_data['Date'], followers_data['Value'], 
             marker='o', linestyle='-', linewidth=2, markersize=8)
    
    plt.title('Subscriber Growth Over Time', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Number of Followers', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('subscriber_growth.png')
    plt.close()

def compare_follower_metrics(df):
    """
    Create a visualization comparing follower-related metrics.
    
    Args:
        df (pandas.DataFrame): Processed dataframe
    """
    # Select relevant metrics
    net_growth = df[df['Metric'] == 'Net Follower Growth']
    total_followers = df[df['Metric'] == 'Number of Followers']
    
    plt.figure(figsize=(12, 6))
    
    # Bar plot for Net Follower Growth
    plt.subplot(1, 2, 1)
    plt.bar(net_growth['Date'].dt.strftime('%b %Y'), net_growth['Value'], 
            color='blue', alpha=0.7)
    plt.title('Net Follower Growth', fontsize=14)
    plt.xlabel('Month', fontsize=10)
    plt.ylabel('New Followers', fontsize=10)
    plt.xticks(rotation=45)
    
    # Line plot for Total Followers
    plt.subplot(1, 2, 2)
    plt.plot(total_followers['Date'], total_followers['Value'], 
             marker='o', color='green', linestyle='-', linewidth=2)
    plt.title('Total Followers', fontsize=14)
    plt.xlabel('Date', fontsize=10)
    plt.ylabel('Cumulative Followers', fontsize=10)
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('follower_metrics_comparison.png')
    plt.close()

def engagement_analysis(df):
    """
    Visualize engagement metrics.
    
    Args:
        df (pandas.DataFrame): Processed dataframe
    """
    # Select engagement-related metrics
    engagement_metrics = ['Total Engagement', 'Total Impressions', 'Total Video Views']
    
    # Prepare data
    engagement_data = df[df['Metric'].isin(engagement_metrics)]
    
    plt.figure(figsize=(12, 6))
    
    # Grouped bar plot for engagement metrics
    engagement_pivot = engagement_data.pivot(index='Date', columns='Metric', values='Value')
    engagement_pivot.plot(kind='bar', figsize=(12, 6))
    
    plt.title('Engagement Metrics Comparison', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Metric Value', fontsize=12)
    plt.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('engagement_metrics.png')
    plt.close()

def main():
    """
    Main function to run the entire analysis and visualization process.
    """
    # Load the data
    file_path = '../transformed/social_metrics_transformed.csv'
    df = load_and_prepare_data(file_path)
    
    # Generate visualizations
    visualize_subscriber_growth(df)
    compare_follower_metrics(df)
    engagement_analysis(df)
    
    print("Visualizations have been generated and saved.")

# Run the main function
if __name__ == '__main__':
    main()