from import_components import *

class XlButton(IB1):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.text_color = Color.files.fg
        self.icon_color = Color.files.icon

class MyFilesBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.spacing = 0
        self.create_layout()

    def create_layout(self):
        self.minwonbtn          =  XlButton(text='민원처리내역.xlsx',  icon  =  'numeric-1-circle',on_press=self.on_press)
        self.dailyreportbtn1    =  XlButton(text='dailyreportfile1',   icon  =  'numeric-2-circle',on_press=self.on_press)
        #self.dailyreportbtn2    =  XlButton(text='dailyreportfile2',   icon  =  'microsoft-excel', on_press=self.on_press)
        self.monthlycommutebtn  =  XlButton(text='monthlycommutefile', icon  =  'numeric-3-circle',on_press=self.on_press)
        self.add_widget(self.minwonbtn)
        self.add_widget(self.dailyreportbtn1)
        #self.add_widget(self.dailyreportbtn2)
        self.add_widget(self.monthlycommutebtn)

    def on_press(self,btn):
        root = Path(__file__).parent
        if btn == self.minwonbtn:
            os.startfile(getminwonfile(root))
        if btn == self.dailyreportbtn1:
            os.startfile( get_dailyreportfile(datetime(*self.date))[0] )
        # \\Main\d\01.업무문서\04.출근부 관련\02.각 조별 월별 출근부\202206 A,B,C조별 월별출근부(반포자이).xlsx
        if btn == self.monthlycommutebtn:
            os.startfile(self.commutefile)

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
