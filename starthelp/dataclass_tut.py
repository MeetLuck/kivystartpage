from dataclasses import dataclass
from datetime import datetime

@dataclass
class Card:
    rank: str = 'Q'
    suit: str = 'hearts'
#print(Card.rank)

@dataclass
class Sub:
    workdate : datetime
    # NOTE files
    minwonfile  = r'\\Main\d\\01.업무문서\000. 민원처리내역.xlsx'
    dailyreportfile1 = None
    dailyreportfile2 = None
    monthlyfile = None

    wonhyungfile = r'\\Main\d\01.업무문서\00.원형도로 단속일지(최종본).xlsx'
    todofile = r'D:\01.A조\sub박종우\banpo\todo.txt'
    minwodbfile = r'D:\01.A조\sub박종우\banpo\minwondb.py'
    hpscanfile = r'C:\Program Files (x86)\HP\HP OfficeJet Pro 8710\bin\HPScan.exe'
    snippingtoolfile = r'C:\WINDOWS\system32\SnippingTool.exe'
    dbbrowserfile = r'D:\01.A조\sub박종우\DB Browser for SQLite\DB Browser for SQLite.exe'
    gitfile = r'D:\01.A조\sub박종우\GitPortable\GitBashPortable.exe'
    # NOTE folders
    workfolder =  r'\\Main\d\01.업무문서'
    commutefolder =  r'\\Main\d\01.업무문서\04.출근부 관련\02.각 조별 월별 출근부'
    weeklyworkfolder =  r'\\Main\d\01.업무문서\05.주간업무보고서 관련\2022년\주간'
    incidentfolder =  r'\\Main\d\01.업무문서\03.사건사고 보고서'
    Afolder =  r'\\Main\d\A조'
    excellinkfolder =  r'\\Main\d\A조\엑셀링크'
    parkfolder =  r'\\Main\d\A조\박종우'
    cctvfolder = r'\\Main\d\A조\박종우\CCTV'
    infofolder =  r'\\Main\d\A조\안내문'

    #NOTE png files
    daypatrolfile = r'D:\01.A조\sub박종우\banpo\day_patrol.png'
    nightpatrolfile = r'D:\01.A조\sub박종우\banpo\night_patrol.png'
    dongpostfile =  r'D:\01.A조\sub박종우\banpo\dong_post.png'

    def __post_init__(self):
        #workdate  = self.workdate
        print(self.workdate)
        from datetime import timedelta
        workmonth =self.workdate.strftime("%m")
        workdate1 =self.workdate.strftime("%Y%m%d")
        workdate2 =(self.workdate + timedelta(days=1)).strftime("%Y%m%d")
        self.monthlyfile = r'\\Main\d\01.업무문서\04.출근부 관련\02.각 조별 월별 출근부\{} A,B,C조별 월별출근부(반포자이).xlsx'.format(workmonth)
        self.dailyreportfile1 = r'\\Main\d\01.업무문서\01.일일상황보고(상황실)\2022년{}월\일일 상황 보고 {}.xlsx'.format(workmonth,workdate1)
        self.dailyreportfile2 = r'\\Main\d\01.업무문서\01.일일상황보고(상황실)\2022년{}월\일일 상황 보고 {}.xlsx'.format(workmonth,workdate2)

