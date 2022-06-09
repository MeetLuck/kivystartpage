from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.chip import MDChip
from kivy.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.config import Config
from kivy.properties import ObjectProperty
from starthelp.starthelp import *
from functools import partial
from kivy.utils import get_color_from_hex as colorhex
from kivy.clock import Clock
from kivy.uix.popup import Popup

from os.path import dirname,join


#To get rid of the red dot:
Config.set('input', 'mouse', 'mouse,disable_multitouch')

#To set the icon so you don’t see the Kivy Icon first:
#Config.set('kivy', 'window_icon','your_app_icon_64x64.png' )

#So pressing esc does not close your program:
#Config.set('kivy', 'exit_on_escape', 0)

LabelBase.register(name='NanumGothic', fn_regular=join( dirname(__file__),'NanumGothic.ttf'),fn_bold=join( dirname(__file__),'NanumGothicBold.ttf'))
LabelBase.register(name='NotoSerifKR', fn_regular=join( dirname(__file__),'NotoSerifKR-Regular.otf'),fn_bold=join( dirname(__file__),'NotoSerifKR-Bold.otf'))
LabelBase.register(name='GothicA1', fn_regular=join( dirname(__file__),'GothicA1-Regular.ttf'),fn_bold=join( dirname(__file__),'GothicA1-Bold.ttf'))
#LabelBase.register(name='NanumGothic', fn_regular='NanumGothic.ttf',fn_bold='NanumGothicBold.ttf')

class base:
    fg = 110/255,130/255,150/255,1
    bg = 0,16/255,38/255,1
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
        bg   = 0,16/255,38/255,1
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

class MyIconButton(MDRectangleFlatIconButton):
    #def __init__(self,font_size=14, md_bg_color=(0,0,0,0),**kwargs):
    def __init__(self,font_size=14,**kwargs):
        super().__init__(**kwargs)
        self.theme_text_color = "Custom"
        self.line_color = (0,0,0,0)
        self.font_name = 'NotoSerifKR'
        #self.font_name = 'NotoSerifKR-Bold.otf'

class MyExcelButton(MyIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "microsoft-excel"
        self.text_color = Color.files.fg
        self.icon_color = Color.files.icon

class MyApplicationButton(MyIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "application"
        self.text_color = Color.cmds.fg
        self.icon_color = Color.cmds.icon

class MyDBButton(MyIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "database"
        self.text_color = Color.cmds.fg
        self.icon_color = Color.cmds.icon

class MyPrinterButton(MyIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "printer"
        self.font_size = 14
        self.md_bg_color =0,0,0,0
        self.text_color = Color.cmds.fg
        self.icon_color = Color.cmds.icon
        self.font_name = 'NotoSerifKR'
        self.line_color = 0,0,0,0

class MyFoldersButton(MyIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "folder"
        self.text_color = Color.folders.fg
        self.icon_color = Color.folders.bg

class MyEVButton(MyIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "elevator"
        self.text_color = Color.ev.fg
        self.icon_color = Color.ev.icon

class MyCCTVButton(MyIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "cctv"
        self.text_color = Color.cctv.fg
        self.icon_color = Color.cctv.icon

class MyHomenetButton(MyIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "home"
        self.text_color = Color.homenet.fg
        self.icon_color = Color.homenet.icon

class MyVaultButton(MyIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "safe"
        self.text_color = Color.vault.fg
        self.icon_color = Color.vault.icon

class MyDoorButton(MyIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "door"
        self.text_color = Color.door.fg
        self.icon_color = Color.door.icon


class MyContactButton(MyIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "contacts"
        self.text_color = Color.contact.fg
        self.icon_color = Color.contact.icon

class MyMapButton(MyIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.icon = "map"
        self.text_color = Color.map.fg
        self.icon_color = Color.map.icon
        #self.line_color = 0,1,0,1
