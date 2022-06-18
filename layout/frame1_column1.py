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
    key='-CAL-',justification = 'c',readonly = True,disabled_readonly_background_color=lbox.bg,text_color=base.fg,\
    enable_events=True,size=(10,1),pad=(10,10) )
calendar = sg.CalendarButton(
    'Cal',size=(3,1),font=cal.font,button_color=cal.color,enable_events=True,target='-CAL-',key='_CALENDAR_',\
    format=('%Y%m%d'),pad=(0,10),default_date_m_d_y=default_date )

row_calendar = [ input_field, calendar ]
cols_offs = list()
cols_offs.append( row_calendar )
for r in range(1,4+1):
    cols_offs.append(\
    [ offdate_Text("/",f'day{r}'),    offteam_Text("A1",f'day{r}team'),   offworker_Text("",f'day{r}workers'),
      offteam_Text("",'placeholder'), offteam_Text("B1",f'night{r}team'), offworker_Text("",f'night{r}workers') ] )

listbox = [ sg.Listbox(
    values=patrol_day,font=lbox.font,size=(20,8), background_color = base.bg, text_color=base.fg,pad=(50,2),auto_size_text = True,\
    highlight_background_color=lbox.bg,highlight_text_color = lbox.fg, no_scrollbar = True,key='patrol') ]

cols_patrol = [
        listbox,
        [ sg.Image(source=None,key='dong_post',pad=(40,10) ) ] ]

frame_calendar = [ sg.Frame('', cols_offs,   background_color=base.bg,font=base.font, expand_x=True, pad=(20,5), border_width=0)   ]
frame_patrol   = [ sg.Frame('', cols_patrol, background_color=base.bg,font=base.font, expand_x=True, pad=(0,5), border_width=0) ]

col1 = [ frame_calendar, frame_patrol ]
