from ..utils.logging import log_message

def save_dataframe(df, output_path, index=False, log=True):
    """
    Guarda DataFrame en un archivo Excel
    
    Args:
        df (DataFrame)
        output_path (Path)
        index (bool)
        
    Returns:
        None
    """
    
    df.to_excel(
        output_path,
        index=index
    )
    
    if log:
        log_message(
            (
                f"DataFrame guardado exitosamente | \n"
                f"Archivo: {output_path.name} | \n"
                f"Ruta: {output_path.parent} | \n"
                f"{df.shape[0]} Filas | {df.shape[1]} Columnas | \n"
            ),
            separator=True
        )