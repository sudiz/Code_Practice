import pandas as pd

def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema= cinema.merge(cinema,how='cross')
    res=cinema[(cinema['free_x']==1)&(cinema['free_y']==1)&(abs(cinema['seat_id_x']-cinema['seat_id_y'])==1)][['seat_id_x']]
    res=res.drop_duplicates(subset='seat_id_x').rename(columns={'seat_id_x':'seat_id'}).sort_values(by='seat_id')
    return res