@dataclass
class Main:
    workdate : datetime
    # NOTE files
    dailyreportfile1 = None
    dailyreportfile2 = None
    monthlyfile = None

    # NOTE files
    minwonfile = r'D:\01.업무문서\000. 민원처리내역.xlsx'
    wonhyungfile = r'D:\01.업무문서\00.원형도로 단속일지(최종본).xlsx'
    todofile =  r'D:\A조\todo.txt'
    minwondb =  r'D:\01.A조\sub박종우\banpo\minwondb.py'
    dbbrowserfile = r'D:\01.A조\sub박종우\DB Browser for SQLite\DB Browser for SQLite.exe'
    hpscanfile =  r'C:\Program Files (x86)\HP\HP OfficeJet Pro 8710\bin\HPScan.exe'
    snippingtoolfile =  r'C:\WINDOWS\system32\SnippingTool.exe'
    gitfile = r'D:\01.A조\sub박종우\GitPortable\GitBashPortable.exe'

    #NOTE png files
    daypatrolfile =  r'D:\01.A조\sub박종우\banpo\day_patrol.png'
    nightpatrolfile =  r'D:\01.A조\sub박종우\banpo\night_patrol.png'
    dongpostfile =  r'D:\01.A조\sub박종우\banpo\dong_post.png'

    # NOTE folders
    workfolder =  r'D:\01.업무문서'
    commutefolder =  r'D:\01.업무문서\04.출근부 관련\02.각 조별 월별 출근부'
    weeklyworkfolder =  r'D:\01.업무문서\05.주간업무보고서 관련\2022년\주간'
    incidentfolder =  r'D:\01.업무문서\03.사건사고 보고서'
    Afolder =  r'D:\A조'
    excellinkfolder =  r'D:\A조\엑셀링크'
    parkfolder =  r'D:\A조\박종우'
    cctvfolder =  r'D:\A조\박종우\CCTV'
    infofolder = r'D:\A조\안내문'

    def __post_init__(self):
        #workdate  = self.workdate
        print(self.workdate)
        from datetime import timedelta
        workmonth =self.workdate.strftime("%m")
        workdate1 =self.workdate.strftime("%Y%m%d")
        workdate2 =(self.workdate + timedelta(days=1)).strftime("%Y%m%d")
        self.monthlyfile = r'D:\01.업무문서\04.출근부 관련\02.각 조별 월별 출근부\{} A,B,C조별 월별출근부(반포자이).xlsx'.format(workmonth)
        self.dailyreportfile1 = r'D:\01.업무문서\01.일일상황보고(상황실)\2022년{}월\일일 상황 보고 {}.xlsx'.format(workmonth,workdate1)
        self.dailyreportfile2 = r'D:\01.업무문서\01.일일상황보고(상황실)\2022년{}월\일일 상황 보고 {}.xlsx'.format(workmonth,workdate2)


@dataclass
class Meetluck:
    workdate : datetime
    # NOTE files
    dailyreportfile1 = None
    dailyreportfile2 = None
    monthlyfile = None

    # NOTE files
    minwonfile = r'D:\Documents\d\01.업무문서\000. 민원처리내역.xlsx'
    wonhyungfile = r'\\Main\d\01.업무문서\00.원형도로 단속일지(최종본).xlsx'
    todofile = r'D:\Documents\d\todo.txt'
    minwodbfile =  r'D:\01.A조\sub박종우\banpo\minwondb.py'
    dbbrowserfile = r'D:\01.A조\sub박종우\DB Browser for SQLite\DB Browser for SQLite.exe'
    hpscanfile =  r'C:\Program Files (x86)\HP\HP OfficeJet Pro 8710\bin\HPScan.exe'
    snippingtoolfile =  r'C:\WINDOWS\system32\SnippingTool.exe'
    gitfile = r'D:\01.A조\sub박종우\GitPortable\GitBashPortable.exe'

    #NOTE png files
    daypatrolfile = r'D:\Documents\banpo\day_patrol.png'
    nightpatrolfile =  r'D:\Documents\banpo\night_patrol.png'
    dongpostfile =  r'D:\Documents\banpo\dong_post.png'

    # NOTE folders

    workfolder =  r'D:\Documents\d\01.업무문서'
    commutefolder =  r'D:\Documents\d\01.업무문서\04.출근부 관련\02.각 조별 월별 출근부'
    weeklyworkfolder =  r'D:\Documents\d\01.업무문서\05.주간업무보고서 관련\2022년\주간'
    incidentfolder =  r'D:\Documents\d\01.업무문서\03.사건사고 보고서'
    Afolder =  r'D:\Documents\d\A조'
    excellinkfolder =  r'D:\Documents\d\A조\엑셀링크'
    parkfolder =  r'D:\Documents\d\A조\박종우'
    cctvfolder =  r'D:\Documents\d\A조\박종우\CCTV'
    infofolder =  r'D:\Documents\d\A조\안내문'


    def __post_init__(self):
        #workdate  = self.workdate
        print(self.workdate)
        from datetime import timedelta
        workmonth =self.workdate.strftime("%m")
        workdate1 =self.workdate.strftime("%Y%m%d")
        workdate2 =(self.workdate + timedelta(days=1)).strftime("%Y%m%d")
        self.monthlyfile = r'D:\Documents\d\01.업무문서\04.출근부 관련\02.각 조별 월별 출근부\{} A,B,C조별 월별출근부(반포자이).xlsx'.format(workmonth)
        self.dailyreportfile1 = r'D:\Documents\d\01.업무문서\01.일일상황보고(상황실)\2022년{}월\일일 상황 보고 {}.xlsx'.format(workmonth,workdate1)
        self.dailyreportfile2 = r'D:\Documents\d\01.업무문서\01.일일상황보고(상황실)\2022년{}월\일일 상황 보고 {}.xlsx'.format(workmonth,workdate2)


if __name__ == '__main__':
    today = datetime.today()
    sub = Sub(datetime(2022,2,10))
    main = Main(datetime(2022,2,10))
    print(repr(sub))
    print(repr(main.monthlyfile))
