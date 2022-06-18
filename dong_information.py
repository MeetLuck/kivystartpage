from interior_layout import *
import pandas as pd
import csv
import os
from datetime import datetime
from dong_data import *
from layout.mysettings import base 
import operator

def double_click(event):
    """
    Additional event for double-click on header
    event: class event
    """
    region = table.identify("region", event.x, event.y)
    if region == 'heading':                                 # Only care double-clock on headings
        cid = int(table.identify_column(event.x)[1:])-1     # check which column clicked
        window.write_event_value("-TABLE-DOUBLE-CLICK-", cid)

def sort_table(table, cols):
    """ sort a table by multiple columns
        table: a list of lists (or tuple of tuples) where each inner list
               represents a row
        cols:  a list (or tuple) specifying the column numbers to sort by
               e.g. (1,0) would sort by column 1, then by column 0
    """
    for col in reversed(cols):
        try:
            #f = operator.itemgetter(col)(table)     #itemgetter(1, 3, 5)('ABCDEFG')
            #print(f)
            sortedtable = sorted(table, key=operator.itemgetter(col))
            #sortedtable = table.sort(key=operator.itemgetter(col))
        except Exception as e:
            sg.popup_error('Error in sort_table', 'Exception in sort_table', e)
    return sortedtable

class ifield(base):
    fg,bg = 'black','#bbb'
    font  = ('맑은 고딕',15,'normal')
    pad   = (1,1)

headings = ' 동  세대  층  EV1  EV-2  초소  1F   B1a   B1b   B2a   B2b  1F34L B1c   B1d   B2c   B2d '.split()
col_w    = [ 6,   3,    3,  3,   4,    3,    5,   5,   5,     5,   5,    5,     5,    5,    5,    5]
layout = [
    [sg.Table(values=dong_sedae_floor_post_ev, key='dongtable', headings=headings,
        col_widths=col_w, font=base.font, text_color=base.fg, background_color=base.bg, alternating_row_color='#001222',
        header_font=base.font, header_text_color='black', header_background_color='#999',
        max_col_width=35, auto_size_columns=False,display_row_numbers=False,
        justification = 'center', num_rows=45, row_height=30,
        enable_events=True,enable_click_events=True) ]
        ]

#NOTE getting dong data 
savefile = 'dong_data.csv'
with open(savefile, 'w',newline='') as f:
    write = csv.writer(f)
    write.writerow(headings)
    write.writerows(dong_sedae_floor_post_ev)

# NOTE set options and theme
sg.set_options(font=ifield.font)
sg.theme('Dark')
sg.theme_background_color(base.bg)

# NOTE right_click_menu
right_click_menu = ['',['save as csv','read csv','view csv']]

# NOTE create sg.Window
window = sg.Window('동 정보',layout,background_color=base.bg, margins=(40,30), size=(1050,800), resizable=True,
                    keep_on_top=False,right_click_menu = right_click_menu, finalize=True)


while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    #print(f'{event=},\t\t{values=}')

    if event =='save as csv':
        savefile = 'dong_data.csv'
        with open(savefile, 'w',newline='') as f:
            write = csv.writer(f)
            write.writerow(headings)
            write.writerows(dong_sedae_floor_post_ev)

    if event =='view csv':
        csvfile = 'dong_data.csv'
        #print(csvfile)
        #os.system( 'start /b {}'.format(csvfile) )
        os.startfile(csvfile)

    if isinstance(event, tuple):
        # TABLE heading CLICKED Event has value in format ('-TABLE-', '+CLICKED+', (row,col))
        key,clicked,[row,col] = event
        #print(f'{key=}, {clicked=}, ({row=}),({col=})')
        if key == 'dongtable' and row == -1:
            print(f'{key=}, {clicked=}, ({row=}),({col=})')
            #sort_table(col)
            new_table = sort_table(dong_sedae_floor_post_ev[:],(col, 0))
            #new_table = sort_table(data[1:][:],(col, 0))
            window[key].update(values=new_table)
            #data = [data[0]] + new_table
window.close()
