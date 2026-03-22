import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # Target the 'quantity' column and fill its NaN/None values with 0
    products['quantity'] = products['quantity'].fillna(0)
    
    return products