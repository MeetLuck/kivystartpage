import csv, os, pandas as pd
from interior_layout import *
from starthelp.starthelp import get_dailyreportfile
from dong_data import *
from pathlib import Path
from os.path import exists as file_exists

def valid_dong(dong):   return dong in map(str,range(101,144+1))
# NOTE get rows from window
def get_row(r1):
    return [ window[f'rc{r1}{c1}'].get() for c1 in range(number_of_cols) ]
def get_rows():
    return [ get_row(r1) for r1 in range(number_of_rows) ]
# NOTE validation
def validate_dong(r1):
    dong = get_row(r1)[2]
    r1c1 = f'rc{r1}2'
    if valid_dong(dong):
        window[r1c1].update(text_color='#0ac')
    else:
        window[r1c1].update(text_color='red')
def validate_ho(r1):
    row = get_row(r1)
    dong,ho = row[2],row[3]
    if not valid_dong(dong): return
    r1c1 = f'rc{r1}3'
    if ho.isnumeric():
        dong_index = find_dong(dong)
        sedae = dong_sedae_floor_post_ev[dong_index][1]
        floor = dong_sedae_floor_post_ev[dong_index][2]
        if int(ho) % 100 in range(1,sedae+1) and int(ho) // 100 in range(1,floor+1):
            window[r1c1].update(text_color=base.fg)
        else:
            window[r1c1].update(text_color='red')
    else:
        window[r1c1].update(text_color='red')

    if dong in ['111','112'] and ho.isnumeric() and int(ho) >= 2200:
            dong_index = find_dong(dong+'-22')      # 111-2201 ~ 111-28
            sedae = dong_sedae_floor_post_ev[dong_index][1]
            floor = dong_sedae_floor_post_ev[dong_index][2]
            if int(ho) % 100 in range(1,sedae+1) and int(ho) // 100 in range(1,floor+1):
                window[r1c1].update(text_color=base.fg)
            else:
                window[r1c1].update(text_color='red')

    if dong in ['127','128','129'] and ho.isnumeric() and int(ho) >= 2100:
            dong_index = find_dong(dong+'-21')      # 111-2201 ~ 111-28
            sedae = dong_sedae_floor_post_ev[dong_index][1]
            floor = dong_sedae_floor_post_ev[dong_index][2]
            if int(ho) % 100 in range(1,sedae+1) and int(ho) // 100 in range(1,floor+1):
                window[r1c1].update(text_color=base.fg)
            else:
                window[r1c1].update(text_color='red')
def validate_date(r1):
    def valid_day(month,day):
        try:
            datetime(2022,int(month),int(day))
            return True
        except:
            return False

    end_date = get_row(r1)[1]
    if end_date.count('/') == 1:# and '/' in end_date:
        month,day = end_date.split('/')
        valid = valid_day(month,day) #22,02,28 -> 22,02,30 -> XXX valueError
    else:
        valid = False

    r1c1 = f'rc{r1}1'
    if valid:
        window[r1c1].update(text_color=base.fg)
    else:
        window[r1c1].update(text_color='red')
    return valid
# NOTE calculate, conditional_format
def conditional_format(r1):
    if not validate_date(r1): return
    enddate = get_row(r1)[1] # NOTE 종료일
    date = datetime.strptime(f'22/{enddate}','%y/%m/%d')
    today = datetime.today()
    r1c1 = f'rc{r1}1'  
    #  27         26
    td = date - datetime(today.year,today.month,today.day)
    if   td == timedelta(0): window[r1c1].update(background_color='#f00')
    elif td == timedelta(1): window[r1c1].update(background_color='#c50')
    elif td == timedelta(2): window[r1c1].update(background_color='#750')
    else:                    window[r1c1].update(background_color=base.bg)
def calculate_row(r1):
    # NOTE get row
    row = get_row(r1)
    #if  not (dong:= row[2]): return  # dong is ''
    validate_date(r1)
    validate_dong(r1)
    validate_ho(r1)
    # NOTE calculate 초소[4], EV[5], 보양X[6], 2호기 설치[7], 보양재 제거[8]
    # --------- row[4] : 초소  ---------------
    row[4] = find_post(row[2])
    # NOTE update row
    conditional_format(r1)
    update_row(r1,row)
