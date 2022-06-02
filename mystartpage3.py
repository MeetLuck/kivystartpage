from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
from mycal.mycalendar import MyCalendar
from functools import partial
from starthelp.starthelp import *
from kivy.config import Config
from datetime import datetime,timedelta
from kivy.core.text import LabelBase

#Config.set('graphics', 'kivy', ["바탕보통", r'C:\Windows\Fonts\batang.ttc'])

import os
LabelBase.register(name='NanumGothic', fn_regular='NanumGothic.ttf',fn_bold='NanumGothicBold.ttf')
#font_name = '/'.join([os.getenv('SystemRoot'),'fonts/batang.ttc'])

Window.size = 1000,800

def convert_offworkers(date):
    # [6/1, A1, 이종화 B1 육백근]
    offs = []
    #date = datetime(*date)
    for i in range(4):
        adate = date + timedelta(days=i)
        aday = f'{adate.month}/{adate.day}'
        offs.append([aday] + get_offworkers(adate)[0] + get_offworkers(adate)[1])
    return offs


def update_offworkers(box,date):
    print(date)
    date = datetime(*date)
    offs = convert_offworkers(date)
    for i,grid in enumerate( reversed(box.children) ):
        #print(i,grid,offs[i])
        for j,label in enumerate(reversed(grid.children) ):
            label.text = offs[i][j]

class MyStartBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.date = self.mycal.date
        self.add_layout_offworkers()
        for id in self.mycal.ids:
            btn = self.mycal.ids[id]
            btn.bind(on_release=self.on_release)
        print('MyStartBox ==>',self.mycal)
            #btn.bind(on_release=partial(self.on_release,self.mycal))
        #update_offworkers(self,self.date)
    def add_layout_offworkers(self):
        #day_label.text = f'{self.date.month}/{self.date.day}'
        date = datetime(*self.date)
        #print(self.date)
        color = 0,0,0,1
        font_name = 'NanumGothic'
        for off in convert_offworkers(date):
            grid = MDGridLayout(cols=5,padding=15,spacing=2)
            #grid = MDGridLayout(cols=5,md_bg_color=(0,0.3,0,1),padding=15,spacing=2)
            day_label = Label(text=off[0],color=color,font_name=font_name,size_hint = (0.2,1), halign = 'right')
            dayteam_label = Label(text=off[1],color=color,font_name=font_name,size_hint=(0.1,1) , halign = 'center')
            dayworkers_label = Label(text=off[2],color=color,font_name=font_name,size_hint=(0.3,1))
            dayworkers_label.bind(size=dayworkers_label.setter('text_size'))    
            nightteam_label = Label(text=off[3],color=color,font_name=font_name,size_hint=(0.1,1), halign='center')
            nightworkers_label = Label(text=off[4],color=color,font_name=font_name,size_hint=(0.3,1),halign='left')
            #nightworkers_label.text_size = nightworkers_label.size
            grid.add_widget(day_label)
            grid.add_widget(dayteam_label)
            grid.add_widget(dayworkers_label)
            grid.add_widget(nightteam_label)
            grid.add_widget(nightworkers_label)
            self.offworkers.add_widget(grid)



    def on_release(self,btn):
        self.date = self.mycal.date
        update_offworkers(self.offworkers,self.date)

class Mystartpage(MDApp):
    def build(self):
        # registering our new custom fontstyle
        return MyStartBox()




Mystartpage().run()
