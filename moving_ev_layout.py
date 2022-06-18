import PySimpleGUI as sg
from datetime import datetime,timedelta
from layout.mysettings import base 

#XXX number_of_cols > 10 : rc110 -> rc1110 BUG reports
number_of_rows = 20; number_of_cols = 11
today = datetime.today()
head_txt = ['순번','일시','동','호수','분류','초소','EV1','EV2','2호기(설치)','보양재 제거','비고']

class head(base):
    fg,bg = '#024','#aaa'
    font  = ('맑은 고딕',14,'normal')
    color =(fg,bg)
    pad = (0,0)
    size = (8,1)

class cell(base):
    fg,bg = 'black','#bbb'
    fg_dong = '#039'
    font  = ('맑은 고딕',15,'normal')
    pad   = (0,0)
    size  =(8,1)

def head_B(text,key,size=head.size,font=head.font,color=head.color):
    return sg.B(text,key=key,enable_events=True,size=size,font=font,button_color=color,pad=head.pad,border_width=1,auto_size_button=False)

def I(key,size=cell.size,font=cell.font,fg=cell.fg,bg=cell.bg):
    return sg.I('',key=key,size=size,font=font,background_color=bg,text_color=fg,pad=cell.pad,border_width=1,justification='c',
            enable_events=True,change_submits=True)
def disabled_I(key,size=cell.size,font=cell.font,fg=base.fg,bg=base.bg):
    return sg.I(key=key,size=size,readonly=True,font=font,disabled_readonly_background_color=bg,disabled_readonly_text_color=fg,\
           pad=(1,0),border_width=1,justification='c')

def  NO(key):    return  I(key,size=4)
def  TIME(key):  return  I(key,size=5)
def  DONG(key):  return  I(key,fg=cell.fg_dong,font=('맑은 고딕',15,'bold'))
def  HO(key):    return  I(key)
def  KIND(key):  return  I(key,size=(10,1))
def  POST(key):  return  disabled_I(key,size=5)
def  EV1(key):   return  disabled_I(key,size=5)
def  EV2(key):   return  disabled_I(key,size=(10,1))
def  NOPR(key):  return  disabled_I(key)            # 보양재 X
def  RM(key):    return  disabled_I(key,size=(10,1))
def  ETC(key):   return  I(key,size=10)

row_head = [ head_B('NO','no',size=4),head_B('일시','time',size=5),head_B(' 동 ','dong'),head_B('호수','ho'),head_B('분류','kind',size=10),
             head_B('초소','post',size=5), head_B('EV1','ev1',size=5),head_B('2호기(설치)','ev2',size=(10,1)), head_B('보양X','noprotect'),
             head_B('보양재 제거','remove',size=(10,1)), head_B('비 고','etc',size=(10,1)) ]

layout = [
    [ sg.T(text=f'moving_ev {today:%y-%m-%d}.csv',key='csvfile',size=(20,1),pad=(0,5),font=base.font,
       text_color='#0d0',background_color=base.bg,justification='l') ],
    [ head_B('NO','no',size=4),head_B('일시','time',size=5),head_B(' 동 ','dong'),head_B('호수','ho'),head_B('분류','kind',size=10),
      head_B('초소','post',size=5), head_B('EV1','ev1',size=5),head_B('2호기(설치)','ev2',size=(10,1)), head_B('보양X','noprotect'),
      head_B('보양재 제거','remove',size=(10,1)), head_B('비 고','etc',size=(10,1)) ]
    ]

for row in range(number_of_rows): layout.append(
    [ NO(f'rc{row}00'), TIME(f'rc{row}01'), DONG(f'rc{row}02'), HO(f'rc{row}03'),KIND(f'rc{row}04'), POST(f'rc{row}05'),
      EV1(f'rc{row}06'), EV2(f'rc{row}07'), NOPR(f'rc{row}08'),RM(f'rc{row}09'),ETC(f'rc{row}10')] )

# NOTE right_click_menu
class rcm:
    format_today        = f'{today:%y-%m-%d}'
    format_nextday      = f'{today+timedelta(1):%y-%m-%d}'
    csvfile_today       = f'moving_ev {format_today}.csv'
    csvfile_nextday     = f'moving_ev {format_nextday}.csv'
    save_as_csv_today   = f'save as {csvfile_today}'
    save_as_csv_nextday = f'save as {csvfile_nextday}'
    open_csv_today      = f'open    {csvfile_today}'
    open_csv_nextday    = f'open    {csvfile_nextday}'
    right_click_menu = ['',['clear',save_as_csv_today,save_as_csv_nextday,open_csv_today,open_csv_nextday,'open csv']]

if __name__ == '__main__':
    right_click_menu = ['',['save as csv','open csv']]
    window = sg.Window('전출입 및 승강기 현황',layout,background_color=base.bg, margins=(45,30), size=(1200,800), resizable=True,
                    keep_on_top=False,finalize=True,right_click_menu=right_click_menu)
    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        print('event,values',event)

    window.close()
