
def get_head(df, rows=5):
    """
    Obtiene las primeras filas de un DataFrame, por defecto las primeras 5
    
    Args:
        df (DataFrame)
        rows (int, optional)
        
    Returns:
        DataFrame
    """
    
    return df.head(rows)