# NOTE sort 
def sort_rows(event):
    events = ['no','endday','dong','ho','post','company','contact','etc']
    col = events.index(event)
    def mysort(row):        return row[col]      if row[col] else str(9999)
    def kr_sort(row):       return row[col]      if row[col] else '히'
    def number_sort(row):   return int(row[col]) if row[col] else 9999
    def date_sort(row):
        if row[col]:
            return datetime.strptime(row[col],'%m/%d')
        else:
            return datetime.strptime('12/31','%m/%d')

    rows = get_rows()
    if event in ['no','post']:
        rows.sort(key=number_sort)
    elif event == 'endday':
        rows.sort(key=date_sort)
    elif event == 'company':
        rows.sort(key=kr_sort)
    else:                      
        rows.sort(key=mysort)

    # NOTE update sorted rows 
    for r1,row in enumerate(rows):
        update_row(r1,row)
# NOTE update
def update_row(r1,row):
    # NOTE r1 : row number, c1: column number
    for c1 in range(number_of_cols):
        window[f'rc{r1}{c1}'].update(value=row[c1])
def update_rows():
    #calculate_row, range(number_of_rows))
    #for r1 in range(number_of_rows):
    #   calculate_row(r1)
    [ calculate_row(r1) for r1 in range(number_of_rows) ]
def clear_rows():
    for r1 in range(number_of_rows):
        for c1 in range(number_of_cols):
            r1c1 = 'rc{}{}'.format(r1,c1)
            window[r1c1].update(value='')
# NOTE read, save, open file
def read_rows_from_excel(date=datetime.today()):
    def get_dataframe(excelfile):
        # NOTE disable chained assignments
        pd.options.mode.chained_assignment = None
        df = pd.read_excel(excelfile,sheet_name='세대공사', skiprows = [0,1,2,3])
        df = df.drop(df.columns[[1,5,6,7]], axis=1)
        return df
    clear_rows()
    excelfile = get_dailyreportfile(date)[0]
    #XXX FileNotFoundError
    df = get_dataframe(excelfile)
    rows =[]
    for row in df.values.tolist():
        row[1] = row[1].strftime('%m/%d') #NOTE 종료일 22/04
        row += ['','','','']
        rows.append(row)

    # initial update window
    for r1,row in enumerate(rows):
        update_row(r1,row)
def open_csv(event):
    if event == rcm.open_csv_today  : csvfile = rcm.csvfile_today
    if event == rcm.open_csv_nextday: csvfile = rcm.csvfile_nextday
    if event == 'open csv':
        csvfile = sg.PopupGetFile('interior*,csv',file_types=(('csv files','csv interior*.csv',)))
    if not csvfile or not file_exists(csvfile):
        print(f'{csvfile} not exist')
        return
    print(f'... opening {csvfile=}')
    window['csvfile'].update( value=Path(csvfile).name )
    with open(csvfile, 'r') as file:
        reader = list( csv.reader(file) )[1:]
        for r1,row in enumerate( row for row in reader ):
            update_row(r1,row) 
def save_csv(event):
    if event == rcm.save_as_csv_today  : csvfile = rcm.csvfile_today
    if event == rcm.save_as_csv_nextday: csvfile = rcm.csvfile_nextday
    window['csvfile'].update(value=csvfile)
    print(f'... saving {csvfile=}')
    with open(csvfile, 'w',newline='') as f:
        write = csv.writer(f)
        write.writerow(['NO','종료일','동','호수','관할초소','공사업체','연락처','비고'] )
        write.writerows( get_rows() )
# NOTE create sg.Window
window = sg.Window('세대공사현황',layout,background_color=base.bg, margins=(40,30), size=(950,900), resizable=True,
                    keep_on_top=False,right_click_menu = rcm.right_click_menu, finalize=True)
#NOTE ---- initialize rows -------------
update_rows()

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    else:
        update_rows()
    if 'read excel' in event: read_rows_from_excel()
    if 'save as'    in event: save_csv(event)
    if 'open'       in event: open_csv(event)
    if event in ['no','endday','dong','post','company']: sort_rows(event)

    update_rows()
window.close()
