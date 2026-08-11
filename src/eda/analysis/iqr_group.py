from ..utils.validators import validate_columns

def iqr_group(df, group_column, column_names):
    """
    Calcula el rango intercuartilico para columnas numericas agrupadas por una variable categorica

    Args:
        df (DataFrame)
        group_column (str)
        column_names (list)
        value_column (str)
    
    Returns:
        DataFrame
    """
    
    validate_columns(df, [group_column, *column_names])
    
    return (
        df.groupby(group_column)[column_names]
        .apply(lambda group: group.quantile(0.75) - group.quantile(0.25))
    )
    