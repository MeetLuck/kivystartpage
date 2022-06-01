from socket import gethostname

if gethostname() == 'main':
    # NOTE files
    minwonfile = r'D:\01.업무문서\000. 민원처리내역.xlsx'
    wonhyungfile = r'D:\01.업무문서\00.원형도로 단속일지(최종본).xlsx'
    todofile =  r'D:\01.A조\sub박종우\banpo\todo.txt'
    minwonpyfile = r'\\Sub\d\01.A조\sub박종우\banpo\minwon\minwon.py'
    minwondbfile =  r'\\Sub\d\01.A조\sub박종우\banpo\minwon\minwondb.py'
    dbbrowserfile = r'D:\A조\박종우\DB Browser for SQLite\DB Browser for SQLite.exe'
    hpscanfile =  r'C:\Program Files (x86)\HP\HP OfficeJet Pro 8710\bin\HPScan.exe'
    snippingtoolfile =  r'C:\WINDOWS\system32\SnippingTool.exe'
    gitfile = r'\\Sub\d\A조\sub박종우\GitPortable\GitBashPortable.exe'
    #NOTE png files
    daypatrolfile =  r'\\Sub\d\01.A조\sub박종우\banpo\day_patrol.png'
    nightpatrolfile =  r'\\Sub\d\01.A조\sub박종우\banpo\night_patrol.png'
    dongpostfile =  r'\\Sub\d\01.A조\sub박종우\banpo\dong_post.png'
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

    #NOTE png files
    dongpostfile    = r'\\Sub\d\01.A조\sub박종우\banpo\dong_post.png'
    phonefile       = r'D:\A조\직원연락처(내선번호)-3.11.jpg'
    map1ffile       = r'D:\A조\엑셀링크\반포자이아파트.jpg'
    mapb1file       = r'D:\A조\엑셀링크\지하주차장.png'
    mapb1cctvfile   = r'D:\A조\엑셀링크\지하주차장cctv.png'
    vaultfile       = r'D:\A조\엑셀링크\금고.png'
    gatemanfile     = r'D:\A조\박종우\subbanpo\세대현관문.jpg'

    #NOTE image_filename
    ev_button_img       = r'\\Sub\d\01.A조\sub박종우\banpo\ev_button.png'
    cctv_button_img     = r'\\Sub\d\01.A조\sub박종우\banpo\cctv_button.png'
    homenet_button_img  = r'\\Sub\d\01.A조\sub박종우\banpo\homenet_button.png'
    vault_button_img    = r'\\Sub\d\01.A조\sub박종우\banpo\vault_button.png'
elif gethostname() == 'Sub':
    # NOTE files
    minwonfile  = r'\\Main\d\\01.업무문서\000. 민원처리내역.xlsx'
    wonhyungfile = r'\\Main\d\01.업무문서\00.원형도로 단속일지(최종본).xlsx'
    todofile = r'D:\01.A조\sub박종우\banpo\todo.txt'
    minwonpyfile = r'D:\01.A조\sub박종우\banpo\minwon\minwon.py'
    minwondbfile = r'D:\01.A조\sub박종우\banpo\minwon\minwondb.py'
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
    banpofolder = r'D:\01.A조\sub박종우\banpo'

    #NOTE png files
    dongpostfile    =  r'D:\01.A조\sub박종우\banpo\dong_post.png'
    phonefile       = r'\\Main\d\A조\직원연락처(내선번호)-3.11.jpg'
    map1ffile       = r'\\Main\d\A조\엑셀링크\반포자이아파트.jpg'
    mapb1file       = r'\\Main\d\A조\엑셀링크\\지하주차장.png'
    mapb1cctvfile   = r'\\Main\d\A조\엑셀링크\\지하주차장cctv.png'
    vaultfile       = r'\\Main\d\A조\엑셀링크\\금고.png'
    gatemanfile     = r'D:\01.A조\sub박종우\banpo\세대현관문.jpg'

    #NOTE Button image_filename
    ev_button_img       = r'D:\01.A조\sub박종우\banpo\ev_button.png'
    cctv_button_img     = r'D:\01.A조\sub박종우\banpo\cctv_button.png'
    homenet_button_img  = r'D:\01.A조\sub박종우\banpo\homenet_button.png'
    vault_button_img    = r'D:\01.A조\sub박종우\banpo\vault_button.png'
elif gethostname() == 'meetluck':
    # NOTE files
    minwonfile = r'D:\Documents\d\01.업무문서\000. 민원처리내역.xlsx'
    wonhyungfile = r'\\Main\d\01.업무문서\00.원형도로 단속일지(최종본).xlsx'
    todofile = r'D:\Documents\banpo\todo.txt'
    minwodbfile =  r'D:\01.A조\sub박종우\banpo\minwon\minwondb.py'
    dbbrowserfile = r'D:\01.A조\sub박종우\DB Browser for SQLite\DB Browser for SQLite.exe'
    hpscanfile =  r'C:\Program Files (x86)\HP\HP OfficeJet Pro 8710\bin\HPScan.exe'
    snippingtoolfile =  r'C:\WINDOWS\system32\SnippingTool.exe'
    gitfile = r'D:\01.A조\sub박종우\GitPortable\GitBashPortable.exe'

    #NOTE png files
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

    #NOTE image_filename
    ev_button_img       = r'D:\Documents\banpo\ev_button.png'
    cctv_button_img     = r'D:\Documents\banpo\cctv_button.png'
    homenet_button_img  = r'D:\Documents\banpo\homenet_button.png'
    vault_button_img    = r'D:\Documents\banpo\vault_button.png'
else:
    raise Exception(r'unknown host {}'.format(gethostname()))



if __name__ == '__main__':
    today = datetime.today()
    sub = Sub(datetime(2022,2,10))
    main = Main(datetime(2022,2,10))
    print(repr(sub))
    print(repr(main.monthlyfile))
