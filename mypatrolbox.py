from import_components import *

class patrolB(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        #self.font_name = 'GothicA1'
        #$self.font_name = 'NotoSerifKR'
        self.bold = True
        self.color = base.fg
        self.background_color = Color.files.bg
        #self.background_color = Color.files.bg
        self.font_size = 20

class patrolG(MDGridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 4


class MyPatrolBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.padding = 2
        self.spacing = 1
        #self.root = MDApp.get_running_app().root
        self.create_layout()

    def create_row(self,patrol):
        print(patrol)
        self.grid = patrolG() 
        self.grid.add_widget( patrolB(text=patrol[0]) )
        #self.grid.add_widget( patrolB(text=':') )
        self.grid.add_widget( patrolB(text=patrol[1]) )
        self.grid.add_widget( patrolB(text=patrol[2]) )
        self.grid.add_widget( patrolB(text=patrol[3]) )
        self.add_widget(self.grid)

    def create_layout(self):
        self.create_row('09  2 6 9'.split())
        self.create_row('10  1 5 8'.split())
        self.create_row('11  3 7 10'.split())
        self.create_row('13  2 6 9'.split())
        self.create_row('14  1 5 8'.split())
        self.create_row('15  3 7 10'.split())
        #print(minwonfile)

    def on_press(self,btn):
        root = Path(__file__).parent
        if btn == self.minwonreportbtn: os.system( 'python {}'.format(minwonpyfile) )
        if btn == self.minwonDBbtn:     os.system( 'python {}'.format(minwondbfile) )
        if btn == self.dBBrowserbtn:    os.startfile(dbbrowserfile)
        if btn == self.HPScanbtn:       os.startfile(hpscanfile)

if __name__ == '__main__':
    Window.size = 200,150
    class Test(MDApp):
        def build(self):
            return MyPatrolBox()
    Test().run()
