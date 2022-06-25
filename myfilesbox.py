from import_components import *

class MyFilesBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.spacing = 0
        self.create_layout()

    def create_layout(self):
        self.minwonbtn          =  IB1(text='민원처리내역.xlsx',  icon = 'numeric-1-circle-outline',icon_color=base.icon1,on_press=self.on_press)
        self.dailyreportbtn1    =  IB1(text='dailyreportfile1',   icon = 'numeric-2-circle-outline',icon_color=base.icon1,on_press=self.on_press)
        self.monthlycommutebtn  =  IB1(text='monthlycommutefile', icon = 'numeric-3-circle-outline',icon_color=base.icon1,on_press=self.on_press)
        self.minwonreportbtn    =  IB1(text='python minwon.py',     icon='numeric-4-circle-outline',icon_color=base.icon1,on_press=self.on_press)
        self.HPScanbtn          =  IB1(text='HP Scan',              icon='numeric-5-circle-outline',icon_color=base.icon1,on_press=self.on_press)
        self.minwonDBbtn        =  IB1(text='python minwondb.py',   icon='application',     on_press=self.on_press)
        self.dBBrowserbtn       =  IB1(text='DB Browser for SQLite',icon='database',        on_press=self.on_press)
        self.add_widget(self.minwonbtn)
        self.add_widget(self.dailyreportbtn1)
        self.add_widget(self.monthlycommutebtn)
        self.add_widget(self.minwonreportbtn)
        self.add_widget(self.HPScanbtn)
        self.add_widget(self.minwonDBbtn)
        self.add_widget(self.dBBrowserbtn)

    def on_press(self,btn):
        root = Path(__file__).parent
        if btn == self.minwonbtn: os.startfile(getminwonfile(root))
        if btn == self.dailyreportbtn1: os.startfile( get_dailyreportfile(datetime(*self.date))[0] )
        # \\Main\d\01.업무문서\04.출근부 관련\02.각 조별 월별 출근부\202206 A,B,C조별 월별출근부(반포자이).xlsx
        if btn == self.monthlycommutebtn: os.startfile(self.commutefile)
        if btn == self.minwonreportbtn: os.system( 'python {}'.format(minwonpyfile) )
        if btn == self.minwonDBbtn:     os.system( 'python {}'.format(minwondbfile) )
        if btn == self.dBBrowserbtn:    os.startfile(dbbrowserfile)
        if btn == self.HPScanbtn:       os.startfile(hpscanfile)

    def update(self,date):
        self.date = date
        date1 = datetime(*date)
        date2 = date1 + timedelta(days=1)
        date1str = date1.strftime('%y%m%d')
        date2str = date2.strftime('%y%m%d')
        self.dailyreportbtn1.text = f'일일상황보고 {date1str}.xlsx'
        #self.dailyreportbtn2.text = f'일일상황보고 {date2str}.xlsx'
        self.commutefile = get_monthlycommutefile(date1)
        self.monthlycommutebtn.text = Path(self.commutefile).name


if __name__ == '__main__':

    class Test(MDApp):
        def build(self):
            return MyFilesBox()
    Test().run()
