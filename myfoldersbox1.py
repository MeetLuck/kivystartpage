from import_components import *

class MyFoldersButton(MDIconButton):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.background_normal = ''
        #self.font_name = 'GothicA1'
        #self.md_bg_color = 0.5,0.5,0.5,1
        #self.size_hint_y = None
        #self.padding = 5
        #self.height = 10
        self.font_name = 'NotoSerifKR-Bold'
        #self.bold = True
        #self.color = Color.black
        #self.background_color = Color.files.bg
        #self.font_size = 12

        #self.icon = "language-python"
        self.icon = 'magnify'
        #pos_hint: {"center_x": .5}
        self.theme_text_color  = "Custom"
        self.text_color =  0, 0, 0, 1
        self.icon_color =  0.5, 0.5, 0.5, 1
        #self.md_bg_color =  get_color_from_hex("#552A7D")

class MyFoldersBox(MDGridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 4
        self.rows = 3
        self.spacing = 0
        #self.root = MDApp.get_running_app().root
        self.create_layout()

    def create_layout(self):
        #print(minwonfile)
        self.workfolderbtn          = MyFoldersButton(text='업무문서',on_press=self.on_press)
        self.commutefolderbtn       = MyFoldersButton(text='출근부',on_press=self.on_press)
        self.weeklyreportfolderbtn  = MyFoldersButton(text='주간업무',on_press=self.on_press)
        self.incidentfolderbtn      = MyFoldersButton(text='사건사고',on_press=self.on_press)
        self.Afolderbtn             = MyFoldersButton(text='A조',on_press=self.on_press)
        self.excellinkfolderbtn     = MyFoldersButton(text='엑셀링크',on_press=self.on_press)
        self.infofolderbtn          = MyFoldersButton(text='안내문',on_press=self.on_press)
        self.dummy1btn              = MyFoldersButton(text=' ',on_press=self.on_press)
        self.parkfolderbtn          = MyFoldersButton(text='박종우',on_press=self.on_press)
        self.cctvfolderbtn          = MyFoldersButton(text='CCTV',on_press=self.on_press)
        self.startfolderbtn         = MyFoldersButton(text='startpage',on_press=self.on_press)
        self.dummy2btn              = MyFoldersButton(text=' ',on_press=self.on_press)
        self.add_widget(self.workfolderbtn)
        self.add_widget(self.commutefolderbtn)
        self.add_widget(self.weeklyreportfolderbtn)
        self.add_widget(self.incidentfolderbtn)
        self.add_widget(self.Afolderbtn)
        self.add_widget(self.excellinkfolderbtn)
        self.add_widget(self.infofolderbtn)
        self.add_widget(self.dummy1btn)
        self.add_widget(self.parkfolderbtn)
        self.add_widget(self.cctvfolderbtn)
        self.add_widget(self.startfolderbtn)
        self.add_widget(self.dummy2btn)

    def on_press(self,btn):
        root = Path(__file__).parent
        if btn == self.minwonreportbtn: os.system( 'python {}'.format(minwonpyfile) )
        if btn == self.minwonDBbtn:     os.system( 'python {}'.format(minwondbfile) )
        if btn == self.dBBrowserbtn:    os.startfile(dbbrowserfile)
        if btn == self.HPScanbtn:       os.startfile(hpscanfile)

if __name__ == '__main__':

    class Test(MDApp):
        def build(self):
            return MyFoldersBox()
    Test().run()
