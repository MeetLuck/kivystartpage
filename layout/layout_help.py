'''
layout/
   ./__init__
   ./frame1_column1
   ./frame1_column2
   ./mysettings
   ./layout_help
'''
from .mysettings import *

patrol_day = [
    '                                  ',
    '    09  :       2       6       9 ',
    '    10  :       1       5       8 ',
    '    11  :       3       7       10',
    '    13  :       2       6       9',
    '    14  :       1       5       8 ',
    '    15  :       3       7       10',
    '                                  ',
]

patrol_night = [
    '                                  ',
    '    23  :       2       6       9 ',
    '    24  :       1       5       8 ',
    '    01  :       3       7       10',
    '    02  :       2       6       9',
    '    03  :       1       5       8 ',
    '    04  :       3       7       10',
    '                                  ',
]

def get_Text(text,key,size=(10,1),font=base.font,fg=base.fg,bg=base.bg,pad=(10,1)):
    return sg.T(text,key=key,size=size,font=font,background_color=bg,text_color=fg,pad=pad)
def get_Button(text,key,size=(50,1),font=base.font,color=base.color,border_width=0):
    return sg.B(text,key=key,enable_events=True,size=size,font=font,button_color=color,border_width=border_width)
def offdate_Text(text,key,size=(6,1)):
    return get_Text(text,key,size=size,font=base.font+" italic",pad=(10,0))
def offteam_Text(text,key,size=(2,1)):
    return get_Text(text,key,size=size,font=base.font+" italic",pad=(4,0) )
def offworker_Text(text,key,size=(16,1)):
    return get_Text(text,key,size=size,font=files.font,pad=(4,0) )
def files_B(text,key,font=files.font,color=files.color):
    return get_Button(text,key,font=font,color=color)
def cmds_B(text,key):
    return get_Button(text,key,size=cmds.size,font=cmds.font,color=cmds.color,border_width=0)
def folders_B(text,key,size=folders.size,font=folders.font,color=folders.color):
    return get_Button(text,key,size=size,font=font,color=color,border_width=2)
def as_B(text,key,fg=AS.fg,bg=AS.bg):
    return get_Button(text,key,size=folders.size,color=(fg,bg),font=('맑은고딕',11,'bold'),border_width=2 )
def get_listbox(values=patrol_day):
    return [ sg.Listbox(values,font=lbox.font,size=(20,8), background_color = base.bg, text_color=base.fg,pad=(50,2),auto_size_text = True,\
           highlight_background_color=lbox.bg,highlight_text_color = lbox.fg, no_scrollbar = True,key='patrol') ]

if __name__ == '__main__':
    print('----testing layout_help.py----------')

