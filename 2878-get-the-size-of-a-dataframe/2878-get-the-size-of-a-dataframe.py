import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    # .shape returns (num_rows, num_columns)
    # We convert it to a list to match the return requirement
    return list(players.shape)