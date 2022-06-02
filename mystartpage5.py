from import_components import *
import os

LabelBase.register(name='NanumGothic', fn_regular='NanumGothic.ttf',fn_bold='NanumGothicBold.ttf')
Window.size = 1000,800
#Config.set('graphics', 'kivy', ["바탕보통", r'C:\Windows\Fonts\batang.ttc'])
#font_name = '/'.join([os.getenv('SystemRoot'),'fonts/batang.ttc'])

def update_offworkers(box,date):
    offs = convert_offworkers(datetime(*date))
    for i,grid in enumerate( reversed(box.children) ):
        for j,label in enumerate(reversed(grid.children) ):
            label.text = offs[i][j]

class MyStartBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.date = self.mycal.date
        self.add_layout_offworkers()
        for id in self.mycal.ids:
            btn = self.mycal.ids[id]
            #btn.bind(on_release=self.on_release)

    def add_layout_offworkers(self):
        date = datetime(*self.date)
        color = 0,0,0,1
        font_name = 'NanumGothic'
        for off in convert_offworkers(date):
            grid = GridLayout(cols=5,padding=5,spacing=2)
            label = Label(text=off[0],color=color,font_name=font_name,size_hint = (0.2,1), halign = 'center')
            label.bind(size=label.setter('text_size'))    
            grid.add_widget(label)
            label = Label(text=off[1],color=color,font_name=font_name,size_hint=(0.1,1) , halign = 'center')
            label.bind(size=label.setter('text_size'))    
            grid.add_widget(label)
            label = Label(text=off[2],color=color,font_name=font_name,size_hint=(0.3,1),halign='left')
            label.bind(size=label.setter('text_size'))    
            grid.add_widget(label)
            label = Label(text=off[3],color=color,font_name=font_name,size_hint=(0.1,1), halign='center')
            label.bind(size=label.setter('text_size'))    
            grid.add_widget(label)
            label = Label(text=off[4],color=color,font_name=font_name,size_hint=(0.3,1),halign='left')
            label.bind(size=label.setter('text_size'))    
            grid.add_widget(label)
            self.offworkers.add_widget(grid)

    def on_press(self,date:tuple):
        print(date)
        update_offworkers(self.offworkers,date)

    def on_release(self,btn):
        update_offworkers(self.offworkers,self.mycal.date)

class Mystartpage(MDApp):
    def build(self):
        return MyStartBox()




Mystartpage().run()
