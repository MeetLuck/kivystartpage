from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.config import Config
from os.path import dirname,abspath,join
from functools import partial
from starhelp.starthelp import create_commute_csv,get_offworkers, get_dayornight, get_workteam, get_monthlycommutefile 


#Window.clearcolor = (0.5,0.5,0.5,1)
Window.size = 300,120
#kvfile = join(dirname(__file__),'mycalendar.kv')

class MyLabel(Label):
    background_normal = ''
    def __init__(self, color = (0,0,0,1),background_color=(0.8,0.8,0.8,0), **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.background_color = background_color

class MyOffBox(BoxLayout):


    def __init__(self,date,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.create_layout()

    def create_layout(self):
        from datetime import timedelta
        day_row = get_offworkers(date)
        self.day1 = MyLabel(text=)
        self.add_widget(self.leftbox)
        self.add_widget(self.rightgrid)
        self.create_weekdays()
        self.create_dates()
        #self.update_dates(self.year,self.month)
        print(self.unsel.bg)

if __name__ ==  '__main__':
    class TestApp(MDApp):
        def build(self):
            return MyCalendar()
    TestApp().run()
