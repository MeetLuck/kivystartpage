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
Config.set('graphics', 'kivy', ["바탕보통", r'C:\Windows\Fonts\batang.ttc'])

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
        self.update_offworkers()
        return  self.root

    def update_offworkers(self):
        from datetime import datetime,timedelta
        off_box = self.root.ids['id_offworkers']
        date = datetime(*self.date)
        day = f'{date.month}/{date.day}'
        #print(self.date)
        print(day)
        for i,label in enumerate(reversed(off_box.children)):
            offday,offnight = get_offworkers(date + timedelta(days=i))
            dayworkers = '\t'.join(offday)
            nightworkers = '\t'.join(offnight)
            print(offday,offnight)
            text = f'[color=#007700]{day}[/color][color=#005500]{dayworkers}'
            text += f'{offnight}[/color]'
            print(text)
            #label.font_name = r'C:\Windows\Fonts\batang.ttc'
            label.font_name ="NanumGothicBold"
            label.text = f'[b]{text}[/b]'
            #print(off_day)
            #print(i,label.text)


    def on_release(self,mycal,btn):
        self.date = mycal.date
        self.update_offworkers()



Mystartpage().run()
