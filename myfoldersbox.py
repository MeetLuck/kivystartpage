from import_components import *

class MyFoldersBox(MDGridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.rows = 4
        self.padding = 0,0,0,0
        self.spacing = 5,0
        #self.root = MDApp.get_running_app().root
        self.create_layout()

    def create_layout(self):
        #print(minwonfile)
        #self.workfolderbtn          = FB(text=' 업무문서            ', icon = 'numeric-6-circle',on_press=self.on_press)
        self.workfolderbtn          = IB1(text=' 업무문서', icon = 'numeric-6-circle-outline',icon_color = base.icon1,on_press=self.on_press)
        self.commutefolderbtn       = IB1(text=' 출근부  ', icon = 'numeric-7-circle-outline',icon_color = base.icon1,on_press=self.on_press)
        self.weeklyreportfolderbtn  = IB1(text=' 주간업무', icon = 'numeric-8-circle-outline',icon_color = base.icon1,on_press=self.on_press)
        self.incidentfolderbtn      = IB1(text=' 사건사고', icon = 'folder',on_press=self.on_press)
        self.Afolderbtn             = IB1(text=' A조',      icon = 'folder',on_press=self.on_press)
        self.excellinkfolderbtn     = IB1(text=' 엑셀링크', icon = 'folder',on_press=self.on_press)
        self.infofolderbtn          = IB1(text=' 안내문',   icon = 'numeric-9-circle-outline',icon_color=base.icon1,on_press=self.on_press)
        self.dummy1btn              = IB1(text=' ',         icon = 'folder',on_press=self.on_press)
        self.parkfolderbtn          = IB1(text=' 박종우',   icon = 'folder',on_press=self.on_press)
        self.cctvfolderbtn          = IB1(text=' CCTV',     icon = 'folder',on_press=self.on_press)
        self.startfolderbtn         = IB1(text=' startpage',icon = 'folder',on_press=self.on_press)
        self.dummy2btn              = IB1(text=' ',         icon = 'folder',on_press=self.on_press)
        self.add_widget(self.workfolderbtn)
        self.add_widget(self.commutefolderbtn)
        self.add_widget(self.weeklyreportfolderbtn)
        self.add_widget(self.incidentfolderbtn)
        self.add_widget(self.infofolderbtn)
        self.add_widget(self.Afolderbtn)
        self.add_widget(self.excellinkfolderbtn)
        self.add_widget(self.parkfolderbtn)
        self.add_widget(self.cctvfolderbtn)
        self.add_widget(self.startfolderbtn)
        self.add_widget(self.dummy1btn)
        self.add_widget(self.dummy2btn)

    def on_press(self,btn):
        root = Path(__file__).parent
        if btn == self.workfolderbtn:           os.startfile(workfolder)                                      
        if btn == self.commutefolderbtn:        os.startfile(commutefolder)
        if btn == self.weeklyreportfolderbtn:   os.startfile(weeklyworkfolder)
        if btn == self.Afolderbtn:              os.startfile(Afolder)
        if btn == self.excellinkfolderbtn:      os.startfile(excellinkfolder)
        if btn == self.infofolderbtn:           os.system('explorer.exe /n,{}'.format(infofolder) )
        if btn == self.parkfolderbtn:           os.startfile(parkfolder)
        if btn == self.cctvfolderbtn:           os.startfile(cctvfolder)
        if btn == self.startfolderbtn:          os.startfile(banpofolder)
        if btn == self.incidentfolderbtn:       os.startfile(incidentfolder)
                                                


if __name__ == '__main__':

    class Test(MDApp):
        def build(self):
            return MyFoldersBox()
    Test().run()
