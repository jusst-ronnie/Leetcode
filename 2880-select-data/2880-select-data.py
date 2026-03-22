import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # 1. Filter the rows where student_id is 101
    # 2. Select the specific columns 'name' and 'age'
    return students.loc[students['student_id'] == 101, ['name', 'age']]