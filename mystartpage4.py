from Wigets import *
import os


def convert_offworkers(date:datetime) -> list: # [6/1, A1, 이종화 B1 육백근]
    offs = list()
    for i in range(4):
        adate = date + timedelta(days=i)
        aday = f'{adate.month}/{adate.day}'
        offs.append([aday] + get_offworkers(adate)[1:] )
    return offs


def update_offworkers(box,date:tuple):
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
            btn.bind(on_release=self.on_release)
    def add_layout_offworkers(self):
        date = datetime(*self.date)
        color = 0,0,0,1
        font_name = 'NanumGothic'
        for off in convert_offworkers(date):
            grid = GridLayout(cols=5,padding=15,spacing=2)
            grid.add_widget( Label(text=off[0],color=color,font_name=font_name,size_hint = (0.2,1), halign = 'right') )
            grid.add_widget( Label(text=off[1],color=color,font_name=font_name,size_hint=(0.1,1) , halign = 'center') )
            label = Label(text=off[2],color=color,font_name=font_name,size_hint=(0.3,1))
            label.bind(size=label.setter('text_size'))    
            grid.add_widget(label)
            grid.add_widget( Label(text=off[3],color=color,font_name=font_name,size_hint=(0.1,1), halign='center') )
            label = Label(text=off[4],color=color,font_name=font_name,size_hint=(0.3,1),halign='left')
            label.bind(size=label.setter('text_size'))    
            grid.add_widget(label)
            self.offworkers.add_widget(grid)

    def on_release(self,btn):
        self.date = self.mycal.date
        update_offworkers(self.offworkers,self.date)

class Mystartpage(MDApp):
    def build(self):
        return MyStartBox()




Mystartpage().run()
