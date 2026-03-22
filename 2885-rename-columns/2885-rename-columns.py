import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # Use a dictionary to map current names to new names
    # columns={ 'old_name': 'new_name' }
    return students.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    })