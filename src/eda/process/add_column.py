
def add_column(df, column_name, value, position=None):
    """
    Agrega columna identificadora y permite controlar su posicion dentro del DataFrame
    
    Args:
        df (DataFrame)
        column_name (str)
        value (Any)
        position (int, optional)
        
    Returns:
        DataFrame
    """ 
    
    df[column_name] = value
    
    if position is not None:
        
        column = df.pop(column_name)
        
        df.insert(
            position,
            column_name,
            column
        )
        
    return df