
def ensure_dir_exists(path):
    """
    Verifica que la ruta de salida exista y en caso de no existir la crea junto con sus directorios correspondientes
    
    Args:
        path (Path)
        
    Returns:
        None
    """
    path.mkdir(parents=True, exist_ok=True) 

def generate_output_path(path, filename):
    """
    Genera una ruta de salida asegurando la existencia de un directorio de destino 
    
    Args:
        path (Path)
        filename (str)
    
    Returns:
        Path
    """
    
    ensure_dir_exists(path)
    return path / filename