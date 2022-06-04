from import_components import *
from functools import partial
from starthelp.starthelp import *
from mycal.mycalendar import MyCalendar
from datetime import datetime,timedelta
import os

#Window.clearcolor = (0.5,0.5,0.5,1)
LabelBase.register(name='NanumGothic', fn_regular='NanumGothic.ttf',fn_bold='NanumGothicBold.ttf')

class MyLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = 0.6,0.6,0.6,1
        self.size = self.texture_size
        self.font_name='NanumGothic'
        #self.bind(size=self.setter('text_size'))    XXX comment this ALWAYS
        

class OffBox(MDBoxLayout):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 0
        self.spacing = 5
        self.create_layout()

    def create_layout(self,date=datetime(2022,6,1)):
        for off in convert_offworkers(date):
            grid = GridLayout(cols=5,padding=5,spacing=2)
            labels = list()
            labels.append(MyLabel(text=off[0],size_hint=(0.2,1), halign= 'center'))
            labels.append(MyLabel(text=off[1],size_hint=(0.1,1), halign= 'center'))
            labels.append(MyLabel(text=off[2],size_hint=(0.3,1), halign='left'))
            labels.append(MyLabel(text=off[3],size_hint=(0.1,1), halign='center'))
            labels.append(MyLabel(text=off[4],size_hint=(0.3,1), halign='left'))
            for label in labels:
                label.bind(size=label.setter('text_size'))    
                grid.add_widget(label)
            self.add_widget(grid)

    def update_offworkers(self,date):
        print('==>',self.parent)
        print('================>',self, date)
        #print('==>',self.root)
        off = convert_offworkers(datetime(*date))
        colors = [(0.6,0.6,0.6)]*5
        if 'A' in off[1]:
            colors[0] = 0,0.4,0.9,1
            colors[1] = 0,0.4,0.9,1
        elif 'A' in off[3]:
            colors[0] = 0,0.4,0.9,1
            colors[3] = 0,0.4,0.9,1
        else:
            colors = [0.6,0.6,0.6,1]*5
        for i,grid in enumerate( reversed(self.children) ):
            for j,label in enumerate(reversed(grid.children) ):
                label.text = off[i][j]
                label.color = colors[j]


if __name__ ==  '__main__':

    kv = '''
<RootWidget@MDBoxLayout>:
    orientation:'vertical'
<OffBox@MDBoxLayout>:
    orientation:'vertical'

<RootWidget>:
    myoffworkers: id_myoffworkers
    OffBox:
        id:  id_myoffworkers
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
        def on_press(self):
            self.date = (2022,6,12)
            self.myoffworkers.update_offworkers(self.date)

    class TestApp(MDApp):
        def build(self):
            return RootWidget()

    TestApp().run()
