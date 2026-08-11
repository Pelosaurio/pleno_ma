from ...process.get_head import get_head
from .show_title import show_title
from .show_separator import show_separator

def show_head(df, rows=5):
    """
    Muestra las primeras filas del DataFrame

    Args:
        df (DataFrame)
        rows (int, optional)
    
    Returns:
        None
    """
    
    show_title(f"Primeras {rows} filas del DataFrame \n")
    
    print(get_head(df, rows))
    
    print()
    
    show_separator()