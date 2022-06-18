'''
+===============frame 1================+
+   [COLUMN1]     |     [COLUMN2]      +
+                 |                    +
+   calendar      |       files        +
+   off workers   |                    +
+-----------------|--------------------+
+   patrol        |       cmds         + 
+                 |                    +
+   dong - post   |--------------------+
+                 |   folders - folder +            
+                 |            - A/S   +            
+===============frame 2================+
+                                      +
+                                      +
++++++++++++++++++++++++++++++++++++++++
'''
from .layout_help import *

def folders_B1(text,key,color=(base.bg,'#bbb')):
    return folders_B(text,key,color=color)
def folders_B2(text,key,color=(base.bg,'#888')):
    return folders_B(text,key,color=color)
def folders_B3(text,key,color=(base.bg,'#888')):
    return folders_B(text,key,color=color)

cols_files =[
    [ files_B("민원","minwonfile")               ],
    [ files_B("일일상황보고1","dailyreportfile1")],
    [ files_B("일일상황보고2","dailyreportfile2")],
    [ files_B("월간출근부","monthlyfile")        ],
    [ files_B("원형도로","wonhyungfile")         ] ]

cols_cmds = [
    [ cmds_B("$ gvim todo.txt","todo"),             cmds_B("$ python minwon.py","runminwon")    ],
    [ cmds_B("$ python minwondb.py",'runminwondb'), cmds_B("$ DB Browser for SQLite.exe","db")  ],
    [ cmds_B("$ GitBashPortable.exe","git"),        cmds_B("$ SnippingTool.exe","snippingtool") ],
    [ cmds_B("$ HP Scan","hpscan"),                 cmds_B("$ to be added","tobeadded")         ] ]

cols_folders = [
[ folders_B1("업무문서","workfolder"), folders_B1("출근부","commutefolder"),    folders_B1("주간업무","weeklyworkfolder"),folders_B1("사건사고","incidentfolder")],
[ folders_B2("A조","Afolder"),         folders_B2("엑셀링크","excellinkfolder"),folders_B2("안내문","infofolder"),        folders_B2("","na1") ],
[ folders_B3("박종우","parkfolder"),   folders_B3("CCTV","cctvfolder"),         folders_B3("banpo","banpofolder"),        folders_B3("","notImplemeted")]
]
cols_as = [
[ as_B("직원연락처",'phonefile'),              as_B("지도",'map1ffile'), as_B("지하주차장",'mapb1file'),as_B("지하주차장cctv",'mapb1cctvfile')],
[ as_B('E/V 1899-7144','ev_button',fg='#090'), as_B('cctv 1566-7896','cctv_button',fg='#090'),
  as_B('홈넷 1111','homenet_button',fg='#d50'),as_B('금고 1234','vault_button',fg='#d60')],
[ as_B('세대현관','gateman_button',fg='#06c')],
]

frame_files   = [ sg.Frame('', cols_files, background_color=base.bg,font=base.font, expand_x=True, pad=(0,0), border_width=1)   ]
frame_cmds    = [ sg.Frame('', cols_cmds,  background_color=base.bg,font=base.font, expand_x=True, pad=(0,10), border_width=1)  ]
frame_folders = [ sg.Frame('', cols_folders, background_color=base.bg,font=base.font, expand_x=True, pad=(0,5), border_width=0) ]
frame_as      = [ sg.Frame('', cols_as, background_color=base.bg,font=base.font, expand_x=True, pad=(0,5), border_width=0) ]

col2 = [ frame_files,
         frame_cmds,
         frame_folders,
         frame_as
         ]
       
