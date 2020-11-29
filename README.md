> 去年投资学课上老师要求每天记录市场数据，由于本人懒癌发作，就写了这个数据自动获取程序
>
> 已完成船新版本的开发（练手Github Actions）

<a title="GitHub Stars" target="_blank" href="https://github.com/huanghaozi/autoInvestmentLog/stargazers"><img src="https://img.shields.io/github/stars/huanghaozi/autoInvestmentLog.svg?label=Star&style=social"></a>  
# 功能
:point_right: 每天晚上9点自动抓取全量**A股、期货、Shibor、Libor**实时数据

:point_right: 可自动提取所需数据，并使用**Server酱**推送至微信

:point_right: 无需下载程序或安装繁杂的环境

# 效果
![](https://cdn.jsdelivr.net/gh/huanghaozi/autoInvestmentLog@master/preview.jpg)

# 使用流程
## 注册Github
[https://github.com](https://github.com)
## 注册Server酱并绑定微信
[http://sc.ftqq.com](http://sc.ftqq.com)
## Fork此项目

点击右上角Fork等待完成即可

## 新建Secrets存入Token

转到自己Fork的项目下，点击项目的Settings--Secrets，新建一个Secret，名称为SCKEY，并将Server酱中的Token复制进其内容，保存。

## 编辑config.ini

回到自己Fork的项目主页，点开根目录下的config.ini，点击右上角的铅笔按钮进行编辑，调整需要的数据。

## 测试
点开自己项目主页的Issue页面，随便New个Issue（标题随便起），即可开始爬取数据，进入Actions页面可查看数据获取进度，约5分钟获取完，即可在微信里看到推送来的信息。