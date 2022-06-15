from import_components import *

#   StatusBox:
#       MyLabel:
#           id: id_status
#           text: 'status bar'
#           font_size: 20
#           bold: True

class StatusLabel(MyLabel):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bold = True
        #self.font_size = 16

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
        self.statusbox = MDBoxLayout(size_hint=(0.78,1))
        self.selectbox = MDBoxLayout(size_hint=(0.12,1))
        self.timebox   = MDBoxLayout(size_hint=(0.1,1))
        self.statuslabel = StatusLabel(text='', text_color= (0,1,0,1))
        self.selectlabel = SelectLabel(text='', text_color =(0,1,1,1) )
        self.timelabel   = TimeLabel(text='')
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
