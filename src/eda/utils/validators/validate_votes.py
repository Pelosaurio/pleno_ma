from ..logging import log_message

def validate_votes(df, column_names, log=True):
    """
    Valida que los votos en el DataFrame solo contengan valores [0] o [1]
    
    Args: 
        df (DataFrame)
        column_names (list)
        log (bool)
        
    Returns:
        list
    """
    
    valid_values = [0, 1]
    
    invalid_details = []
    
    for col in column_names:
        is_invalid = df[col].isin(valid_values) == False
        invalid_votes = df[is_invalid]
        
        if not invalid_votes.empty:
            for row, invalid_value in invalid_votes[col].items():
                invalid_details.append(
                    f"Fila {row} | Columna {col} | Valor {invalid_value}"
                )
                
    if log: 
        if invalid_details:
            log_message(
                (
                    f"Validación de votos completada | \n"
                    f"Columnas evaluadas = {column_names} | \n"
                    f"Valores inválidos detectados = {len(invalid_details)} | \n"
                    f"Estado = REQUIERE MODIFICACIONES | \n"
                    + "\n".join(invalid_details) 
                    +"| \n"
                ),
                separator=True
            )
        
        else:
            log_message(
                (
                    f"Validación de votos completada | \n"
                    f"Columnas evaluadas = {column_names} | \n"
                    f"Valores inválidos detectados = {len(invalid_details)} | \n"
                    f"Estado = APROBADA | \n"
                ),
                separator=True
            )
    
    return invalid_details