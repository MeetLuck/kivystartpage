from import_components import *

class CmdButton(IB1):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.font_name = 'NotoSerifKR'
        self.bold = True
        self.color = Color.files.fg
        self.background_color = Color.files.bg
        self.text_color = Color.cmds.fg
        self.icon_color = Color.cmds.icon
        #self.font_size = 16

class MyCmdsBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.spacing = 0
        #self.root = MDApp.get_running_app().root
        self.create_layout()

    def create_layout(self):
        #print(minwonfile)
        self.minwonreportbtn  =  CmdButton(text='python minwon.py',     icon='numeric-4-circle',on_press=self.on_press)
        self.HPScanbtn        =  CmdButton(text='HP Scan',              icon='numeric-5-circle',on_press=self.on_press)
        self.minwonDBbtn      =  CmdButton(text='python minwondb.py',   icon='application',     on_press=self.on_press)
        self.dBBrowserbtn     =  CmdButton(text='DB Browser for SQLite',icon='database',        on_press=self.on_press)
        self.add_widget(self.minwonreportbtn)
        self.add_widget(self.HPScanbtn)
        self.add_widget(self.minwonDBbtn)
        self.add_widget(self.dBBrowserbtn)

    def on_press(self,btn):
        root = Path(__file__).parent
        if btn == self.minwonreportbtn: os.system( 'python {}'.format(minwonpyfile) )
        if btn == self.minwonDBbtn:     os.system( 'python {}'.format(minwondbfile) )
        if btn == self.dBBrowserbtn:    os.startfile(dbbrowserfile)
        if btn == self.HPScanbtn:       os.startfile(hpscanfile)

if __name__ == '__main__':

    class Test(MDApp):
        def build(self):
            return MyCmdsBox()
    Test().run()
