from import_components import *

from functools import partial
from starthelp.starthelp import *
from mycal.mycalendar import MyCalendar
from myoffworkers import *
from myfilesbox import *
from mycmdsbox  import *
from myfoldersbox import *
from datetime import datetime,timedelta
import os

Window.size = 1200,900

class MyStartBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.update_date(self.mycalendar.date)

    def update_date(self,date:tuple):
        print(date,type(date))
        self.offworkers.update(date)
        self.myfiles.update(date)

class Mystartpage(MDApp):
    def build(self):
        Window.clearcolor = 0,16/255,38/255,1
        return MyStartBox()




Mystartpage().run()
