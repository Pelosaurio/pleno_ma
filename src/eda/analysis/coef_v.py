import numpy as np

from .mean_group import mean_group
from .standard_d import standard_d

def coef_v(df, group_column, column_names, mean=None, std=None):
    """
    Calcula el coeficiente de variacion para columnas numericas agrupadas por una variable categorica
    
    Args:
        df (DataFrame)
        group_column (str)
        column_names (list)
        mean (DataFrame, optional)
        std (DataFrame, optional)
        
    Returns:
        DataFrame
    """
    
    if mean is None:
        mean = mean_group(df, group_column, column_names)
    
    if std is None:
        std = standard_d(df, group_column, column_names)
        
    coef_var = (std / mean.replace(0, np.nan)) * 100
    
    coef_var = coef_var.fillna(0)
    
    return coef_var