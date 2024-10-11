import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    idx=activity.groupby('player_id')['event_date'].idxmin()
    res=activity.loc[idx,['player_id','device_id']]
    return res
