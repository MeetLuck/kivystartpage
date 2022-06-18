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
from starthelp import default_date

input_field = sg.Input(
    key='-CAL-',justification = 'c',readonly = True,disabled_readonly_background_color=base.bg,text_color='#0ee',\
    enable_events=True,size=(10,1),pad=(10,10) )
calendar = sg.CalendarButton(
    'Cal',size=(3,1),font=cal.font,button_color=cal.color,enable_events=True,target='-CAL-',key='_CALENDAR_',\
    format=('%Y%m%d'),pad=(0,10),default_date_m_d_y=default_date )

row_calendar = [ input_field, calendar ]

row_theday = [
    offdate_Text("/","day1"),       offteam_Text("A1",f"day{r}team"),   offworker_Text("",f"day{r]workers"),
    offteam_Text("","placeholder"), offteam_Text("B1",f"night{r}team"), offworker_Text("",f"night{r]workers") ]
row_nextday = [
    offdate_Text("/","day2"),       offteam_Text("A2","day2team"),   offworker_Text("","day2workers"),
    offteam_Text("","placeholder"), offteam_Text("B2","night2team"), offworker_Text("","night2workers") ]
row_3rdday = [
    offdate_Text("/","day3"),       offteam_Text("A2","day3team"),   offworker_Text("","day3workers"),
    offteam_Text("","placeholder"), offteam_Text("B2","night2team"), offworker_Text("","night2workers") ]
row_4thday = [
    offdate_Text("/","day4"),       offteam_Text("A2","day4team"),   offworker_Text("","day4workers"),
    offteam_Text("","placeholder"), offteam_Text("B2","night2team"), offworker_Text("","night2workers") ]

listbox = [ sg.Listbox(
    values=patrol_day,font=lbox.font,size=(20,8), background_color = base.bg, text_color=base.fg,pad=(50,2),auto_size_text = True,\
    highlight_background_color=lbox.bg,highlight_text_color = lbox.fg, no_scrollbar = True,key='patrol') ]

cols_calendar = [
        row_calendar, row_theday, row_nextday, row_3rdday, row_4thday,
        ]
cols_patrol = [
        listbox,
        [ sg.Image(source=None,key='dong_post',pad=(40,10) ) ] ]

frame_calendar = [ sg.Frame('', cols_calendar, background_color=base.bg,font=base.font, expand_x=True, pad=(20,5), border_width=0)   ]
frame_patrol   = [ sg.Frame('', cols_patrol, background_color=base.bg,font=base.font, expand_x=True, pad=(0,5), border_width=0) ]

col1 = [ frame_calendar, frame_patrol ]
