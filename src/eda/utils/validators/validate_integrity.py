from ..logging import log_message

def validate_integrity(df, column_names, log=True):
    """
    Valida que cada fila tenga exactamente un voto registrado
    
    Args:
        df (DataFrame)
        column_names (list)
        log (bool)
        
    Returns:
        DataFrame
    """
    
    vote_sum = df[column_names].sum(axis=1)
    
    invalid_integrity = df[vote_sum != 1]
    
    invalid_details = []
    
    without_vote = 0
    
    multiple_vote = 0
    
    if invalid_integrity.empty: 
        if log:
            log_message(
                (
                    f"Validación de integridad de votos completada | \n"
                    f"Columnas evaluadas = {column_names} | \n"
                    f"Filas evaluadas = {len(df)} | \n"
                    f"Estado = APROBADA | \n"
                    f"Cada convencional ha emitido exactamente 1 voto por artículo | \n"
                ),
                separator=True
            )
        
    else:
        
        for row in invalid_integrity.index:
            active_votes = []
            
            for col in column_names:
                if df.loc[row, col] == 1:
                    active_votes.append(col)
            
            if not active_votes:
                without_vote += 1
                
                invalid_details.append(
                    f"Fila {row} | Sin votos registrados"
            )
                
            elif len(active_votes) > 1:
                multiple_vote +=1
                
                invalid_details.append(
                    f"Fila {row} | Múltiples votos detectados: {active_votes}"
                )
        
        if log:
            log_message(
                (
                    f"Validación de integridad de votos completada | \n"
                    f"Columnas evaluadas = {column_names} | \n"
                    f"Filas evaluadas = {len(df)} | \n"
                    f"Convencionales sin votos registrados = {without_vote} | \n"
                    f"Convencionales con múltiples votos registrados = {multiple_vote} | \n"
                    f"Estado = REQUIERE MODIFICACIONES | \n"
                    + "\n".join(invalid_details) 
                    +"| \n"
                    ),
                    separator=True
            )
    
    return invalid_integrity