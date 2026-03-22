import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Access the 'salary' column and multiply all values by 2
    # Then, assign those values back to the same 'salary' column
    employees['salary'] = employees['salary'] * 2
    
    return employees