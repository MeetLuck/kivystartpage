from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import Label
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
from mycal.mycalendar import MyCalendar
from functools import partial
from starthelp.starthelp import *
from kivy.config import Config
Config.set('graphics', 'kivy', ["바탕보통", r'C:\Windows\Fonts\batang.ttc'])

Window.size = 1000,800


def update_offworkers(root,date):
    from datetime import datetime,timedelta
    parent = root.ids['id_offworkers']
    offgrid = MDGridLayout(cols=4)
    label1 = Label(text='label1',color=[0,0,1,1])
    label2 = Label(text='label2',color=[0,0,0,1])
    label3 = Label(text='label3',color=[0,0,0,1])
    label4 = Label(text='label4',color=[0,0,0,1])
    offgrid.add_widget(label1)
    offgrid.add_widget(label2)
    offgrid.add_widget(label3)
    offgrid.add_widget(label4)
    parent.add_widget(offgrid)

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
        update_offworkers(self.root,self.date)
        return  self.root

    def on_release(self,mycal,btn):
        self.date = mycal.date
        update_offworkers(self.root,self.date)



Mystartpage().run()
