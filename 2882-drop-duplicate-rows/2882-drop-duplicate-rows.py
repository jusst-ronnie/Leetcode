import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Drop rows where 'email' is repeated, keeping the first one seen
    return customers.drop_duplicates(subset='email', keep='first')