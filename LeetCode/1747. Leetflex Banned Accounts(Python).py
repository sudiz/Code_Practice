import pandas as pd

def leetflex_banned_accnts(log_info: pd.DataFrame) -> pd.DataFrame:
    log_info = log_info.merge(log_info,how='cross')
    res=log_info[(log_info['account_id_x']==log_info['account_id_y'])
    &(log_info['ip_address_x']!=log_info['ip_address_y'])
    &(log_info['login_x']>=log_info['login_y'])
    &(log_info['login_x']<=log_info['logout_y'])][['account_id_x']].drop_duplicates(subset='account_id_x').rename(columns={'account_id_x':'account_id'})

    return res
