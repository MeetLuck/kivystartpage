import openpyxl
from socket import gethostname
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass
@dataclass
class Card:
    rank: str = 'Q'
    suit: str = 'hearts'

A_day1 = datetime(2022,1,31)

today = datetime.today()
default_date=(today.month,today.day, today.year)
days = '월 화 수 목 금 토 일'.split()
def get_weekday(date):
    return days[date.weekday()]

weekday = get_weekday(today)

def get_monthlyfile(workdate):
    workmonth = workdate.strftime("%Y%m")
    # NOTE gethostname
    if gethostname() == 'main':
        monthlyfile = r'D:\01.업무문서\04.출근부 관련\02.각 조별 월별 출근부\{} A,B,C조별 월별출근부(반포자이).xlsx'.format(workmonth)
    elif gethostname() =='Sub':
        monthlyfile = r'\\Main\d\01.업무문서\04.출근부 관련\02.각 조별 월별 출근부\{} A,B,C조별 월별출근부(반포자이).xlsx'.format(workmonth)
    elif gethostname() =='meetluck':
        monthlyfile = r'D:\Documents\d\01.업무문서\04.출근부 관련\02.각 조별 월별 출근부\{} A,B,C조별 월별출근부(반포자이).xlsx'.format(workmonth)
        #raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')
    return monthlyfile

def get_minwonfile():
    if gethostname() == 'main':
        minwonfile = r'D:\01.업무문서\000. 민원처리내역.xlsx'
    elif gethostname() =='Sub':
        minwonfile = r'\\Main\d\01.업무문서\000. 민원처리내역.xlsx'
    elif gethostname() =='meetluck':
        minwonfile = r'D:\Documents\d\01.업무문서\000. 민원처리내역.xlsx'
        #raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')
    return minwonfile

def get_wonhyungfile():
    if gethostname() == 'main':
        wonhyungfile = r'D:\01.업무문서\00.원형도로 단속일지(최종본).xlsx'
    elif gethostname() =='Sub':
        wonhyungfile = r'\\Main\d\01.업무문서\00.원형도로 단속일지(최종본).xlsx'
    elif gethostname() =='meetluck':
        wonhyungfile = r'\\Main\d\01.업무문서\00.원형도로 단속일지(최종본).xlsx'
        #raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')
    return wonhyungfile

def get_todofile():
    if gethostname() == 'main':
        return r'D:\A조\todo.txt'
    elif gethostname() =='Sub':
        return r'D:\01.A조\sub박종우\banpo\todo.txt'
    elif gethostname() =='meetluck':
        return r'D:\Documents\d\todo.txt'
        #raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')
    return todofile

def get_hpscanfile():
    if gethostname() == 'main':
        raise Exception('Invalid host name' + gethostname())
        return r'C:\Program Files (x86)\HP\HP OfficeJet Pro 8710\bin\HPScan.exe'
    elif gethostname() =='Sub':
        return r'C:\Program Files (x86)\HP\HP OfficeJet Pro 8710\bin\HPScan.exe'
    elif gethostname() =='meetluck':
        raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')

def get_snappingtoolfile():
        return r'C:\WINDOWS\system32\SnippingTool.exe'

def get_dbfile():
    if gethostname() == 'main':
        dbfile = r'D:\01.A조\sub박종우\DB Browser for SQLite\DB Browser for SQLite.exe'
        raise Exception('Invalid host name')
    elif gethostname() =='Sub':
        dbfile = r'D:\01.A조\sub박종우\DB Browser for SQLite\DB Browser for SQLite.exe'
    elif gethostname() =='meetluck':
        raise Exception('Invalid host name' + gethostname())
        dbfile = r'D:\Documents\d\todo.txt'
    else:
        raise Exception('Invalid host name')
    return dbfile

def get_minwondbfile():
    if gethostname() == 'main':
        raise Exception('Invalid host name')
        return r'D:\01.A조\sub박종우\banpo\minwondb.py'
    elif gethostname() =='Sub':
        return r'D:\01.A조\sub박종우\banpo\minwondb.py'
        #dbfile = r'D:\01.A조\sub박종우\DB Browser for SQLite\DB Browser for SQLite.exe'
    elif gethostname() =='meetluck':
        raise Exception('Invalid host name' + gethostname())
        return r'D:\01.A조\sub박종우\banpo\minwondb.py'
    else:
        raise Exception('Invalid host name')

