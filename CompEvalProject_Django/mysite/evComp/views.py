from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from evComp.models import Company, Profitability, Activity, Stability, Growth, Operation, Finance, Analysis, Report
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import json
import requests #pip install requests
from bs4 import BeautifulSoup as bs#pip install beautifulsoup4 & conda install html5lib
import re
import pandas as pd #pip install pandas
## pip install django-autocomplete-light
from selenium import webdriver
import pandas as pd
import time
from urllib.request import urlopen
import numpy as np
from datetime import timedelta, datetime, date
from ast import literal_eval
from io import StringIO



class evCompModelView(TemplateView):
    # books/templates/books/index.html
    template_name = 'evComp/index.html'

def doorConstruction(request):
    print("-----------------doorConstruction()---------------------")
    selectedCode = request.GET["code"]
    print(selectedCode)
    return render(request, 'evComp/door.html', {"selectedCode" : selectedCode})

def FinRatioAnalysis(request):
    #공통코드
    analysisCode = request.GET["param"]
    print(analysisCode)
    ticker = analysisCode
    pat_enc = re.compile("encparam: '(.*)'")
    url = "https://companyinfo.stock.naver.com/v1/company/c1040001.aspx?cmp_cd={}&cn".format(ticker)
    html = requests.get(url).text
    encparam = pat_enc.search(html).group(1)

    #수익성 지표 코드
    profitUrl = "https://companyinfo.stock.naver.com/v1/company/cF4002.aspx?cmp_cd={}&frq=0&rpt=1&finGubun=IFRSS&frqTyp=0&cn=&encparam={}".format(ticker, encparam)
    headers = {"Referer": "HACK"}
    profitHtml = requests.get(profitUrl, headers=headers).text
    profitSoup = bs(profitHtml, "html.parser") #"html5lib"
    #profitSoup = profitSoup.select("body")[0].text
    profitJson = json.loads(profitSoup.text)
    profitDate = profitJson["YYMM"]
    profitData = profitJson["DATA"]

    profitCol = ["date"]
    profitRow1 = [profitDate[0].replace('(IFRS별도)',"")]
    profitRow2 = [profitDate[1].replace('(IFRS별도)',"")]
    profitRow3 = [profitDate[2].replace('(IFRS별도)',"")]
    profitRow4 = [profitDate[3].replace('(IFRS별도)',"")]
    profitRow5 = [profitDate[4].replace('(IFRS별도)',"")]
    profitList = [profitCol, profitRow1, profitRow2, profitRow3, profitRow4, profitRow5]
    try:
        for i in range(len(profitData)):
            profitDataYear = profitData[i]
            if profitDataYear["P_ACCODE"] == None:
                profitCol.append(profitDataYear["ACC_NM"])
                data1 = round(float(profitDataYear["DATA1"]),2)
                profitRow1.append(data1)
                data2 = round(float(profitDataYear["DATA2"]),2)
                profitRow2.append(data2)
                data3 = round(float(profitDataYear["DATA3"]),2)
                profitRow3.append(data3)
                data4 = round(float(profitDataYear["DATA4"]),2)
                profitRow4.append(data4) 
                data5 = round(float(profitDataYear["DATA5"]),2)
                profitRow5.append(data1)
    except:
        pass
    print(profitList)

    profitArray = (profitList)

#성장성 지표
    growthUrl = "https://companyinfo.stock.naver.com/v1/company/cF4002.aspx?cmp_cd={}&frq=0&rpt=2&finGubun=IFRSS&frqTyp=0&cn=&encparam={}".format(ticker, encparam)

    headers = {"Referer": "HACK"}
    growthHtml = requests.get(growthUrl, headers=headers).text
    growthSoup = bs(growthHtml, "html.parser")
    growthJson = json.loads(growthSoup.text)
    growthDate = growthJson["YYMM"]
    growthData = growthJson["DATA"]
    growthCol = ["date"]
    growthRow1 = [growthDate[0].replace('(IFRS별도)',"")]
    growthRow2 = [growthDate[1].replace('(IFRS별도)',"")]
    growthRow3 = [growthDate[2].replace('(IFRS별도)',"")]
    growthRow4 = [growthDate[3].replace('(IFRS별도)',"")]
    growthRow5 = [growthDate[4].replace('(IFRS별도)',"")]
    growthList = [growthCol, growthRow1, growthRow2, growthRow3, growthRow4, growthRow5]
    try:
        for i in range(len(growthData)):
            growthDataYear = growthData[i]
            if growthDataYear["P_ACCODE"] == None:
                growthCol.append(growthDataYear["ACC_NM"])
                data1 = round(float(growthDataYear["DATA1"]),2)
                growthRow1.append(data1)
                data2 = round(float(growthDataYear["DATA2"]),2)
                growthRow2.append(data2)
                data3 = round(float(growthDataYear["DATA3"]),2)
                growthRow3.append(data3)
                data4 = round(float(growthDataYear["DATA4"]),2)
                growthRow4.append(data4) 
                data5 = round(float(growthDataYear["DATA5"]),2)
                growthRow5.append(data1)
    except:
        pass
    print(growthList)

    growthArray = (growthList)
    #growthContext = {'growthArray': json.dumps(growthArray)}

