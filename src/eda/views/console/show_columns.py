from ...process.get_columns import get_columns
from .show_title import show_title
from .show_separator import show_separator

def show_columns(df):
    """
    Muestra los nombres de las columnas de un DataFrame
    
    Args:
        df (DataFrame)
        
    Returns:
        None
    """
    
    columns = get_columns(df)
    
    show_title("Todas las columnas del DataFrame \n")
    
    for col in columns:
        print(f"- {col}")
    
    print()
    
    show_separator()