def get_daypatrolefile():
    if gethostname() == 'main':
        raise Exception('Invalid host name')
        return r'D:\01.A조\sub박종우\banpo\day_patrol.png'
    elif gethostname() =='Sub':
        return r'D:\01.A조\sub박종우\banpo\day_patrol.png'
    elif gethostname() =='meetluck':
        return r'D:\Documents\banpo\day_patrol.png'
    else:
        raise Exception('Invalid host name')

def get_nightpatrolefile():
    if gethostname() == 'main':
        raise Exception('Invalid host name')
        return r'D:\01.A조\sub박종우\banpo\night_patrol.png'
    elif gethostname() =='Sub':
        return r'D:\01.A조\sub박종우\banpo\night_patrol.png'
    elif gethostname() =='meetluck':
        return r'D:\Documents\banpo\night_patrol.png'
    else:
        raise Exception('Invalid host name')

def get_dong_postfile():
    if gethostname() == 'main':
        raise Exception('Invalid host name')
        return r'D:\01.A조\sub박종우\banpo\dong_post.png'
    elif gethostname() =='Sub':
        return r'D:\01.A조\sub박종우\banpo\dong_post.png'
    elif gethostname() =='meetluck':
        return r'D:\Documents\banpo\dong_post.png'
    else:
        raise Exception('Invalid host name')

def get_gitfile():
    if gethostname() == 'main':
        raise Exception('Invalid host name')
        gitfile = r'D:\01.A조\sub박종우\GitPortable\GitBashPortable.exe'
    elif gethostname() =='Sub':
        gitfile = r'D:\01.A조\sub박종우\GitPortable\GitBashPortable.exe'
    elif gethostname() =='meetluck':
        raise Exception('Invalid host name' + gethostname())
        gitfile = r'D:\01.A조\sub박종우\GitPortable\App\Git\git-bash.exe'
    else:
        raise Exception('Invalid host name')
    return gitfile

def get_dailyreportfile(workdate):
    from datetime import timedelta
    workmonth =workdate.strftime("%m")
    workday1  =workdate.strftime("%Y%m%d")
    workday2  =(workdate + timedelta(days=1)).strftime("%Y%m%d")
    #print(workmonth)
    #print(workday1,workday2)
    if gethostname() == 'main':
        dailyreportfile1 = r'D:\01.업무문서\01.일일상황보고(상황실)\2022년{}월\일일 상황 보고 {}.xlsx'.format(workmonth,workday1)
        dailyreportfile2 = r'D:\01.업무문서\01.일일상황보고(상황실)\2022년{}월\일일 상황 보고 {}.xlsx'.format(workmonth,workday2)
    elif gethostname() =='Sub':
        dailyreportfile1 = r'\\Main\d\01.업무문서\01.일일상황보고(상황실)\2022년{}월\일일 상황 보고 {}.xlsx'.format(workmonth,workday1)
        dailyreportfile2 = r'\\Main\d\01.업무문서\01.일일상황보고(상황실)\2022년{}월\일일 상황 보고 {}.xlsx'.format(workmonth,workday2)
    elif gethostname() =='meetluck':
        dailyreportfile1 = r'D:\Documents\d\01.업무문서\01.일일상황보고(상황실)\2022년{}월\일일 상황 보고 {}.xlsx'.format(workmonth,workday1)
        dailyreportfile2 = r'D:\Documents\d\01.업무문서\01.일일상황보고(상황실)\2022년{}월\일일 상황 보고 {}.xlsx'.format(workmonth,workday2)
        #raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')
    return dailyreportfile1, dailyreportfile2

#ws = wb['조별연차표'] 


def get_offworkers(workdate):
    wb = openpyxl.load_workbook( get_monthlyfile(workdate), data_only=True )
    ws = wb['조별연차표'] 
    dayteam, nightteam = get_workteam(workdate)
    def R1C1(row,col):
        return ws.cell(row,col)
    for r in [4,8,12,16,20]:
        for c in [2,3,4,5,6,7,8]:
            if R1C1(r,c).value == workdate.day:
                wb.close()
                off_day,off_night = R1C1(r+1,c).value, R1C1(r+2,c).value
                if off_day   == None : off_day='없음'
                if off_night == None : off_night='없음'
                return ( [dayteam,off_day], [nightteam,off_night] )
    # [A1 , "홍길동'] , [B1, "홍길순"]
    raise Exception('unknown error') 

