from import_components import *


class MyServicesBox(MDGridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.rows = 3
        self.padding = 0,0,0,0
        self.spacing = 0,0
        #self.root = MDApp.get_running_app().root
        self.create_layout()

    def create_layout(self):
        #print(minwonfile)
        self.evbtn         = MyEVButton(text='EV:1899-7144',on_press=self.on_press)
        self.homenetbtn    = MyHomenetButton(text='홈넷:1111',on_press=self.on_press)
        self.vaultbtn      = MyVaultButton(text='금고:1234',on_press=self.on_press)
        self.cctvbtn       = MyCCTVButton(text='CCTV:1566-7896 ',on_press=self.on_press)
        self.doorbtn       = MyDoorButton(text='세대현관',on_press=self.on_press)
        self.contactbtn    = MyContactButton(text='직원연락처',on_press=self.on_press)
        self.a1Fmapbtn     = MyMapButton(text='1F(지도)',on_press=self.on_press)
        self.b1Fmapbtn     = MyMapButton(text='B1F(지도)',on_press=self.on_press)
        self.b1FCCTVmapbtn = MyMapButton(text='B1F(CCTV)',on_press=self.on_press)
        self.add_widget(self.evbtn)
        self.add_widget(self.homenetbtn)
        self.add_widget(self.vaultbtn)
        self.add_widget(self.cctvbtn)
        self.add_widget(self.doorbtn)
        self.add_widget(self.contactbtn)
        self.add_widget(self.a1Fmapbtn)
        self.add_widget(self.b1Fmapbtn)
        self.add_widget(self.b1FCCTVmapbtn)

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
