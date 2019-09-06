#coding: utf-8
from bs4 import BeautifulSoup
import requests, datetime, string, os, xlsxwriter

todaytime = datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')

wt_book = xlsxwriter.Workbook(todaytime + '.xlsx')
wt_sheet = wt_book.add_worksheet('AllData')

styleA = wt_book.add_format({
    "bold": True, 
    "font_name": 'Microsoft YaHei', 
    "font_size": 12,
    "align" : 'center',
    "locked" : True
})
styleB = wt_book.add_format({
    "font_name": 'Microsoft YaHei Light', 
    "font_size": 14,
    "align" : 'center',
    "num_format": '#,##0.000'
})
styleC = wt_book.add_format({
    "font_name": 'Microsoft YaHei Light', 
    "font_size": 14,
    "align" : 'center',
    "num_format": 'yyyy-mm-dd'
})
styleD = wt_book.add_format({
    "font_name": 'Microsoft YaHei Light', 
    "font_size": 14,
    "align" : 'center',
    "num_format": '0.000%'
})

def writeInit2xlsx():
    wt_sheet.write(0, 0, "日期", styleA)
    wt_sheet.write(0, 1, "名称", styleA)
    wt_sheet.write(0, 2, "开", styleA)
    wt_sheet.write(0, 3, "现", styleA)
    wt_sheet.write(0, 4, "昨收", styleA)
    wt_sheet.write(0, 5, "最高", styleA)
    wt_sheet.write(0, 6, "最低", styleA)
    wt_sheet.write(0, 7, "涨跌", styleA)
    wt_sheet.write(0, 8, "涨跌百分比", styleA)
    wt_sheet.write(0, 9, "成交量（手）", styleA)
    
    wt_sheet.write(13, 0, "Shibor", styleB)
    wt_sheet.write(14, 0, "日期", styleA)
    wt_sheet.write(14, 1, "O/N", styleA)
    wt_sheet.write(14, 2, "1W", styleA)
    wt_sheet.write(14, 3, "2W", styleA)
    wt_sheet.write(14, 4, "1M", styleA)
    wt_sheet.write(14, 5, "3M", styleA)
    wt_sheet.write(14, 6, "6M", styleA)
    wt_sheet.write(14, 7, "9M", styleA)
    wt_sheet.write(14, 8, "1Y", styleA)
    
    wt_sheet.write(17, 0, "Libor", styleB)
    wt_sheet.write(18, 0, "日期", styleA)
    wt_sheet.write(18, 1, "O/N", styleA)
    wt_sheet.write(18, 2, "1W", styleA)
    wt_sheet.write(18, 3, "1M", styleA)
    wt_sheet.write(18, 4, "2M", styleA)
    wt_sheet.write(18, 5, "3M", styleA)
    wt_sheet.write(18, 6, "6M", styleA)
    wt_sheet.write(18, 7, "1Y", styleA)
    
    wt_sheet.set_column('A:B', 14.0)
    wt_sheet.set_column('B:C', 13.4)
    wt_sheet.set_column('C:D', 12.32)
    wt_sheet.set_column('D:E', 13.4)
    wt_sheet.set_column('E:F', 13.4)
    wt_sheet.set_column('F:G', 13.4)
    wt_sheet.set_column('G:H', 13.4)
    wt_sheet.set_column('H:I', 8.735)
    wt_sheet.set_column('I:J', 11.3675)
    wt_sheet.set_column('J:K', 19.7436)
    
def write2xlsx(allData,xrow):
    wt_sheet.write(xrow,0,allData['时间'], styleC)
    wt_sheet.write(xrow,1,allData['名称'], styleB)
    wt_sheet.write_number(xrow,2,allData['开'], styleB)
    wt_sheet.write_number(xrow,3,allData['现'], styleB)
    wt_sheet.write_number(xrow,4,allData['昨收'], styleB)
    wt_sheet.write_number(xrow,5,allData['最高'], styleB)
    wt_sheet.write_number(xrow,6,allData['最低'], styleB)
    wt_sheet.write_number(xrow,7,allData['涨跌'], styleB)
    wt_sheet.write_number(xrow,8,allData['涨跌百分比'], styleD)
    if('成交量' in allData.keys()):
        wt_sheet.write_number(xrow,9,allData['成交量'], styleB)
    
