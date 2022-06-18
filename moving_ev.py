import csv
from moving_ev_layout import *
from dong_data import *
from pathlib import Path

def valid_time(time):   return time in ['9','09','13']
def valid_dong(dong):   return dong in map(str,range(101,144+1))
def is_1f(ho):          return ho   in map(str,range(101,104+1)) #NOTE first floor 101,102,103,104
def valid_kind(kind):   return kind in ['전출','전입','반출','반입','공사']
def not_interior(kind): return kind != '공사' #kind = row[4] #return ('전출' in kind) or ('전입' in kind) or ('반출' in kind) or ('반입' in kind)
# NOTE validate
def validate_time(r1):
    row = get_row(r1)
    r1c1 = f'rc{r1}01'
    if not valid_time(row[1]):
        window[r1c1].update(text_color='red')
    else:
        window[r1c1].update(text_color=cell.fg)
def validate_dong(r1):
    row = get_row(r1)
    r1c1 = f'rc{r1}02'
    if not valid_dong(row[2]):
        window[r1c1].update(text_color='red')
    else:
        window[r1c1].update(text_color=cell.fg_dong)
def validate_ho(r1):
    row = get_row(r1)
    dong,ho = row[2],row[3]
    #print( f'{dong=}, {ho=}, {type(ho)=}')
    #if not dong or not ho: return
    if not valid_dong(dong): return
    r1c1 = f'rc{r1}03'
    if ho.isnumeric():
        #ho = int(ho)
        dong_index = find_dong(dong)
        sedae = dong_sedae_floor_post_ev[dong_index][1]
        floor = dong_sedae_floor_post_ev[dong_index][2]
        if int(ho) % 100 in range(1,sedae+1) and int(ho) // 100 in range(1,floor+1):
            window[r1c1].update(text_color=cell.fg)
        else:
            window[r1c1].update(text_color='red')
    else:
        window[r1c1].update(text_color='red')

    if dong in ['111','112'] and ho.isnumeric() and int(ho) >= 2200:
            dong_index = find_dong(dong+'-22')      # 111-2201 ~ 111-28
            sedae = dong_sedae_floor_post_ev[dong_index][1]
            floor = dong_sedae_floor_post_ev[dong_index][2]
            if int(ho) % 100 in range(1,sedae+1) and int(ho) // 100 in range(1,floor+1):
                window[r1c1].update(text_color=cell.fg)
            else:
                window[r1c1].update(text_color='red')

    if dong in ['127','128','129'] and ho.isnumeric() and int(ho) >= 2100:
            dong_index = find_dong(dong+'-21')      # 111-2201 ~ 111-28
            sedae = dong_sedae_floor_post_ev[dong_index][1]
            floor = dong_sedae_floor_post_ev[dong_index][2]
            if int(ho) % 100 in range(1,sedae+1) and int(ho) // 100 in range(1,floor+1):
                window[r1c1].update(text_color=cell.fg)
            else:
                window[r1c1].update(text_color='red')
# NOTE update
def update_background(r1,c1,bg=cell.bg):
    r1c1 = f'rc{r1}{c1:0>2}'
    window[r1c1].update(background_color=bg)
def update_row(r1,row): # NOTE window[key=r1c1].update(value=)
    # NOTE update window using row data, so we need data
    for c1,val in enumerate(row):
        r1c1 = f'rc{r1}{c1:0>2}'
        window[r1c1].update(value=val)
def update_rows():
    rows = get_rows()
    for r1,row in enumerate(rows):
        calculate_row(r1)
    # NOTE after calculate row, check same dongs
    check_samedongs()
# NOTE get row
def clear_row(r1):
    for  c1 in range(number_of_cols):
        r1c1 = f'rc{r1}{c1:0>2}'
        window[r1c1].update(value='',background_color=cell.bg)
def get_row(r1):
    row = ['']* number_of_cols
    for c1 in range(number_of_cols):
        r1c1 = f'rc{r1}{c1:0>2}'
        row[c1] =  window[r1c1].get()
    return row
def get_rows():
    rows = []
    for r1 in range(number_of_rows):
        rows.append( get_row(r1) )
    return rows
