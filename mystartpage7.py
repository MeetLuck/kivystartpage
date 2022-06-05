from import_components import *

from functools import partial
from starthelp.starthelp import *
from mycal.mycalendar import MyCalendar
from myoffworkers import *
from datetime import datetime,timedelta
import os

Window.size = 1200,1800

class MyStartBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.update(self.mycalendar.date)

    def on_press(self,date:tuple):
        print(date)
        self.update(date)

    def update(self,date):
        self.offworkers.update(date)

class Mystartpage(MDApp):
    def build(self):
        Window.clearcolor = 0,16/255,38/255,1
        return MyStartBox()




Mystartpage().run()