def writedqs2xlsx(allData, xrow):
    wt_sheet.write(xrow,0,allData['时间'], styleC)
    wt_sheet.write(xrow,1,allData['名称'], styleB)
    wt_sheet.write_number(xrow,3,allData['点数'], styleB)
    wt_sheet.write_number(xrow,7,allData['涨跌'], styleB)
    wt_sheet.write_number(xrow,8,allData['涨跌百分比'], styleD)
    
def writeshibor2xlsx(allData):
    wt_sheet.write(15,0,allData['时间'], styleC)
    wt_sheet.write_number(15,1,allData['O/N'], styleB)
    wt_sheet.write_number(15,2,allData['1W'], styleB)
    wt_sheet.write_number(15,3,allData['2W'], styleB)
    wt_sheet.write_number(15,4,allData['1M'], styleB)
    wt_sheet.write_number(15,5,allData['3M'], styleB)
    wt_sheet.write_number(15,6,allData['6M'], styleB)
    wt_sheet.write_number(15,7,allData['9M'], styleB)
    wt_sheet.write_number(15,8,allData['1Y'], styleB)
    
def writelibor2xlsx(allData):
    wt_sheet.write(19,0,allData['时间'], styleC)
    wt_sheet.write_number(19,1,allData['O/N'], styleB)
    wt_sheet.write_number(19,2,allData['1W'], styleB)
    wt_sheet.write_number(19,3,allData['1M'], styleB)
    wt_sheet.write_number(19,4,allData['2M'], styleB)
    wt_sheet.write_number(19,5,allData['3M'], styleB)
    wt_sheet.write_number(19,6,allData['6M'], styleB)
    wt_sheet.write_number(19,7,allData['12M'], styleB)
    
def get_libor():
    libor = {}
    response = requests.get('https://www.global-rates.com/interest-rates/libor/american-dollar/american-dollar.aspx')
    soup = BeautifulSoup(response.text, 'lxml')
    allData = soup.find('table', style='width:100%;margin:16px 0px 0px 0px;border:1px solid #CCCCCC;').find_all('td')
    libor['时间'] = datetime.datetime.strptime(soup.find('span',id='lbl_hdr2').string,'%m-%d-%Y').strftime('%Y-%m-%d')
    libor['O/N'] = float(allData[7].string[:7])
    libor['1W'] = float(allData[13].string[:7])
    libor['1M'] = float(allData[25].string[:7])
    libor['2M'] = float(allData[31].string[:7])
    libor['3M'] = float(allData[37].string[:7])
    libor['6M'] = float(allData[55].string[:7])
    libor['12M'] = float(allData[91].string[:7])
    print(libor)
    return libor
    
def get_shibor():
    shibor = {}
    response = requests.get('http://www.shibor.org/shibor/ShiborTendaysShow.do')
    soup = BeautifulSoup(response.text, 'lxml')
    allData = soup.find('table',class_='shiborquxian2').find('tr').find_all('td')
    shibor['时间'] = allData[0].string
    shibor['O/N'] = float(allData[1].string)
    shibor['1W'] = float(allData[2].string)
    shibor['2W'] = float(allData[3].string)
    shibor['1M'] = float(allData[4].string)
    shibor['3M'] = float(allData[5].string)
    shibor['6M'] = float(allData[6].string)
    shibor['9M'] = float(allData[7].string)
    shibor['1Y'] = float(allData[8].string)
    print(shibor)
    return shibor

