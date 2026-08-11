from ..utils.validators import validate_columns

def sort_dataframe(df, column, ascending=False):
    """
    Ordena el DataFrame segun la columna indicada
    
    Args:
        df (DataFrame)
        column (str)
        ascending (bool, optional)
        
    Returns:
        DataFrame
    """
    
    validate_columns(df, column)
    
    return df.sort_values(by=column, ascending=ascending)