def get_dayornight(date):
    diff = (datetime(date.year,date.month,date.day) - A_day1).days
    dayornight=['day1','day2','night1','night2','off1','off2']
    return dayornight[diff % 6]

def get_workteam(date):
    diff = (datetime(date.year,date.month,date.day) - A_day1).days
    if diff % 6 == 0:
        dayteam,nightteam = "A1","B1"
    if diff % 6 == 1:
        dayteam,nightteam = "A2","B2"
    if diff % 6 == 2:
        dayteam,nightteam = "C1","A1"
    if diff % 6 == 3:
        dayteam,nightteam = "C1","A2"
    if diff % 6 == 4:
        dayteam,nightteam = "B1","C1"
    if diff % 6 == 5:
        dayteam,nightteam = "B2","C2"
    #print(dayteam,nightteam)
    return (dayteam,nightteam)

#NOTE folders -------------------------------------------------------------------------------------------------
def get_workfolder():
    if gethostname() == 'main':
       return r'D:\01.업무문서'
    elif gethostname() =='Sub':
       return r'\\Main\d\01.업무문서'
    elif gethostname() =='meetluck':
       return  r'D:\Documents\d\01.업무문서'
        #raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')

def get_commutefolder():
    if gethostname() == 'main':
       return r'D:\01.업무문서\04.출근부 관련\02.각 조별 월별 출근부'
    elif gethostname() =='Sub':
       return r'\\Main\d\01.업무문서\04.출근부 관련\02.각 조별 월별 출근부'
    elif gethostname() =='meetluck':
       return  r'D:\Documents\d\01.업무문서\04.출근부 관련\02.각 조별 월별 출근부'
        #raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')
def get_weeklyworkfolder():
    if gethostname() == 'main':
       return r'D:\01.업무문서\05.주간업무보고서 관련\2022년\주간'
    elif gethostname() =='Sub':
       return r'\\Main\d\01.업무문서\05.주간업무보고서 관련\2022년\주간'
    elif gethostname() =='meetluck':
       return  r'D:\Documents\d\01.업무문서\05.주간업무보고서 관련\2022년\주간'
        #raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')

def get_incidentfolder():
    if gethostname() == 'main':
       return r'D:\01.업무문서\03.사건사고 보고서'
    elif gethostname() =='Sub':
       return r'\\Main\d\01.업무문서\03.사건사고 보고서'
    elif gethostname() =='meetluck':
       return  r'D:\Documents\d\01.업무문서\03.사건사고 보고서'
        #raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')

def get_Afolder():
    if gethostname() == 'main':
       return r'D:\A조'
    elif gethostname() =='Sub':
       return r'\\Main\d\A조'
    elif gethostname() =='meetluck':
       return  r'D:\Documents\d\A조'
        #raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')

def get_excellinkfolder():
    if gethostname() == 'main':
       return r'D:\A조\엑셀링크'
    elif gethostname() =='Sub':
       return r'\\Main\d\A조\엑셀링크'
    elif gethostname() =='meetluck':
       return  r'D:\Documents\d\A조\엑셀링크'
        #raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')

def get_parkfolder():
    if gethostname() == 'main':
       return r'D:\A조\박종우'
    elif gethostname() =='Sub':
       return r'\\Main\d\A조\박종우'
    elif gethostname() =='meetluck':
       return  r'D:\Documents\d\A조\박종우'
        #raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')

def get_cctvfolder():
    if gethostname() == 'main':
       return r'D:\A조\박종우\CCTV'
    elif gethostname() =='Sub':
       return r'\\Main\d\A조\박종우\CCTV'
    elif gethostname() =='meetluck':
       return  r'D:\Documents\d\A조\박종우\CCTV'
        #raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')

def get_infofolder():
    if gethostname() == 'main':
       return r'D:\A조\안내문'
    elif gethostname() =='Sub':
       return r'\\Main\d\A조\안내문'
    elif gethostname() =='meetluck':
       return  r'D:\Documents\d\A조\안내문'
        #raise Exception('Invalid host name' + gethostname())
    else:
        raise Exception('Invalid host name')
