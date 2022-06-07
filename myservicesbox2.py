from import_components import *


class MyServicesBox(MDGridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.rows = 4
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
        self.a1Fmapbtn     = MyMapButton(text='지도: 지상',on_press=self.on_press)
        self.b1Fmapbtn     = MyMapButton(text='지하주차장',on_press=self.on_press)
        self.b1FCCTVmapbtn = MyMapButton(text='지하주차장(CCTV)',on_press=self.on_press)
        self.box1 = BoxLayout(orientation='horizontal',padding=0)
        self.box2 = BoxLayout(orientation='horizontal',padding=0)
        self.box3 = BoxLayout(orientation='horizontal',padding=0)
        self.box1.add_widget(self.evbtn)
        self.box1.add_widget(self.homenetbtn)
        self.box1.add_widget(self.vaultbtn)
        self.box2.add_widget(self.cctvbtn)
        self.box2.add_widget(self.doorbtn)
        self.box2.add_widget(self.contactbtn)
        self.box3.add_widget(self.a1Fmapbtn)
        self.box3.add_widget(self.b1Fmapbtn)
        self.box3.add_widget(self.b1FCCTVmapbtn)
        self.add_widget(self.box1)
        self.add_widget(self.box2)
        self.add_widget(self.box3)

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
