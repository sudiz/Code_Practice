import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    login=activity.groupby('player_id')['event_date'].min().reset_index()
    login['event_date']=login['event_date']+pd.DateOffset(days=1)#pd.Timedelta(days=1)
    temp = activity.merge(login,on=['player_id','event_date'])
    res=round(temp['player_id'].nunique()/activity['player_id'].nunique(),2)

    return pd.DataFrame({'fraction':[res]})
