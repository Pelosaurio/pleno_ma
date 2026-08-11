
def count_duplicates(df):
    """
    Cuenta valores duplicados en un DataFrame
    
    Args:
        df (DataFrame)
        
    Returns:
        int
    """
    
    return df.duplicated().sum()
