from datetime import datetime

def create_month_year_lists(start_month, start_year, num_months=17):
    # Create mapping for Sept 2024 to Dec 2025
    '''
    month index is not zero indexed. it is 1 indexed. so january is 1, february is 2, etc.
    '''
    months = []
    years = []
    current_month = start_month
    current_year = start_year
    distant_from_new_year = 12 - start_month
    
    for i in range(1, num_months):  # 16 months from Sept 2024 to Dec 2025
        if distant_from_new_year == 12:
            current_year += 1
            
        month_name = datetime(2000, current_month, 1).strftime('%B')
        months.append(month_name)
        years.append(current_year)
        
        current_month += 1
        
        if current_month > 12:
            current_month = 1
          
        
        distant_from_new_year -= 1  
        if distant_from_new_year == 0:
            distant_from_new_year = 12
            
            
    
    return months, years

def create_month_year_mapping(start_month, start_year, num_months=17):
    # Create mapping for Sept 2024 to Dec 2025
    '''
    month index is not zero indexed. it is 1 indexed. so january is 1, february is 2, etc.
    '''
    mapping = {}
    current_month = start_month
    current_year = start_year
    distant_from_new_year = 12 - start_month
    
    for i in range(1, num_months):  # 16 months from Sept 2024 to Dec 2025
        if distant_from_new_year == 12:
            current_year += 1
            
        month_name = datetime(2000, current_month, 1).strftime('%B')
        mapping[i] = [month_name, current_year]
        
        current_month += 1
        
        if current_month > 12:
            current_month = 1
          
        
        distant_from_new_year -= 1  
        if distant_from_new_year == 0:
            distant_from_new_year = 12
            
            
    
    return mapping

month_order = {month: index for index, month in enumerate(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'], 1)}
       