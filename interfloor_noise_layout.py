import PySimpleGUI as sg
import pandas as pd
from datetime import datetime
from layout.mysettings import base 
from starthelp.starthelp import minwonfile

number_of_rows, number_of_cols = 8, 8  # NOTE : 101 - 144
today = datetime.today()

class swb(base):
    fg,bg = '#f50','#bbb'
    size  = (10,1)
    pad   = (5,5)
    font  = ('Centry Gothic',12,'bold')
    #font  = ('맑은 고딕',12,'normal')
class house(base):
    fg,bg = '#699','#024'
    font  = ('맑은 고딕',14,'bold')
    #font  = ('Centry Gothic',15,'bold')
    color =(fg,bg)

def sort_rows(rows,c1):
    events = ['no','endday','dong','ho','post','company','contact','etc']
    def mysort(row):       return row[c1] if row[c1] else str(9999)
    def kr_sort(row):      return row[c1] if row[c1] else '히'
    def date_sort(row):    return row[c1] if row[c1] else '히'
    if c1 == 0:
        rows.sort(key=date_sort,reverse=True)
    elif c1 in [1,4]:
        rows.sort(key=kr_sort)
    elif c1 == 2:
        rows.sort(key=kr_sort)
    return rows
def get_dataframe(excelfile):
    # disable chained assignments
    pd.options.mode.chained_assignment = None
    df = pd.read_excel(excelfile,sheet_name='층간소음분쟁세대', skiprows = [0,1,2])
    #NOTE clean data
    df.fillna(value={'확인 날짜':'2022-01-01'},inplace=True)
    df.fillna(value={'민원 세대':''},inplace=True)
    df.fillna(value={'분쟁 세대':''},inplace=True)
    df.fillna(value={'조치 내용':''},inplace=True)
    return df
def read_rows_from_excel():
    #today = datetime.today()
    #date= datetime(date.year,date.month,date.day)
    df = get_dataframe(minwonfile)
    rows = []
    for row in df.values.tolist():
        for c1,col in enumerate(row):
            if c1 == 0:
                row[c1] = col.strftime('%y-%m-%d')
        rows.append(row)
    return rows[:]
def get_sorted_rows():
    rows = read_rows_from_excel()
    #print(rows)
    # sort by dong-ho --> c1 = 1
    return sort_rows(rows,1)
def B(text,key,size=(6,1),font=house.font,color=house.color,pad=(3,3),border_width=0,expandx=False,expandy=False):
    return sg.B(text,key=key,enable_events=True,size=size,font=font,button_color=color,pad=pad,border_width=border_width,
                expand_x=expandx,expand_y=expandy)
def T(text,key):
    return sg.T(text,key=key,size=(80,1),pad=(30,5),font=base.font, text_color='#08d',background_color=base.bg,justification='r')
def H(key):
    return B('',key,size=(10,2) )
def swB(text,key,size=swb.size,fg=swb.fg,bg=swb.bg,pad=swb.pad,border_width=2,expandx=False,expandy=False):
    return sg.B(text,key=key,enable_events=True,size=size,font=swb.font,button_color=(fg,bg),pad=pad,border_width=border_width,
                expand_x=expandx,expand_y=expandy)

layout =[
    [ swB('민원세대',key='minwonhouse'), T(f'층간소음분쟁세대{today: %y-%m-%d}',key='interfloorfilename') ]
]

for row in range(number_of_rows): 
    layout.append(
        [ H(f'rc{row}0'), H(f'rc{row}1'), H(f'rc{row}2'), H(f'rc{row}3'), H(f'rc{row}4'), H(f'rc{row}5'), H(f'rc{row}6'), H(f'rc{row}7') ])

if __name__ == '__main__':
    # NOTE right_click_menu
    right_click_menu = ['',['read excel','save as csv','read csv','view csv']]
    # NOTE create sg.Window
    window = sg.Window('층간소음 분쟁세대',layout,background_color=base.bg, margins=(40,30), size=(900,800), resizable=True,
                        keep_on_top=False,right_click_menu = right_click_menu, finalize=True)
    #window = sg.Window('세대공사현황',layout,background_color=base.bg, margins=(40,30), size=(600,100), resizable=True,
    #                keep_on_top=False,finalize=True)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
