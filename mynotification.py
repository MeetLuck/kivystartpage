from import_components import *

class MyNotiLabel2(MDLabel):
    def __init__(self, size_hint_x = None, width = 80, **kwargs):
        super().__init__(size_hint_x = None, width=width , **kwargs)
        self.font_name='NotoSerifKR'
        self.color = base.fg
        self.bold = False
        self.font_size=15
        #self.size = self.texture_size
        #self.size_hint_x = None
        #self.width = 80
        #self.bind(size=self.setter('text_size'))    

class MyNotiLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name='NotoSerifKR'
        self.color = base.fg
        self.bold = False
        self.font_size=15
        self.size = self.texture_size
        #self.bind(size=self.setter('text_size'))    

class MyWeeklyReportGrid(MDGridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 6
        self.padding = 0,0,0,0
        self.spacing = 0,0
        #self.root = MDApp.get_running_app().root
        self.create_layout()

    def create_layout(self):
        self.add_widget( MyNotiLabel(text='주간업무 : ',halign='center') )
        for i in range(5):
            self.add_widget(MyNotiLabel(text='') )
        self.update()

    def update(self,adate:datetime=today):
        # NOTE update weeklyreport
        dates = list( reversed(get_weeklyreports(adate)) )
        print(dates)
        for idx, date in enumerate(dates):
            print('==>',idx,date)
            fg = Color.Dday.fg if date > adate-timedelta(1) else Color.Dday.past
            text = date.strftime("%m-%d") + r' ({}) '.format( get_workteam(date)[0] )
            if len(dates) == 4:
                self.children[0].text=''
                self.children[idx+1].text  = text
                self.children[idx+1].color = fg
            else:
                self.children[idx].text  = text
                self.children[idx].color = fg

        print('updated weeklyreport days')

class MyMonthlyReportGrid(MDGridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 6
        self.padding = 0,0,0,0
        self.spacing = 0,0
        self.create_layout()

    def create_layout(self):
        self.add_widget( MyNotiLabel(text='월간업무 : ',halign='center') )
        for i in range(5):
            self.add_widget(MyNotiLabel(text='') )
        self.update()

    def update(self,adate=today):
        # NOTE update 월간보고
        monthly_date = datetime(adate.year,adate.month,20)
        if get_weekday(monthly_date)=='토': monthly_date = datetime(adate.year,adate.month,20-1)
        if get_weekday(monthly_date)=='일': monthly_date = datetime(adate.year,adate.month,20-2)
        fg = Color.Dday.fg if monthly_date > today-timedelta(1) else Color.Dday.past
        self.children[4].text = monthly_date.strftime('%m-%d') + r' ({}) '.format( get_workteam(monthly_date)[0] )
        self.children[4].color = fg
        print('updated monthlyreport days')

class MyDdayBox(MDGridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 5
        self.padding = 0,0,0,0
        self.spacing = 0
        self.create_layout()

    def get_Dday(self,date) -> int:
        from calendar import monthrange
        start,end = monthrange(date.year, date.month)
        return end-date.day

    def create_grid(self,label1,label2):
        grid = MDGridLayout(cols=2)
        grid.add_widget(label1)
        grid.add_widget(label2)
        self.add_widget(grid)

    def create_label(self,date=today):
        self.dday  = self.get_Dday(date)
        ddaylabel = MyNotiLabel2()
        ddaylabel.text  = f'D-{str(self.dday)}'
        ddaylabel.color = Color.Dday.fg  if self.dday <= 5 else Color.Dday.past
        return ddaylabel

    def create_layout(self):
        from calendar import monthrange
        end = monthrange(today.year, today.month)[1]
        # D-day(31)
        label = MyNotiLabel2(text=f'비품({end}) : ',width=75);         self.create_grid(label,self.create_label())
        label = MyNotiLabel2(text=f'직무교육({end}) : ',width=110);    self.create_grid(label,self.create_label())
        label = MyNotiLabel2(text=f'연차계획({end}) : ',width=110);    self.create_grid(label,self.create_label())
        label = MyNotiLabel2(text=f'출근현황표({end}) : ',width=120);  self.create_grid(label,self.create_label())
        label = MyNotiLabel2(text=f'지문인식기(05) : ',width=120);     self.create_grid(label,self.create_label(today-timedelta(days=5)))

    def update(self,adate=today):
        # NOTE update 월간보고
        monthly_date = datetime(adate.year,adate.month,20)
        if get_weekday(monthly_date)=='토': monthly_date = datetime(adate.year,adate.month,20-1)
        if get_weekday(monthly_date)=='일': monthly_date = datetime(adate.year,adate.month,20-2)
        fg = Color.Dday.fg if monthly_date > today-timedelta(1) else Color.Dday.pas
        self.children[4].text = monthly_date.strftime('%m-%d') + r' ({}) '.format( get_workteam(monthly_date)[0] )
        self.children[4].color = fg
        print('updated monthlyreport days')

if __name__ == '__main__':

    Window.size = 1200,100

    class Root(MDBoxLayout):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            self.orientation = 'vertical'
            self.add_widget( MyWeeklyReportGrid() )
            self.add_widget( MyMonthlyReportGrid() )
            self.add_widget( MyDdayBox() )

    class Test(MDApp):
        def build(self):
            return Root()
    Test().run()
