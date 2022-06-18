import PySimpleGUI as sg
from layout.mysettings import base 
from datetime import datetime, timedelta

today = datetime.today()
default_date=(today.month,today.day, today.year)

number_of_rows = 20
number_of_cols = 8

class ifield(base):
    fg,bg = 'black','#bbb'
    font  = ('맑은 고딕',15,'normal')
    pad   = (1,1)
    #font  = ('Centry Gothic',16,'normal')

class hfield(base):
    fg,bg = '#024','#aaa'
    font  = ('맑은 고딕',14,'bold')
    #font  = ('Centry Gothic',16,'normal')
    color =(fg,bg)

def head_B(text,key,size=(6,1),font=hfield.font,color=hfield.color,pad=(0,1),border_width=1):
    return sg.B(text,key=key,enable_events=True,size=size,font=font,button_color=color,pad=pad,border_width=border_width)

def I(key,size=(12,1),font=ifield.font,fg=ifield.fg,bg=ifield.bg,border_width=1):
    return sg.I(key=key,size=size,font=font,background_color=bg,text_color=fg,pad=ifield.pad,border_width=border_width,justification='c',enable_events=True)

def NO(key):        return I(key,size=(6,1),fg='#035',   bg=base.bg)
def TIME(key):      return I(key,size=(8,1),fg=base.fg,  bg=base.bg)
def DONG(key):      return I(key,size=(8,1),fg='#0ac',   bg=base.bg)
def HO(key):        return I(key,size=(8,1),fg=base.fg,  bg=base.bg)
def POST(key):      return I(key,size=(6,1),fg=ifield.fg,bg=ifield.bg)
def COMPANY(key):   return I(key,size=(12,1),fg=ifield.fg,bg=ifield.bg)
def CONTACT(key):   return I(key,size=(12,1),fg=ifield.fg,bg=ifield.bg) 
def ETC(key):       return I(key,size=(14,1),fg=ifield.fg,bg=ifield.bg)

input_field = sg.Input( key='-CAL-',justification = 'c',readonly = True, disabled_readonly_background_color=base.bg, disabled_readonly_text_color='#ff0', enable_events=True,size=(10,1),pad=(10,10) )

calendar = sg.CalendarButton(
    'Cal',size=(3,1),font=base.font, button_color=base.color,enable_events=True,target='-CAL-',key='_CALENDAR_',\
    format=('%Y%m%d'),pad=(0,10),default_date_m_d_y=default_date )

row_calendar = [ input_field, calendar ]
row_head = [ head_B('NO','no',size=(6,1)),head_B('종료일','endday',size=(8,1)),head_B('동','dong',size=(8,1)),head_B('호수','ho',size=(8,1)),
             head_B('초소','post',size=(6,1)),head_B('공사업체','company',size=(12,1)),head_B('연락처','contact',size=(12,1)), head_B('비고','etc',size=(14,1))]

# NOTE      No     종료일    동     호수   관할초소 공사업체  연락처   비고
#           r00     r01     r02     r03     r04     r05        r06     r07


layout =[
[ sg.T(text=f'interior{today:%y-%m-%d}.csv',key='csvfile',size=(20,1),pad=(0,5),font=base.font,
      text_color='#0d0',background_color=base.bg,justification='l')]
]

layout.append(row_head)
for row in range(20): layout.append(
[ NO(f'rc{row}0'), TIME(f'rc{row}1'), DONG(f'rc{row}2'), HO(f'rc{row}3'), POST(f'rc{row}4'), COMPANY(f'rc{row}5'), CONTACT(f'rc{row}6'), ETC(f'rc{row}7')])


# NOTE right_click_menu
class rcm:
    format_today        = f'{today:%y-%m-%d}'
    format_nextday      = f'{today+timedelta(1):%y-%m-%d}'
    csvfile_today       = f'interior {format_today}.csv'
    csvfile_nextday     = f'interior {format_nextday}.csv'
    save_as_csv_today   = f'save as {csvfile_today}'
    save_as_csv_nextday = f'save as {csvfile_nextday}'
    open_csv_today      = f'open    {csvfile_today}'
    open_csv_nextday    = f'open    {csvfile_nextday}'
    right_click_menu = ['',['read excel',save_as_csv_today,save_as_csv_nextday,open_csv_today,open_csv_nextday,'open csv']]

if __name__ == '__main__':
    # NOTE right_click_menu
    right_click_menu = ['',['read excel','save as csv','read csv','view csv']]
    # NOTE create sg.Window
    window = sg.Window('세대공사현황',layout,background_color=base.bg, margins=(40,30), size=(900,800), resizable=True,
                        keep_on_top=False,right_click_menu = right_click_menu, finalize=True)
    #window = sg.Window('세대공사현황',layout,background_color=base.bg, margins=(40,30), size=(600,100), resizable=True,
    #                keep_on_top=False,finalize=True)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