def calculate_row(r1):
    # [ row[0], row[1],   row[2],  row[3],  row[4]  row[5],   row[6],  row[7],         row[8],     row[9]
    # [ 순번,   일시,   동          호수,   분류,   초소,    보양X,   2호기(설치),  보양재 제거,   비고 ]
    #   rx0,    rx1,    rx2,       rx3,     rx4,    rx5,     rx6,       rx7,          rx8,        rx9 
    # NOTE get row
    row = get_row(r1)

    # NOTE validate time
    validate_time(r1)

    # NOTE 동, 호수
    dong,ho = row[2],row[3]
    #if not valid_dong(dong): return # NOTE no calculation
    if not dong: return

    validate_dong(r1)
    validate_ho(r1)

    # NOTE calculate 초소[4], EV[5], 보양X[6], 2호기 설치[7], 보양재 제거[8]
    # --------- row[5] : 초소  ---------------
    row[5] = find_post(dong)

    # --------- row[6] : ev1(승강기 갯수) ----
    row[6] = find_ev1(dong)

    # --------- row[7] : 2호기 설치 ---------------
    row[7] = '{}-2'.format(dong) if find_must_ev2(dong) else ''

    # --------- row[8] : 보양X ---------------
    #if not ho: update_row(r1,row); return
    if '보양X' in row[10]: # row[10] :  비 고 = 보양X
        row[8] = '보양X'
    elif is_1f(ho) and ( valid_kind(row[4]) and not_interior(row[4])  ):
        row[8] = '보양X'
    else:
        row[8] = ''

    # --------- row[9] : 보양재 제거 ---------------
    if row[8] == '보양X':
        row[9] = ''
    elif '9' in row[1] and find_ev1(dong) != 1:
        row[9] = '주간'
    else:
        row[9] = ''
        if find_ev1(dong) == 1:
            row[9] += '(EV1)'

    # --------- row[10] : 비고 ---------------
    r1c1 = f'rc{r1}10'
    if '제거' in row[10] and '제거X' not in row[10]:
        window[r1c1].update(background_color='#090')
    else:
        window[r1c1].update(background_color=cell.bg)

    # NOTE update row
    update_row(r1,row)
#NOTE sort
def sort_rows(event):
    events = ['no','time','dong','ho','kind','post','ev1','ev2','noprotect','remove','etc']
    c1 = events.index(event)
    def mysort(row):      return row[c1]      if row[c1] else str(9999)
    def numbersort(row):  return int(row[c1]) if row[c1] else 9999
    
    def kind_sort(row):
        if '전출'in row[c1]: return 0
        if '전입'in row[c1]: return 1
        if '반출'in row[c1]: return 2
        if '반입'in row[c1]: return 3
        if '공사'in row[c1]: return 4
        return 99
    rows = get_rows()
    if event =='kind':           rows.sort(key=kind_sort)
    elif event in ['no','post']: rows.sort(key=numbersort)
    else:                        rows.sort(key=mysort)

    # NOTE update sorted rows 
    for r1,row in enumerate(rows):
        update_row(r1,row)
def check_samedongs():
    #print('check same dongs +++')
    def clear_bg(r1,c1):
        r1c1 = f'rc{r1}{c1:0>2}'
        window[r1c1].update(background_color=cell.bg)
    for r1,row in enumerate( rows:= get_rows() ):
        if not valid_dong( dong:= row[2] ): continue
        clear_bg(r1,c1=2)  # NOTE clear background_color of dong

        for r1_tmp,row_tmp in enumerate(rows):
            if r1_tmp == r1:       continue # NOTE same row
            if row_tmp[2] != dong: continue # NOTE check same place(동)

            # dubplication found
            if row[1] == row_tmp[1]: # NOTE check same time(일시)
                update_background(r1,c1=2,bg='red')
            else:
                update_background(r1,c1=2,bg='#05f')

            # NOTE  recalculate 보양재 제거[9]
            if row[1] != row_tmp[1]:
                r1c1 = f'rc{r1}09'
                window[r1c1].update(value='')
# NOTE sav, open file
def save_csv(event):
    if event == rcm.save_as_csv_today  : csvfile = rcm.csvfile_today
    if event == rcm.save_as_csv_nextday: csvfile = rcm.csvfile_nextday
    window['csvfile'].update(value=csvfile)
    print(f'... saving {csvfile=}')
    with open(csvfile, 'w',newline='') as f:
        write = csv.writer(f)
        write.writerow( head_txt )
        write.writerows( get_rows() )

window = sg.Window('전출입 및 승강기 현황',layout,background_color=base.bg, margins=(40,20), size=(1050,800), resizable=True, icon='truck.png',
                    keep_on_top=False,finalize=True,right_click_menu=rcm.right_click_menu)
def open_csv(event):
    from os.path import exists as file_exists
    if event == rcm.open_csv_today  : csvfile = rcm.csvfile_today
    if event == rcm.open_csv_nextday: csvfile = rcm.csvfile_nextday
    if event == 'open csv':
        csvfile = sg.PopupGetFile('moving_ev*,csv',file_types=(('csv files','csv moving_ev*.csv',)))
    if not csvfile or not file_exists(csvfile):
        print(f'{csvfile} not exist')
        return
    print(f'... opening {csvfile=}')
    window['csvfile'].update( value=Path(csvfile).name )
    with open(csvfile, 'r') as file:
        reader = list( csv.reader(file) )[1:]
        for r1,row in enumerate( row for row in reader ):
            update_row(r1,row) 

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    else:
       update_rows()

    if event == 'clear'       :
        window['csvfile'].update(value='moving_ev.csv')
        for r1 in range(number_of_rows):
            clear_row(r1)
    if 'save as' in event : save_csv(event)
    if 'open'    in event : open_csv(event)
    if event in ['no','time','dong','kind','post']: sort_rows(event)


    update_rows()

window.close()
