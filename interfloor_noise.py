from interfloor_noise_layout import *

''' rows_sum = [
    [ 22-03-01, 101-1103,101-1203,방문금지,.... ],
    [ 22-03-03, 103-1902,103-2002,방문금지,.....],
    ..............................................
    [ 22-03-03, 103-1902,103-2002,방문금지,.....]
    ] '''

def interfloor_data(table):
    headings = ' 날짜   민원세대  분쟁세대  분쟁내용    조치내용    비고'.split()
    col_w    = [ 6,        6,      6,         8,        10,         90]
    layout = [
        [sg.Table(values=table, key='floornoise', headings=headings,
            col_widths=col_w, font=base.font, text_color=base.fg, background_color=base.bg, alternating_row_color='#001222',
            header_font=base.font, header_text_color='black', header_background_color='#999',
            max_col_width=80, auto_size_columns=False,display_row_numbers=False,
            justification = 'left', num_rows=70, row_height=40,  expand_x = True, expand_y = True,
            enable_events=True,enable_click_events=True) ]
            ]

    # NOTE create sg.Window
    window = sg.Window('층간소음 분쟁세대 Data',layout,background_color=base.bg, margins=(40,30), size=(1200,900), resizable=True, keep_on_top=False,finalize=True)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit': break
        if isinstance(event, tuple):
            # TABLE heading CLICKED Event has value in format ('-TABLE-', '+CLICKED+', (row,col))
            key,clicked,[row,col] = event
            if key == 'floornoise' and row == -1:
                print(f'{key=}, {clicked=}, ({row=}),({col=})')
                sort_rows(table,col)
                window[key].update(values=table)

    window.close()

def update_rows(rows,minwon):
    for row_no,dongho_record in enumerate(rows):
        if minwon:
            dongho,novisit = dongho_record[1], dongho_record[4]
        else:
            dongho,novisit = dongho_record[2], dongho_record[4]

        if type(dongho) != str:
            print(dongho)
            dongho  = str(dongho) 
        if type(novisit) == str and ('103-1902' in dongho or '103-2002' in dongho):
            button_color = ('#046',house.bg)
        elif type(novisit) == str and ('금지' in novisit or '거부' in novisit): 
            button_color = (house.fg,'#700')
        elif type(novisit) == str and '자제' in novisit: 
            button_color = (house.fg,'#950')
        else:
            button_color = house.color

        r1,c1 = row_no // number_of_cols, row_no % number_of_cols
        r1c1 = f'rc{r1}{c1}'
        window[r1c1].update(text=dongho, button_color=button_color)

# NOTE set options and theme
sg.set_options(font=house.font)
sg.theme('Dark')
sg.theme_background_color(base.bg)

# NOTE create sg.Window
window = sg.Window('층간소음 분쟁세대',layout,background_color=base.bg, margins=(40,30), size=(1050,700), resizable=True,
                    right_click_menu = ['',['show data',' ']],finalize=True)
# NOTE switch 
MINWON = True  # 0 -> 민원세대, 1-> 분쟁세대

# NOTE update rows 
rows = get_sorted_rows()
update_rows(rows,MINWON)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': break
    if event == 'minwonhouse':
        MINWON = not MINWON
        if MINWON:
            window[event].update(text='민원세대',button_color = (swb.fg,swb.bg) )
        else:
            window[event].update(text='분쟁세대',button_color = ('red',swb.bg) )
        update_rows(rows,MINWON)
    if 'rc' in event: # NOTE button event
        #print(dir(window[event]))
        dongho = window[event].GetText()
        for r1,dongho_record in enumerate(rows):
            if dongho and dongho in dongho_record[1]:
                sg.popup(dongho_record)
                continue
    if event == 'show data':
        interfloor_data(rows)
window.close()

