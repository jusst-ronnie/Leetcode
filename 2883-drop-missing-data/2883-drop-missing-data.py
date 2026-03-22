import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # Remove rows where the 'name' column contains null/None values
    # By default, it returns a new DataFrame with the rows removed.
    return students.dropna(subset=['name'])