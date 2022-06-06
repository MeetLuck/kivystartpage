from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.config import Config
from kivy.properties import ObjectProperty
from starthelp.starthelp import *

from os.path import dirname,join
LabelBase.register(name='NanumGothic', fn_regular=join( dirname(__file__),'NanumGothic.ttf'),fn_bold=join( dirname(__file__),'NanumGothicBold.ttf'))
LabelBase.register(name='NotoSerifKR', fn_regular=join( dirname(__file__),'NotoSerifKR-Regular.otf'),fn_bold=join( dirname(__file__),'NotoSerifKR-Bold.otf'))
LabelBase.register(name='GothicA1', fn_regular=join( dirname(__file__),'GothicA1-Regular.ttf'),fn_bold=join( dirname(__file__),'GothicA1-Bold.ttf'))
#LabelBase.register(name='NanumGothic', fn_regular='NanumGothic.ttf',fn_bold='NanumGothicBold.ttf')

class Color:
    fg = 110/255,130/255,150/255,1
    bg = 0,16/255,38/255,1
    black = 0,0,0,1
    #fg = 90/255,110/255,110/255,1
    class off:
        day   = 0, 70/255, 255/255, 1
        night = 0, 70/255, 255/255, 1
    class files:
        fg   = 0, 130/255, 255/255, 1
        #fg   = 0, 150/255, 255/255, 1
        #fg   = 0, 50/255, 255/255, 1
        bg   = 0,16/255,38/255,1
