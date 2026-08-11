from .count_duplicates import count_duplicates
from .count_missing_values import count_missing_values
from ..utils.validators import validate_columns

def get_summary(df, unique_cols=None):
    """
    Genera un resumen general del DataFrame
    
    Args:
        df (DataFrame)
        unique_cols (list)
        
    Returns:
        dict
    """
    
    if unique_cols is None:
        unique_cols = []
    
    validate_columns(df, unique_cols)
        
    summary = {
        "Filas": df.shape[0],
        "Columnas": df.shape[1],
        "Valores nulos": count_missing_values(df),
        "Duplicados": count_duplicates(df)
    }
    
    for col in unique_cols:
        summary[f"{col} únicos"] = df[col].nunique()
        
    return summary