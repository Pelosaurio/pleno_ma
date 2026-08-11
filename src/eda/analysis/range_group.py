from ..utils.validators import validate_columns

def range_group(df, group_column, column_names):
    """
    Calcula el rango para columnas numericas agrupadas por una variable categorica
    
    Args:
        df (DataFrame)
        group_column (str)
        column_names (list)
    
    Returns:
        DataFrame
    """
    
    validate_columns(df, [group_column, *column_names])
    
    return df.groupby(group_column)[column_names].apply(lambda x: x.max() - x.min())
