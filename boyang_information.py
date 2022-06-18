#from interior_layout import ifield
import PySimpleGUI as sg
import pandas as pd,csv,os
from datetime import datetime
from dong_data import *
from layout.mysettings import base 

print(base,base.bg)
class table(base):
    fg,bg = 'black','#bbb'
    font  = ('맑은 고딕',12,'normal')
    pad   = (1,1)

class ifield(base):
    fg,bg = 'black','#bbb'
    font  = ('맑은 고딕',15,'normal')
    pad   = (1,1)

csvfile = '보양재현황.csv'

def read_csv(csvfile):
    from os.path import exists as file_exists
    if not file_exists(csvfile):
        return
        #raise Exception('FileNotFoundError {}'.format(csvfile))
    rows = []
    with open(csvfile, 'r') as file:
        reader = csv.reader(file)
        for row_no,row in enumerate(reader):
            if row_no == 0: continue
            rows.append(row)
    return rows

#headings = ' 동  세대  층  EV  초소  1F   B1a   B1b   B2a   B2b  1F3,4L B1c   B1d   B2c   B2d '.split()
headings =    '위 치,관할초소,승강기 보양재,바닥 보양재,카트'.split(',')
col_w    = [ 12,   10,   10,  10,   10]
layout = [
    [sg.Table(values=read_csv(csvfile), headings=headings,
        col_widths = col_w, font = table.font,
        text_color=base.fg,background_color = base.bg,alternating_row_color = '#001222',
        header_font=base.font, header_text_color = 'black', header_background_color = '#999',
        max_col_width=35, auto_size_columns=False,display_row_numbers=False, hide_vertical_scroll = True,
        justification = 'center', num_rows=45, key='dongtable',row_height=30)]
        ]

# NOTE set options and theme
sg.set_options(font=ifield.font)
sg.theme('Dark')
sg.theme_background_color(base.bg)

# NOTE create sg.Window
window = sg.Window('보양재현황',layout,background_color=base.bg, margins=(40,30), size=(700,800), resizable=True, keep_on_top=False, finalize=True)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break


window.close()
