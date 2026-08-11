
def validate_columns(df, columns):
    """
    Valida que la columna exista en el DataFrame
    
    Args:
        df (DataFrame)
        column_names (list)
        
    Raises:
        ValueError
    """
    
    if isinstance(columns, str):
        columns = [columns]
        
    for column in columns:
        if column not in df.columns:
            raise ValueError(
                f"La columna '{column}' no existe en el DataFrame"
            )