from ..utils.logging import log_message

def exclude_sheets(sheet_names, excluded_sheets=None, log=True):
    """
    Excluye las hojas de Excel innecesarias
    
    Args:
        sheet_names (iterable)
        excluded_sheets (list, optional)
        log (bool)
        
    Returns:
        list
    """
        
    if excluded_sheets is None:
        excluded_sheets = []
        
    valid_sheets = [
        sheet
        for sheet in sheet_names
        if sheet not in excluded_sheets
    ]
    
    if log:
        log_message(
            (
                f"Han sido excluidas {len(excluded_sheets)} hojas correctamente | \n"
                f"Total hojas: {len(sheet_names)} | \n"
                f"Hojas Válidas: {len(valid_sheets)} | \n"
            ),
            separator=True
        )
    
    return valid_sheets