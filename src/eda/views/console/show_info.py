from .show_title import show_title
from .show_separator import show_separator

def show_info(df):
    """
    Muestra informacion general del DataFrame
    
    Args:
        DataFrame
        
    Returns:
        None
    """
    
    show_title(f"Información general del Dataframe \n")
    
    df.info()
    
    show_separator()