from Wigets import *

class OffBox(BoxLayout):
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



