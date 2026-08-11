from .show_title import show_title
from .show_separator import show_separator

def show_keys(data, columns=9):
    """
    Muestra los nombres de las hojas excel
    
    Args:
        data(dict)
    
    Returns:
        None
    """
    
    keys = list(data.keys())
    
    show_title(f"Existen {len(keys)} hojas en el archivo Excel \n")
    
    for i in range(0, len(keys), columns):
        print(" | ".join(keys[i:i + columns]))
    
    print()
    
    show_separator()