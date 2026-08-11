from ...analysis.get_summary import get_summary
from .show_title import show_title
from .show_separator import show_separator

def show_summary(df, unique_cols=None):
    """
    Muestra un resumen general del DataFrame
    
    Args:
        df (DataFrame)
        unique_cols (list, optional)
        
    Returns:
        None
    """
    
    summary = get_summary(df, unique_cols)
    
    show_title("Resumen del DataFrame \n")
    
    for key, value in summary.items():
        print(f"{key}: {value}")
    
    print()
    
    show_separator()