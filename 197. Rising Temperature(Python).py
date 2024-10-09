import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather=weather.sort_values(by='recordDate')
    temp = weather[(weather['recordDate']-weather.shift(1)['recordDate']==datetime.timedelta(days=1) ) 
    & (weather['temperature']>weather.shift(1)['temperature'])]
    
    return temp[['id']]
    
