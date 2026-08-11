from pandas.api.types import is_numeric_dtype

def validate_numeric_columns(df, columns):
    """
    Valida que una o mas columnas existan en el DataFrame y que sean numericas
    
    Args:
        df (DataFrame)
        columns (str | list)
        
    Raises:
        ValueError
        TypeError
    """
    
    if isinstance(columns, str):
        columns = [columns]
        
    for column in columns:
        
        if column not in df.columns:
            raise ValueError(f'La columna "{column}" no existe en el DataFrame')
    
        if not is_numeric_dtype(df[column]):
            raise TypeError(f'La columna "{column}" debe ser numérica')