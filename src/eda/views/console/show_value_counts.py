from ...analysis.count_values import count_values
from .show_title import show_title
from .show_separator import show_separator

def show_value_counts(df, group_column):
    """
    Muestra el conteo de valores de cada categoria en una columna
    
    Args:
        df (DataFrame)
        group_column (str)
        
    Returns:
        None
    """
    
    counts = count_values(df, group_column)
    
    show_title(f"Frecuencia de valores en cada '{group_column}' \n")
    
    print(counts.to_string())
    
    print(f"Grupos en total = {len(counts)} \n")
    
    show_separator()