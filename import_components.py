from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
from kivymd.uix.button import MDFlatButton, MDIconButton, MDRectangleFlatIconButton, MDRaisedButton
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.popup import Popup
from kivymd.uix.chip import MDChip
from kivymd.uix.behaviors import TouchBehavior
from kivy.clock import Clock
from kivy.app import App
from kivymd.app import MDApp
from kivy.config import Config
from kivy.properties import ObjectProperty, StringProperty
from kivy.utils import get_color_from_hex as colorhex
from kivymd.uix.snackbar import Snackbar
import calendar
from datetime import datetime
from os.path import dirname,join
from starthelp.starthelp import *
from functools import partial


#To get rid of the red dot:
Config.set('input', 'mouse', 'mouse,disable_multitouch')
#To set the icon so you don’t see the Kivy Icon first:
#Config.set('kivy', 'window_icon','your_app_icon_64x64.png' )
#So pressing esc does not close your program:
#Config.set('kivy', 'exit_on_escape', 0)

# XXX fonts
fonts= join( dirname(__file__),'fonts')
NotoSerifKRBold=join( fonts,'NotoSerifKR-Bold.otf')
LabelBase.register(name='NanumGothic', fn_regular=join( fonts,'NanumGothic.ttf'),fn_bold=join( fonts,'NanumGothicBold.ttf'))
LabelBase.register(name='NotoSerifKR', fn_regular=join( fonts,'NotoSerifKR-Regular.otf'),fn_bold=join( fonts,'NotoSerifKR-Bold.otf'))
LabelBase.register(name='GothicA1', fn_regular=join( fonts,'GothicA1-Regular.ttf'),fn_bold=join( fonts,'GothicA1-Bold.ttf'))
#LabelBase.register(name='NanumGothic', fn_regular='NanumGothic.ttf',fn_bold='NanumGothicBold.ttf')

def get_color(color,multiply):
    return list(map(lambda c : c * multiply, color[:-1])) + [1]

class base:
    fg = 110/255,130/255,150/255,1
    bg = 0,0,0.12,1
    #bg = 0,16/255,38/255,1
    icon  = 150/255*0.6, 170/255*0.6, 185/255*0.6, 1
    black  = 0,0,0,1
    white  = 150/255, 170/255, 185/255, 1

class Color:
    class off:
        day     = 0, 50/255,255/255,1
        night   = 0, 50/255,255/255,1
        #night = 110/255,130/255,150/255,1
        #day   = 0, 70/255, 255/255, 1
        #night = 0, 70/255, 255/255, 1
    class files:
        #fg   = 0, 150/255,0/255,1
        fg   = 0, 150/255,0/255,1
        icon   = 0, 100/255,0/255,1
        #bg   = 0,16/255,38/255,1
        bg   = base.bg
    class cmds:
        fg     = 0, 150/255,255/255,1
        icon   = 0, 100/255,255/255,1
    class folders:
        fg   = base.fg
        bg   = 120/255, 120/255, 70/255, 1
    class homenet:
        fg     = 200/255, 70/255, 0,1
        icon   = base.icon
    class vault:
        fg  = base.fg
        icon  = base.icon
    class ev:
        fg     = 200/255, 70/255, 0,1
        icon  = base.icon
    class cctv:
        fg     = 200/255, 70/255, 0,1
        icon  = base.icon
    class door:
        fg  = base.fg
        icon  = base.icon
    class contact:
        fg  = base.fg
        icon  = base.icon
    class map:
        fg  = base.fg
        icon  = base.icon
    class Dday:
        fg   = base.fg
        past = 110/255,130/255,150/255, 0.7
        #past = 0.4,0.4,0.4,1

class MyLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name='NotoSerifKR'
        self.color = base.fg
        self.bold = False
        self.font_size=14
        self.size = self.texture_size
        #self.bind(size=self.setter('text_size'))    

class B1(MDFlatButton):
    def __init__(self,font_size=14,theme_text_color='Custom',line_color=(0,0,0,0),text_color=base.fg,**kwargs):
        super().__init__(font_size=font_size,theme_text_color='Custom',line_color=(0,0,0,0),text_color=text_color,**kwargs)
        self.background_normal = ''
        self.font_name = 'NotoSerifKR'

class IB1(MDRectangleFlatIconButton):
    def __init__(self,font_size=14,theme_text_color='Custom',line_color=(0,0,0,0),text_color=base.fg,**kwargs):
        super().__init__(font_size=font_size,theme_text_color='Custom',line_color=(0,0,0,0),text_color=text_color,**kwargs)
        self.background_normal = ''
        self.font_name = 'NotoSerifKR'


class MyEVButton(IB1):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "elevator"
        self.text_color = Color.ev.fg
        self.icon_color = Color.ev.icon

class MyCCTVButton(IB1):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "cctv"
        self.text_color = Color.cctv.fg
        self.icon_color = Color.cctv.icon

class MyHomenetButton(IB1):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "home"
        self.text_color = Color.homenet.fg
        self.icon_color = Color.homenet.icon

class MyVaultButton(IB1):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "safe"
        self.text_color = Color.vault.fg
        self.icon_color = Color.vault.icon

class MyDoorButton(IB1):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "door"
        self.text_color = Color.door.fg
        self.icon_color = Color.door.icon

class MyContactButton(IB1):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "contacts"
        self.text_color = Color.contact.fg
        self.icon_color = Color.contact.icon

class MyMapButton(IB1):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "map"
        self.text_color = Color.map.fg
        self.icon_color = Color.map.icon
        #self.line_color = 0,1,0,1
