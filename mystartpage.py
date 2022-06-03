from import_components import *

from functools import partial
from starthelp.starthelp import *
from mycal.mycalendar import MyCalendar
from myoffworkers import *
from datetime import datetime,timedelta
import os

LabelBase.register(name='NanumGothic', fn_regular='NanumGothic.ttf',fn_bold='NanumGothicBold.ttf')
Window.size = 1000,800
#Config.set('graphics', 'kivy', ["바탕보통", r'C:\Windows\Fonts\batang.ttc'])
#font_name = '/'.join([os.getenv('SystemRoot'),'fonts/batang.ttc'])

class MyStartBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def on_press(self,date:tuple):
        print(date)
        self.offworkers.update_offworkers(date)

class Mystartpage(MDApp):
    def build(self):
        Window.clearcolor = 0,0,0,1
        return MyStartBox()




Mystartpage().run()
