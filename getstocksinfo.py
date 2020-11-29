# coding: utf-8
import akshare as ak
import os
import datetime
import time
import pytz

localtime = datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d")
if not os.path.exists(localtime):
    os.mkdir(localtime)
try:
    df_Stock = ak.stock_zh_a_spot()
    df_Stock.to_excel(localtime + '/A_data.xlsx')

except:
    pass

time.sleep(10)

try:
    dce_text = ak.match_main_contract(exchange="dce")
    czce_text = ak.match_main_contract(exchange="czce")
    shfe_text = ak.match_main_contract(exchange="shfe")
    df_Future_C = ak.futures_zh_spot(subscribe_list=",".join([dce_text, czce_text, shfe_text])
                                     , adjust=False, market="CF")
    df_Future_C.to_excel(localtime + '/Future_C_data.xlsx')
except:
    pass

time.sleep(10)

try:
    cffex_text = ak.match_main_contract(exchange="cffex")
    df_Future_F = ak.futures_zh_spot(subscribe_list=cffex_text, market="FF", adjust=False)
    df_Future_F.to_excel(localtime + '/Future_F_data.xlsx')
except:
    pass

time.sleep(10)

try:
    subscribe_list = ak.hf_subscribe_exchange_symbol()
    df_Future_W = ak.futures_hf_spot(subscribe_list=subscribe_list)
    df_Future_W.to_excel(localtime + '/Future_W_data.xlsx')
except:
    pass

df_Shibor = {'隔夜': None, '1周': None, '2周': None, '1月': None, '3月': None, '6月': None, '9月': None, '1年': None}
try:
    for key, value in df_Shibor.items():
        df_Shibor[key] = ak.rate_interbank(market="上海银行同业拆借市场", symbol="Shibor人民币", indicator=key, need_page="1")
    for key, value in df_Shibor.items():
        value.to_excel(localtime + '/Shibor_' + key + '.xlsx')
except:
    pass

df_Libor = {'隔夜': None, '1周': None, '1月': None, '2月': None, '3月': None, '8月': None}
try:
    for key, value in df_Libor.items():
        df_Libor[key] = ak.rate_interbank(market="伦敦银行同业拆借市场", symbol="Libor美元", indicator=key, need_page="1")
    for key, value in df_Libor.items():
        value.to_excel(localtime + '/Libor_' + key + '.xlsx')
except:
    pass
