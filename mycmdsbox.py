from import_components import *

class MyCmdsButton(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.font_name = 'GothicA1'
        #self.font_name = 'NotoSerifKR'
        self.bold = True
        self.color = Color.files.fg
        self.background_color = Color.files.bg
        self.font_size = 16

class MyCmdsBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.spacing = 0
        #self.root = MDApp.get_running_app().root
        self.create_layout()

    def create_layout(self):
        #print(minwonfile)
        self.minwonreportbtn = MyApplicationButton(text='python minwon.py',on_press=self.on_press)
        self.minwonDBbtn     = MyApplicationButton(text='python minwondb.py',on_press=self.on_press)
        self.dBBrowserbtn    = MyDBButton(text='DB Browser for SQLite',on_press=self.on_press)
        self.HPScanbtn       = MyPrinterButton(text='HP Scan',on_press=self.on_press)
        self.add_widget(self.minwonreportbtn)
        self.add_widget(self.minwonDBbtn)
        self.add_widget(self.dBBrowserbtn)
        self.add_widget(self.HPScanbtn)

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