class cdjkinfo(object):
    def __init__(self, id, type):
        self.id = id              #ID
        self.type = type            #类型
        
    def get_info(self):
        try:
            content = requests.get('http://hq.sinajs.cn/list=' + self.id).text                  #获取数据
        except:
            print("请检查网络连接！")
            os.system("PAUSE")
        str = content[(content.find('"'))+1:][:content[(content.find('"'))+1:].find('"')]       #整理字符串
        All_data = str.split(',')                                                               #分离数据
        if self.type == 0:                                                                      #股票
            self.name = All_data[0]                                                             #名称
            self.kd = float(All_data[1])                                                        #开
            self.xm = float(All_data[3])                                                        #收
            self.zouz = float(All_data[2])                                                      #昨收
            self.zvgc = float(All_data[4])                                                      #最高
            self.zvdi = float(All_data[5])                                                      #最低
            if self.id == 'sh000001':
                self.igjnll = float(All_data[8])                                                #成交量（单位：手）
            else:
                self.igjnll = float(All_data[8])/100
            self.time = datetime.datetime.strptime(All_data[30] + ' ' + All_data[31],'%Y-%m-%d %H:%M:%S')
        elif self.type == 1:                                                                    #期货
            self.name = All_data[0]                                                             #名称
            self.kd = float(All_data[2])                                                        #开
            self.xm = float(All_data[8])                                                        #收
            self.zouz = float(All_data[5])                                                      #昨收
            self.zvgc = float(All_data[3])                                                      #最高
            self.zvdi = float(All_data[4])                                                      #最低
            self.time = datetime.datetime.strptime(All_data[17] + ' ' +All_data[1],'%Y-%m-%d %H%M%S')
        elif self.type == 2:                                                                    #外盘期货
            self.name = All_data[13]                                                            #名称
            self.kd = float(All_data[8])                                                        #开
            self.xm = float(All_data[0])                                                        #收
            self.zouz = float(All_data[7])                                                      #昨收
            self.zvgc = float(All_data[4])                                                      #最高
            self.zvdi = float(All_data[5])                                                      #最低
            self.time = datetime.datetime.strptime(All_data[12] + ' ' + All_data[6],'%Y-%m-%d %H:%M:%S')
        elif self.type == 3:                                                                    #外汇
            self.name = All_data[9]                                                             #名称
            self.kd = float(All_data[5])                                                        #开
            self.xm = float(All_data[2])                                                        #收
            self.zouz = float(All_data[3])                                                      #昨收
            self.zvgc = float(All_data[6])                                                      #最高
            self.zvdi = float(All_data[7])                                                      #最低
            self.time = datetime.datetime.strptime(All_data[10] + ' ' + All_data[0],'%Y-%m-%d %H:%M:%S')
        elif self.type == 4:                                                                    #美股盘
            self.name = All_data[0]                                                             #名称
            self.xm = float(All_data[1])                                                        #收
            self.vhdp = float(All_data[2])                                                      #涨跌
            self.vhdpPercent = float(All_data[3])                                               #涨跌百分比
            self.time = datetime.datetime.today()
        if self.type != 4:
            self.vhdp = self.xm - self.zouz
            self.vhdpPercent = (self.xm - self.zouz)/self.zouz
            if self.type == 0:
                self.allToday = {"时间":self.time.strftime('%Y-%m-%d'), "名称": self.name, "开":self.kd, "现":self.xm, "昨收":self.zouz, "最高":self.zvgc, "最低":self.zvdi, "涨跌":self.vhdp, "涨跌百分比":self.vhdpPercent, "成交量": self.igjnll}
            else:
                self.allToday = {"时间":self.time.strftime('%Y-%m-%d'), "名称": self.name, "开":self.kd, "现":self.xm, "昨收":self.zouz, "最高":self.zvgc, "最低":self.zvdi, "涨跌":self.vhdp, "涨跌百分比":self.vhdpPercent}
        else:
            self.allToday = {"时间":self.time.strftime('%Y-%m-%d'), "名称": self.name, "点数":self.xm, "涨跌":self.vhdp, "涨跌百分比":self.vhdpPercent/100}
        print(self.allToday)
        
#上证指数
sz = {'id' : 'sh000001', 'type': '0'}

