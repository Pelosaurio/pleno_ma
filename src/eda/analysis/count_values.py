from ..utils.validators import validate_columns

def count_values(df, group_column):
    """
    Cuenta los valores de cada categoria en una columna
    
    Args:
        df (DataFrame)
        group_column (str)
    
    Returns:
        Series
    """
    
    validate_columns(df, group_column)
    
    return df[group_column].value_counts()