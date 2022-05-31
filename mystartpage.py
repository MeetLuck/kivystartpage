from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
from kivycal.mycalendar import MyCalendar

Window.size = 1000,800

class MyStartBox(MDBoxLayout):
    ...

class Mystartpage(MDApp):
    def build(self):
        return  MyStartBox()


Mystartpage().run()
