
def count_missing_values(df):
    """
    Cuenta valores faltantes en un DataFrame
    
    Args:
        df (DataFrame) 
    
    Returns:
        int
    """
    
    return df.isnull().sum().sum()

