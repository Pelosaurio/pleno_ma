from .get_mode import get_mode
from ..utils.validators import validate_columns

def mode_group(df, group_column, column_names):
    """
    Calcula la moda para columnas numericas agrupadas por una variable categorica
    
    Args:
        df (DataFrame)
        group_column (str)
        column_names (list)
    
    Returns:
        DataFrame
    """
    
    validate_columns(df, [group_column, *column_names])
    
    grouped = (
        df
        .groupby(group_column)[column_names]
        .agg(get_mode)
        .reset_index()
    )
    
    return grouped
