from import_components import *

from functools import partial
from starthelp.starthelp import *
from mycal.mycalendar import MyCalendar
from datetime import datetime,timedelta
import os

        
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 5
        self.padding = 0
        self.spacing = 0
        self.create_layout()

    def create_layout(self):
        self.theday       = MyLabel(text='0',size_hint=(0.25,1),halign= 'center')
        self.dayteam      = MyLabel(text='1',size_hint=(0.1,1),halign= 'center')
        self.dayworkers   = MyLabel(text='2',size_hint=(0.3,1),halign='left')
        self.nightteam    = MyLabel(text='3',size_hint=(0.1,1),halign='center')
        self.nightworkers = MyLabel(text='4',size_hint=(0.3,1),halign='left')
        self.add_widget(self.theday)
        self.add_widget(self.dayteam)
        self.add_widget(self.dayworkers)
        self.add_widget(self.nightteam)
        self.add_widget(self.nightworkers)

    def update(self,off): # [6/1,A1,이종화, B1,서광석]
        self.theday.text        = off[0]
        self.dayteam.text       = off[1]
        self.dayworkers.text    = off[2]
        self.nightteam.text     = off[3]
        self.nightworkers.text  = off[4]


class OffBox(MDBoxLayout):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 0
        self.spacing = 0
        self.create_layout()


    def create_layout(self,date=datetime(2022,6,1)):
        for offdata in convert_offworkers(date):
            grid = MyGrid()
            grid.update(offdata)
            self.add_widget(grid)


    def update(self,date):
        off = convert_offworkers(datetime(*date))
        for i,grid in enumerate( reversed(self.children) ):
            # XXX check A1, A2
            theday, dayteam, dayoffs, nightteam, nightoffs = off[i]
            for j,label in enumerate(reversed(grid.children)):
                label.text = off[i][j]
                label.color = base.fg
                label.bold = False
                if dayteam in 'A1A2' and j in [0,1,2]:
                    label.color = Color.off.day
                    label.bold = True
                if nightteam in 'A1A2' and j in [0,3,4]:
                    label.color = Color.off.night
                    label.bold = True

if __name__ ==  '__main__':

    kv = '''
<RootWidget@MDBoxLayout>:
    orientation:'vertical'
#<OffBox@MDBoxLayout>:
#    orientation:'vertical'

<RootWidget>:
    myoffworkers:id_myoffworkers
    OffBox:
        id: id_myoffworkers
    Button:
        text:'change date'
        on_press: root.on_press()
    '''
    Builder.load_string(kv)
    Window.size = 600,400 #kvfile = join(dirname(__file__),'mycalendar.kv')
    Window.clearcolor = 0,0,0,1
    class RootWidget(MDBoxLayout):
        #date = ObjectProperty()
        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            self.date = (2022,6,1)
            print( datetime( *self.date))
        def on_press(self):
            self.date = (2022,6,12)
            self.myoffworkers.update(self.date)

    class TestApp(MDApp):
        def build(self):
            return RootWidget()

    TestApp().run()
