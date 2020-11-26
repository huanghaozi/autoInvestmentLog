# coding: utf-8
import akshare as ak
import pandas as pd
import time
try:
    df_Stock = ak.stock_zh_a_spot()
    df_Stock.to_json('A_data.json')
except:
    pass

time.sleep(10)

try:
    dce_text = ak.match_main_contract(exchange="dce")
    czce_text = ak.match_main_contract(exchange="czce")
    shfe_text = ak.match_main_contract(exchange="shfe")
    df_Future_C = ak.futures_zh_spot(subscribe_list=",".join([dce_text, czce_text, shfe_text])
                                     ,adjust=False,market="CF")
    df_Future_C.to_json('Future_C_data.json')
except:
    pass

time.sleep(10)

try:
    cffex_text = ak.match_main_contract(exchange="cffex")
    df_Future_F = ak.futures_zh_spot(subscribe_list=cffex_text, market="FF", adjust=False)
    df_Future_F.to_json('Future_F_data.json')
except:
    pass

time.sleep(10)

try:
    subscribe_list = ak.hf_subscribe_exchange_symbol()
    df_Future_W = ak.futures_hf_spot(subscribe_list=subscribe_list)
    df_Future_W.to_json('Future_W_data.json')
except:
    pass
