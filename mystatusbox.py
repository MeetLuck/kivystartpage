from import_components import *


class StatusLabel(MyLabel):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bold = True

class SelectLabel(MyLabel):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bold = True
        #self.font_size = 16

class TimeLabel(MyLabel):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bold = True
        self.font_size = 16


class StatusBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='horizontal'
        self.spacing = 0
        self.statusbox = MDBoxLayout(size_hint=(0.78,1) )
        self.selectbox = MDBoxLayout(size_hint=(0.12,1) )
        self.timebox   = MDBoxLayout(size_hint=(0.1,1))
        self.statuslabel = Label(text='',color=base.fg, font_name=base.font_name,font_size=16)
        self.selectlabel = Label(text='',color=base.fg, font_name=base.font_name,font_size=16)
        self.timelabel   = Label(text='',color=base.fg2,font_name=base.font_name,font_size=16)
        self.statusbox.add_widget(self.statuslabel)
        self.selectbox.add_widget(self.selectlabel)
        self.timebox.add_widget(self.timelabel)
        self.add_widget(self.statusbox)
        self.add_widget(self.selectbox)
        self.add_widget(self.timebox)
        #self.add_widget(self.timelabel)


    def update(self,date):
        ...

if __name__ == '__main__':
    Window.size = 1200,200
    class Test(MDApp):
        def build(self):
            return StatusBox()
    Test().run()