# 안정성 지표
    stabilityUrl = "https://companyinfo.stock.naver.com/v1/company/cF4002.aspx?cmp_cd={}&frq=0&rpt=3&finGubun=IFRSS&frqTyp=0&cn=&encparam={}".format(ticker, encparam)
    headers = {"Referer": "HACK"}
    stabilityHtml = requests.get(stabilityUrl, headers=headers).text
    stabilitySoup = bs(stabilityHtml, "html.parser")
    stabilityJson = json.loads(stabilitySoup.text)
    stabilityDate = stabilityJson["YYMM"]

    stabilityData = stabilityJson["DATA"]
    stabilityCol = ["date"]
    stabilityRow1 = [stabilityDate[0].replace('(IFRS별도)',"")]
    stabilityRow2 = [stabilityDate[1].replace('(IFRS별도)',"")]
    stabilityRow3 = [stabilityDate[2].replace('(IFRS별도)',"")]
    stabilityRow4 = [stabilityDate[3].replace('(IFRS별도)',"")]
    stabilityRow5 = [stabilityDate[4].replace('(IFRS별도)',"")]
    stabilityList = [stabilityCol, stabilityRow1, stabilityRow2, stabilityRow3, stabilityRow4, stabilityRow5]
    try:
        for i in range(len(stabilityData)):
            stabilityDataYear = stabilityData[i]
            if stabilityDataYear["P_ACCODE"] == None:
                stabilityCol.append(stabilityDataYear["ACC_NM"])
                data1 = round(float(stabilityDataYear["DATA1"]),2)
                stabilityRow1.append(data1)
                data2 = round(float(stabilityDataYear["DATA2"]),2)
                stabilityRow2.append(data2)
                data3 = round(float(stabilityDataYear["DATA3"]),2)
                stabilityRow3.append(data3)
                data4 = round(float(stabilityDataYear["DATA4"]),2)
                stabilityRow4.append(data4) 
                data5 = round(float(stabilityDataYear["DATA5"]),2)
                stabilityRow5.append(data1)
    except:
        pass

    print(stabilityList)

    stabilityArray = (stabilityList)
    #stabilityContext = {'stabilityArray': json.dumps(stabilityArray)}

# 활동성 지표
    activityUrl = "https://companyinfo.stock.naver.com/v1/company/cF4002.aspx?cmp_cd={}&frq=0&rpt=4&finGubun=IFRSS&frqTyp=0&cn=&encparam={}".format(ticker, encparam)
    headers = {"Referer": "HACK"}
    activityHtml = requests.get(activityUrl, headers=headers).text
    activitySoup = bs(activityHtml, "html.parser")
    activityJson = json.loads(activitySoup.text)
    activityDate = activityJson["YYMM"]

    activityData = activityJson["DATA"]
    activityCol = ["date"]
    activityRow1 = [activityDate[0].replace('(IFRS별도)',"")]
    activityRow2 = [activityDate[1].replace('(IFRS별도)',"")]
    activityRow3 = [activityDate[2].replace('(IFRS별도)',"")]
    activityRow4 = [activityDate[3].replace('(IFRS별도)',"")]
    activityRow5 = [activityDate[4].replace('(IFRS별도)',"")]
    activityList = [activityCol, activityRow1, activityRow2, activityRow3, activityRow4, activityRow5]
    try:
        for i in range(len(activityData)):
            activityDataYear = activityData[i]
            if activityDataYear["P_ACCODE"] == None:
                activityCol.append(activityDataYear["ACC_NM"])
                data1 = round(float(activityDataYear["DATA1"]),2)
                activityRow1.append(data1)
                data2 = round(float(activityDataYear["DATA2"]),2)
                activityRow2.append(data2)
                data3 = round(float(activityDataYear["DATA3"]),2)
                activityRow3.append(data3)
                data4 = round(float(activityDataYear["DATA4"]),2)
                activityRow4.append(data4) 
                data5 = round(float(activityDataYear["DATA5"]),2)
                activityRow5.append(data1)
    except:
        pass

    print(activityList)

    activityArray = (activityList)
    #activityContext = {'activityArray': json.dumps(activityArray)}
    
    context = {'profitArray': json.dumps(profitArray), 'growthArray': json.dumps(growthArray), 'stabilityArray': json.dumps(stabilityArray), 'activityArray': json.dumps(activityArray)}
    return render(request, 'evComp/ratioChart.html', context)


