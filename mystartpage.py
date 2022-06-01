from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
from mycal.mycalendar import MyCalendar
from functools import partial
from starthelp.starthelp import *
from kivy.config import Config
Config.set('graphics', 'kivy', '["Arial", "C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/ariali.ttf", "C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/arialbi.ttf"]')
#or this 

Window.size = 1000,800

class MyStartBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

class Mystartpage(MDApp):
    def build(self):
        self.root = MyStartBox()
        mycal = self.root.ids['id_mycal' ]
        self.date = mycal.date
        for id in mycal.ids:
            btn = mycal.ids[id]
            btn.bind(on_release=partial(self.on_release,mycal))
        self.date = mycal.date
        self.add_offworkers()
        return  self.root

    def add_offworkers(self):
        from datetime import datetime,timedelta
        off_box = self.root.ids['id_offworkers']
        print(self.date)
        date = datetime(*self.date)
        off_day1 = get_offworkers(date)
        off_day2 = get_offworkers(date + timedelta(days=1))
        off_day3 = get_offworkers(date + timedelta(days=2))
        off_day4 = get_offworkers(date + timedelta(days=3))
        print(off_day1)
        off_box.add_widget(MDLabel(text=' '.join(off_day1),pos_hint={'center_x':0.8,'center_y':0.5}))
        #off_box.add_widget(MDLabel(text=off_day2,pos_hint={'center_x':0.5,'center_y':0.5}))
        #off_box.add_widget(MDLabel(text=off_day3,pos_hint={'center_x':0.5,'center_y':0.5}))
        #off_box.add_widget(MDLabel(text=off_day4,pos_hint={'center_x':0.5,'center_y':0.5}))


    def on_release(self,mycal,btn):
        self.date = mycal.date



Mystartpage().run()