#大连大豆
douyi = {'id' : 'A0', 'type':'1'}
douer = {'id' : 'B0', 'type':'1'}

#纽约原油
nyyy = {'id' : 'hf_CL', 'type':'2'}

#上海原油
shyy = {'id' : 'SC1910', 'type':'1'}

#伦敦金
ldj = {'id' : 'hf_XAU', 'type':'2'}

#沪金
hj = {'id' : 'AU0', 'type':'1'}

#道琼斯
dqs = {'id' : 'int_dji', 'type':'4'}

#USDCNY
usdcny = {'id' : 'USDCNY', 'type':'3'}

writeInit2xlsx()

print("正在获取上证指数")
getsz = cdjkinfo(sz['id'], int(sz['type']))
getsz.get_info()
write2xlsx(getsz.allToday,1)
print('\n')

print("正在获取大连大豆")
getdouyi = cdjkinfo(douyi['id'], int(douyi['type']))
getdouer = cdjkinfo(douer['id'], int(douer['type']))
getdouyi.get_info()
write2xlsx(getdouyi.allToday,2)
getdouer.get_info()
write2xlsx(getdouer.allToday,3)
print('\n')

print("正在获取纽约原油")
getnyyy = cdjkinfo(nyyy['id'], int(nyyy['type']))
getnyyy.get_info()
write2xlsx(getnyyy.allToday,4)
print('\n')

print("正在获取上海原油")
getshyy = cdjkinfo(shyy['id'], int(shyy['type']))
getshyy.get_info()
write2xlsx(getshyy.allToday,5)
print('\n')

print("正在获取伦敦金")
getldj = cdjkinfo(ldj['id'], int(ldj['type']))
getldj.get_info()
write2xlsx(getldj.allToday,6)
print('\n')

print("正在获取沪金")
gethj = cdjkinfo(hj['id'], int(hj['type']))
gethj.get_info()
write2xlsx(gethj.allToday,7)
print('\n')

print("正在获取道琼斯")
getdqs = cdjkinfo(dqs['id'], int(dqs['type']))
getdqs.get_info()
writedqs2xlsx(getdqs.allToday, 9)
print('\n')

print("正在获取USDCNY")
getusdcny = cdjkinfo(usdcny['id'], int(usdcny['type']))
getusdcny.get_info()
write2xlsx(getusdcny.allToday,8)
print('\n')

print("正在获取Shibor")
shibor = get_shibor()
writeshibor2xlsx(shibor)
print('\n')

print("正在获取Libor（可能较慢，请耐心等待）")
libor = get_libor()
writelibor2xlsx(libor)
print('\n')

zixuan1 = input("请输入第一支自选股代码(Enter跳过): ")
if(zixuan1 != ''):  
    firstLetter = zixuan1[0]
    if(firstLetter == '6'):
        zixuan1 = 'sh' + zixuan1
    elif(firstLetter == '3' or firstLetter =='0'):
        zixuan1 = 'sz' + zixuan1
    else:
        print("请输入0，3，6开头的股票代码")
        os.system("PAUSE")
        exit()
    print("正在获取" + zixuan1)
    zixuanA = cdjkinfo(zixuan1, 0)
    zixuanA.get_info()
    write2xlsx(zixuanA.allToday,10)
    print('\n')
    
zixuan2 = input("请输入第二支自选股代码(Enter跳过): ")
if(zixuan2 != ''):  
    firstLetter = zixuan2[0]
    if(firstLetter == '6'):
        zixuan2 = 'sh' + zixuan2
    elif(firstLetter == '3' or firstLetter =='0'):
        zixuan2 = 'sz' + zixuan2
    else:
        print("请输入0，3，6开头的股票代码")
        os.system("PAUSE")
        exit()
    print("正在获取" + zixuan2)
    zixuanB = cdjkinfo(zixuan2, 0)
    zixuanB.get_info()
    write2xlsx(zixuanB.allToday,11)
    print('\n')


wt_book.close()
print("保存成功\n文件名：" + todaytime + '.xls\n')

os.system("PAUSE")