def analysisResult(request):
    
    company_code = request.GET["param"]
    ticker = company_code
    
    # 고정 변수
    # 현대증권 경제 보고서 참조(파일명: 현대증권경기예측.pdf //8 p.g " 국내 잠재성장률은 2016~2020년 중 2%대 진입이 예상되며... ")
    I_Growth = 0.02
    GDPsite = pd.read_html(
        'http://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=2736', header=0)
    GDPgrowthRate = GDPsite[1].values[1][-2]*0.01

    # 회사명 : 회사종목코드

    #company_name = "삼성전자" 

    # 재무제표 네이버 크롤링

    python_dict = literal_eval("{'a': 1}")

    rpt = [0, 1, 2]  # 0 -- IS / 1 -- BS / 2 -- CF
    freq = 0  # 0 -- yearly/ 1 -- quarter

    pat_enc = re.compile("encparam: '(.*)'")
    # pat_id = re.compile("id: '([a-zA-Z0-9]*)' ?", re.IGNORECASE)
    url = "https://companyinfo.stock.naver.com/v1/company/c1030001.aspx?cmp_cd={}&cn".format(
        company_code)
    html = requests.get(url).text
    encparam = pat_enc.search(html).group(1)

    def FinancialStatement(company_code, freq, num, encparam):
        profitUrl = "https://companyinfo.stock.naver.com/v1/company/cF3002.aspx?cmp_cd={}&frq={}&rpt={}&finGubun=IFRSS&frqTyp={}&cn=&encparam={}".format(
            company_code, freq, num, freq, encparam)
        headers = {
            "Referer": "HACK"
        }
        # print(profitUrl)
        profitHtml = requests.get(profitUrl, headers=headers).text
        profitSoup = bs(profitHtml, "html5lib")
        profitSoup = profitSoup.select("body")[0].text
        profitJson = json.loads(profitSoup)

        # 정규표현식 - yet
        # removeDotsAndAsterisk = re.sub("(\.*|\**)","",str(profitJson))
        # eval_fix = re.sub("(\,\s\'QOQ_COMMENT\'(.+)\s1\})","}",removeDotsAndAsterisk)
        # profitJson1=literal_eval(eval_fix)

        # profitDate = profitJson["YYMM"]
        profitData = profitJson["DATA"]
        Dframe = pd.DataFrame(profitData, dtype='float')
        Dframe.fillna(0, inplace=True)
        return Dframe

    def Merge(FS, FS_quarter):
        FS_left = FS[['ACC_NM', 'DATA2', 'DATA3', 'DATA4', 'DATA5']]
        FS_right = FS_quarter[['DATA5']]
        FS_right.columns = ['DATA6']
        FS_right = FS_right*(4/3)
        FinancialStatement = FS_left.join(FS_right, how='outer')

        return FinancialStatement

    for num in rpt:
        if(num == 0):
            IS = FinancialStatement(company_code, freq, num, encparam)
            freq += 1
            IS_quarter = FinancialStatement(company_code, freq, num, encparam)
            freq = 0
            IS = Merge(IS, IS_quarter)
            IS.rename({'ACC_NM': '포괄손익계산서', 'DATA2': '2014/12', 'DATA3': '2015/12',
                    'DATA4': '2016/12', 'DATA5': '2017/12', 'DATA6': '2018/12'}, axis=1, inplace=True)
            IS_timesMillion = IS.select_dtypes(exclude=['object']) * 100000000
            IS[IS_timesMillion.columns] = IS_timesMillion

        elif(num == 1):
            BS = FinancialStatement(company_code, freq, num, encparam)
            freq += 1
            BS_quarter = FinancialStatement(company_code, freq, num, encparam)
            freq = 0
            BS = Merge(BS, BS_quarter)
            BS.rename({'ACC_NM': '재무상태표', 'DATA2': '2014/12', 'DATA3': '2015/12',
                    'DATA4': '2016/12', 'DATA5': '2017/12', 'DATA6': '2018/12'}, axis=1, inplace=True)
            BS_timesMillion = BS.select_dtypes(exclude=['object']) * 100000000
            BS[BS_timesMillion.columns] = BS_timesMillion

        elif(num == 2):
            CF = FinancialStatement(company_code, freq, num, encparam)
            freq += 1
            CF_quarter = FinancialStatement(company_code, freq, num, encparam)
            freq = 0
            CF = Merge(CF, CF_quarter)
            CF.rename({'ACC_NM': '현금흐름표', 'DATA2': '2014/12', 'DATA3': '2015/12',
                    'DATA4': '2016/12', 'DATA5': '2017/12', 'DATA6': '2018/12'}, axis=1, inplace=True)
            CF_timesMillion = CF.select_dtypes(exclude=['object']) * 100000000
            CF[CF_timesMillion.columns] = CF_timesMillion

    # 총 차입금

    ST_borrowing = BS.loc[BS['재무상태표'] == '....단기차입금']
    LT_borrowing = BS.loc[BS['재무상태표'] == '....장기차입금']
    for idx, col in enumerate(ST_borrowing.columns):
        if(idx == 0):
            pass
        elif col in LT_borrowing.columns:
            ST_borrowing[col] = ST_borrowing[col].values + \
                LT_borrowing[col].values
    Total_borrowing = ST_borrowing.reset_index().iloc[0][2:]
    BW = Total_borrowing.tolist()

    # Beta -- 수정 필요. 아래 링크 참조
    # https://nbviewer.jupyter.org/gist/FinanceData/1cd9cf4b8198e7924392dca3ace46bfe

    html = "https://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd=005930&cn="
    BetaCrawler = pd.read_html(html)
    beta = float(BetaCrawler[1].values[5][1])

    # 보유 주식량
    # 재무제표 긁을때 같이하게 수정 필요

    def get_date_str(s):
        date_str = ''
        r = re.search("\d{4}/\d{2}", s)
        if r:
            date_str = r.group()
            date_str = date_str.replace('/', '-')

        return date_str

    '''
    * code: 종목코드
    * fin_type(종류): 0=주재무제표(기본), 1=GAAP개별, 2=GAAP연결, 3=IFRS별도, 4=FRS연결
    * freq_type(기간): Y=년(기본), Q=분기
    '''

    def get_finstate_naver(code, fin_type='0', freq_type='Y'):
        # encparam, encid  추출
        url_tmpl = 'http://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd=%s'
        url = url_tmpl % (code)

        html_text = requests.get(url).text
        if '기업재무정보 접속장애' in html_text:
            return None

        encparam = re.findall("encparam: '(.*?)'", html_text)[0]
        encid = re.findall("id: '(.*?)'", html_text)[0]

        #  재무데이터 표 추출
        url_tmpl = 'http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?' \
            'cmp_cd=%s&fin_typ=%s&freq_typ=%s&encparam=%s&id=%s'

        url = url_tmpl % (code, fin_type, freq_type, encparam, encid)

        header = {
            'Referer': 'https://companyinfo.stock.naver.com/v1/company/c1010001.aspx',
        }

        html_text = requests.get(url, headers=header).text
        dfs = pd.read_html(StringIO(html_text))
        df = dfs[1]
        if df.iloc[0, 0].find('해당 데이터가 존재하지 않습니다') >= 0:
            return None

        cols = list(df.columns)
        new_cols = []
        new_cols.append(cols[0][0])
        new_cols += [c[1] for c in cols[:-1]]
        df.columns = new_cols
        df.set_index('주요재무정보', inplace=True)
        df.columns = [get_date_str(x) for x in df.columns]

        return df

    df = get_finstate_naver(company_code, fin_type='3', freq_type='Q')
    NO = df['2018-09'][-1]

    # 무위험 이자율 계산
    # e나라지표 사이트에서 국고채 평균 10년 금리 추출
    url = "http://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1073"
    html = urlopen(url)
    source = html.read()
    html.close()
    soup = bs(source, "html5lib")
    # 10년물 국공채 평균 이자율 #매달
    Rf = float(soup.select(
        "tbody > tr > td[data-id='td_107301_13']")[2].string)/100

    # kospi 5년치 시장수익률(Rm)
    # kospi200 일일 주가지수 crawling
    url = 'https://finance.naver.com/sise/sise_index_day.nhn?code=KPI200'
    html = urlopen(url)
    source = bs(html.read(), "html.parser")

    maxPage = source.find_all("table", align="center")
    mp = maxPage[0].find_all("td", class_="pgRR")
    mpNum = int(mp[0].a.get('href')[-3:])

    pageNum, Kospi200diff = [1, 205], []
    for i in range(len(pageNum)):
        url = 'https://finance.naver.com/sise/sise_index_day.nhn?code=KPI200' + \
            '&page=' + str(pageNum[i])
        html = urlopen(url)
        source = bs(html.read(), "html.parser")
        srlists = source.find_all("tr")
        isCheckNone = None
        # print(float(srlists[2].find("td",class_="number_1").text))
        Kospi200diff.append(
            float(srlists[2].find("td", class_="number_1").text))

    Rm = (Kospi200diff[0]-Kospi200diff[1])*0.01

    # Rm-Rf가 마이너스 값이 나올경우 무성장 가정
    # if(Rm-Rf < 0):
    #    Rm=0
    #    Rf=0

    #  주식 수익률 계산
    Re = Rf + (beta * (Rm - Rf))

    # CFO
    g1 = CF.loc[(CF['현금흐름표'] == '영업활동으로인한현금흐름')]
    CFO = g1.iloc[0, 1:]

    # INT
    g2 = CF.loc[(CF['현금흐름표'] == '........금융비용')]
    INT = g2.iloc[0, 1:]

    # TAXRATE

    # 법인세비용
    g3 = IS.loc[(IS['포괄손익계산서'] == '법인세비용')]
    g3 = g3.iloc[0, 1:]

    # 법인세비용차감전계속사업이익
    g4 = IS.loc[(IS['포괄손익계산서'] == '법인세비용차감전계속사업이익')]
    g4 = g4.iloc[0, 1:]

    corporateTaxRate = g3/g4

    # 세율이 마이너스일 경우는 기업이 국가에게 환급받은 경우 -> 우리나라 법인세율(20%) 적용
    for i in range(len(corporateTaxRate)):
        if(corporateTaxRate[i] < 0):
            corporateTaxRate[i] = 0.2
    TAXRATE = corporateTaxRate

    # CAPEX

    g5 = CF.loc[(CF['현금흐름표'] == '투자활동으로인한현금흐름')]
    CAPEX = g5.iloc[0, 1:]

    a = [CFO, INT, TAXRATE, CAPEX]
    b = pd.DataFrame(a)
    if(b.iloc[0, [4]].values[0]+b.iloc[3, [4]].values[0] < 0):
        b.iloc[3, [4]] = 0
    c = b.iloc[0]+b.iloc[1]*(1-b.iloc[2])+b.iloc[3]  # FCFF계산
    FCFF = b.append([c])
    FCFF = FCFF.append(FCFF.iloc[4].pct_change())
    FCFF.index = ["CFO", "INT", "TAXRATE", "CAPEX", "FCFF", "FCFF_growthRate"]

    # FCFF_G = FCFF.iloc[5,[3,4]].mean() #경우의 수 1 : 해당기업의 성장률(변동이 심함)
    FCFF_G = GDPgrowthRate  # 경우의 수 2 : gdp성장률로 대체

    # 10년 예측 재무제표

    FUTURE = ['2019', '2020', '2021', '2022', '2023',
            '2024', '2025', '2026', '2027', '2028']

    # 미래 10년 예측 FCFF
    ExpFCFF = FCFF.iloc[4, [4]]
    FUTUREFCFF = []
    for j in range(10):
        ExpFCFF = (FCFF_G + 1)*ExpFCFF
        FUTUREFCFF.append(ExpFCFF.round(2))

    FUTUREFCFF1 = [{FUTURE[i]:FUTUREFCFF[i]
        for i in range(10)}]  # df=df.round(2)

    F_FCFF = pd.DataFrame(FUTUREFCFF1)

    # WACC 계산
    eRatio = BS.loc[(BS['재무상태표'] == '자본총계')].values[0][1:][-1] / \
        BS.loc[(BS['재무상태표'] == '자산총계')].values[0][1:][-1]  # 자본 비율
    dRatio = 1 - eRatio  # 부채비율
    # iRate = FCFF.iloc[1,4] / BW[-1] # 차입금/이자율
    iRate = .0421
    taxR = FCFF.iloc[2].mean()  # 법인 세율
    WACC = eRatio * Re + iRate*(1-taxR)*dRatio

    WACC = 0.045
    # if(I_Growth > WACC): #r-g가 0보다 작으면 r만 적용. 분자(1+g)도 g가 0으로 적용. (무성장을 가정하는 경우)
    #    I_Growth=0

    # Terminal Value 및 FCFF 현재가치 계산
    df = F_FCFF
    df.iloc[0][-1] = df.iloc[0][-1]+df.iloc[0, 9]*(1+I_Growth)/(WACC-I_Growth)
    p = pd.DataFrame([np.zeros(10)], columns=['2019', '2020', '2021',
                                            '2022', '2023', '2024', '2025', '2026', '2027', '2028'])
    df = df.append(p, ignore_index=True)
    DiscountedFCFF = []
    for i in range(10):
        DiscountedFCFF.append(df.iloc[0][i]/((1+WACC)**(i+1)))

    df.iloc[1] = DiscountedFCFF
    EnterpriseValue = df.iloc[1].sum()
    EquityValue = EnterpriseValue-BW[-1]
    StockPrice = EquityValue / NO

    #오늘 해당기업 주가
    # url = 'http://finance.naver.com/item/sise_day.nhn?code={0}'.format(company_code)
    # html = urlopen(url)
    # source = bs(html.read(), "html.parser")
    # srlists = source.find_all("td")
    # todayP=srlists
    #todayP = int(srlists[2].text.replace(',', ''))

    #opinion=""
    # 주식 트레이딩 의사결정

    #int(StockPrice.values.item())
    # if(StockPrice.values.item() > todayP ):
    #     opinion = "BUY"
    # elif(StockPrice.values.item() > (todayP * 0.8)):
    #     opinion = "HOLD"
    # else:
    #     opinion = "SELL"

    # if(int(StockPrice.values.item())>= (int(todayP) * 1.2)):
    #     opinion = "BUY"
    # elif(StockPrice.values.item() >= (int(todayP) * 0.8)):
    #     opinion = "HOLD"
    # else:
    #     opinion = "SELL"

    DecisionArray= [[' '],['DCF적용 예상 주당 가치', round(StockPrice[0],2).astype(str)],
                               #['현재 거래가격', str(todayP)]
                            #['주식에 대한 의견',opinion]
                            ]

    global LargeBucket
    LargeBucket1=[]
    for i in range(len(IS)):
        SmallBucket=[]
        for idx, k in enumerate(IS.iloc[i]):
            SmallBucket.append(str(k))
            if(idx == len(IS.iloc[i])-1):
                LargeBucket1.append(SmallBucket)
    
    ISArray=LargeBucket1

    global LargeBucket
    LargeBucket2=[]
    for i in range(len(IS)):
        SmallBucket=[]
        for idx, k in enumerate(IS.iloc[i]):
            SmallBucket.append(str(k))
            if(idx == len(IS.iloc[i])-1):
                LargeBucket2.append(SmallBucket)
    
    BSArray=LargeBucket2

    global LargeBucket
    LargeBucket3=[]
    for i in range(len(IS)):
        SmallBucket=[]
        for idx, k in enumerate(IS.iloc[i]):
            SmallBucket.append(str(k))
            if(idx == len(IS.iloc[i])-1):
                LargeBucket3.append(SmallBucket)
    
    CFArray=LargeBucket3
    
    
    context = {'DecisionArray': json.dumps(DecisionArray), 'ISArray': json.dumps(ISArray), 'BSArray': json.dumps(BSArray), 'CFArray': json.dumps(CFArray)}
    return render(request, 'evComp/result.html', context)

def ajaxTag(request):
    search = request.GET['q']
    #request.setCharacterEncoding("UTF-8")
    company_list = Company.objects.filter(name__istartswith = search)   #name__icontains
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(search)
    print(company_list)
    
    arrayList = []
    for i in company_list:
        #print(i.name, "-----------------------",i.code)
        array = {}
        array["id"] = i.id
        array["name"] = i.name
        array["code"] = i.code
        print(array)
        arrayList.append(array)
    print(arrayList[0]["name"])
    
    print("************************")
    print(company_list)
    print(type(company_list))
    context = {'arrayList' : arrayList}
    print("***************************")
    print(context)
    print(type(context))
    return HttpResponse(json.dumps(context), content_type="application/json")

