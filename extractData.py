# coding: utf-8
import pandas as pd
import configparser
import datetime
import pytz

localtime = datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d")
config = configparser.ConfigParser()
filename = 'config.ini'
config.read(filename, encoding='utf-8')
report = str()

stocks_codes_str = config.get('stocks', 'codes')
stocks_codes_list = stocks_codes_str.replace(' ', '').split(',')
df_stocks = pd.read_excel(localtime + '/A_data.xlsx', dtype='object')[['code', 'name', 'trade', 'changepercent']]
for stock_code in stocks_codes_list:
    if stock_code == '':
        continue
    try:
        df_temp = df_stocks[df_stocks['code'] == stock_code].reset_index(drop=True)
        name = df_temp['name'][0]
        trade = df_temp['trade'][0]
        change = df_temp['changepercent'][0]
        report += "{code} {name}  现价 {close:.2f}, {vhdp}{change:.2f}%\n"\
            .format(code=stock_code, name=name, close=float(trade)
                    , vhdp='上涨' if float(change) >= 0 else '下跌', change=abs(float(change)))
    except:
        continue

inner_goods_future_str = config.get('InnerGoodsFutures', 'names')
inner_goods_future_list = inner_goods_future_str.replace(' ', '').split(',')
df_inner_goods = pd.read_excel(localtime + '/Future_C_data.xlsx', dtype='object')[['symbol', 'current_price', 'last_settle_price']]
df_inner_goods['change'] = 100 * (df_inner_goods['current_price'].apply(float) - df_inner_goods['last_settle_price'].apply(float)) / df_inner_goods['last_settle_price'].apply(float)
for name in inner_goods_future_list:
    if name == '':
        continue
    try:
        df_temp = df_inner_goods[df_inner_goods['symbol'].str.contains(name)].reset_index(drop=True)
        price = df_temp['current_price'][0]
        change = df_temp['change'][0]
        report += "{name}  现价 {price:.2f}, {vhdp}{change:.2f}%\n"\
            .format(name=name, price=float(price), change=abs(float(change)), vhdp='上涨' if float(change) >=0 else '下跌')
    except:
        continue

inner_finance_future_str = config.get('InnerFinanceFutures', 'names')
inner_finance_future_list = inner_finance_future_str.replace(' ', '').split(',')
df_inner_finance = pd.read_excel(localtime + '/Future_F_data.xlsx', dtype='object')[['symbol', 'current_price', 'open']]
df_inner_finance['change'] = 100 * (df_inner_finance['current_price'].apply(float) - df_inner_finance['open'].apply(float)) / df_inner_finance['open'].apply(float)
for name in inner_finance_future_list:
    if name == '':
        continue
    try:
        df_temp = df_inner_finance[df_inner_finance['symbol'].str.contains(name)].reset_index(drop=True)
        price = df_temp['current_price'][0]
        change = df_temp['change'][0]
        report += "{name}  现价 {price:.2f}, {vhdp}{change:.2f}%\n"\
            .format(name=name, price=float(price), change=abs(float(change)), vhdp='上涨' if float(change) >=0 else '下跌')
    except:
        continue

outer_future_str = config.get('OuterFutures', 'names')
outer_future_list = outer_future_str.replace(' ', '').split(',')
df_outer = pd.read_excel(localtime + '/Future_W_data.xlsx', dtype='object')[['symbol', 'current_price', 'last_settle_price']]
df_outer['change'] = 100 * (df_outer['current_price'].apply(float) - df_outer['last_settle_price'].apply(float)) / df_outer['last_settle_price'].apply(float)
for name in outer_future_list:
    if name == '':
        continue
    try:
        df_temp = df_outer[df_outer['symbol'].str.contains(name)].reset_index(drop=True)
        price = df_temp['current_price'][0]
        change = df_temp['change'][0]
        report += "{name}  现价 {price:.2f}, {vhdp}{change:.2f}%\n"\
            .format(name=name, price=float(price), change=abs(float(change)), vhdp='上涨' if float(change) >=0 else '下跌')
    except:
        continue

shibor_time_str = config.get('Shibor', 'times')
shibor_time_list = shibor_time_str.replace(' ', '').split(',')
for t in shibor_time_list:
    try:
        df_temp = pd.read_excel(localtime + '/Shibor_' + t + '.xlsx', index_col=0)
        rate = df_temp['利率(%)'][0]
        bp = df_temp['涨跌(BP)'][0]
        report += "Shibor{ti}  利率 {rate}%, 涨跌{bp}BP\n"\
            .format(ti=t, rate=rate, bp=bp)
    except:
        continue

libor_time_str = config.get('Libor', 'times')
libor_time_list = libor_time_str.replace(' ', '').split(',')
for t in libor_time_list:
    try:
        df_temp = pd.read_excel(localtime + '/Libor_' + t + '.xlsx', index_col=0)
        rate = df_temp['利率(%)'][0]
        bp = df_temp['涨跌(BP)'][0]
        report += "Libor美元 {ti}  利率 {rate}%, 涨跌{bp}BP\n"\
            .format(ti=t, rate=rate, bp=bp)
    except:
        continue


with open('todayData.txt', 'w', encoding='utf-8') as f:
    f.write(report)
