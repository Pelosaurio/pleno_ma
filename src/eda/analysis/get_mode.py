def get_mode(series):
    """
    Obtiene la primera moda de una serie
    
    Args:
        series (Series)
        
    Returns:
        Any
    """
    
    modes = series.mode()
    
    return modes.iloc[0]