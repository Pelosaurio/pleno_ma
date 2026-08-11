from .range_group import range_group
from .standard_d import standard_d
from .coef_v import coef_v
from ..utils.logging import log_message

def dispersion_m(df, group_column, column_names, log=True):
    """
    Calcula las medidas de dispersion para columnas numericas agrupadas por una variable categorica
    
    Args:
        df (DataFrame)
        group_column (str)
        column_names (list)
        log (bool)
        
    Returns:
        dict
    """
    
    range_result = range_group(df, group_column, column_names)
    
    std_result = standard_d(df, group_column, column_names)
    
    cv_result = coef_v(df, group_column, column_names)
    
    if log:
        log_message(
            (
                f"Medidas de dispersion agrupadas calculadas exitosamente | \n"
                f"Columnas analizadas = {column_names} | \n"
                f"Agrupadas por: {group_column} | \n"
            ),
            separator=True
        )
    
    return {
        "rango": range_result,
        "des_std": std_result,
        "coef_var": cv_result
    }