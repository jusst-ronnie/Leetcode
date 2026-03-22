import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    # Define the column names in the exact order requested
    column_names = ["student_id", "age"]
    
    # Create the DataFrame
    df = pd.DataFrame(student_data, columns=column_names)
    
    return df