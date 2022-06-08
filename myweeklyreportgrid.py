from import_components import *

class MyNotiLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name='NotoSerifKR'
        self.color = base.fg
        self.bold = False
        self.font_size=16
        self.size = self.texture_size
        #self.bind(size=self.setter('text_size'))    

class MyNotiLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name='NotoSerifKR'
        self.color = base.fg
        self.bold = False
        self.font_size=16
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

    def update(self,adate=today):
        # NOTE update weeklyreport
        dates = list( reversed(get_weeklyreports(adate)) )
        for no, date in enumerate(dates):
            fg = Color.Dday.fg if date > adate-timedelta(1) else Color.Dday.past
            text = date.strftime("%m-%d") + r' ({}) '.format( get_workteam(date)[0] )
            self.children[no].text= text
            self.children[no].color = fg
        if len(dates) == 4: self.children[4].text=''
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
        fg = Color.Dday.fg if monthly_date > today-timedelta(1) else Color.Dday.pas
        self.children[4].text = monthly_date.strftime('%m-%d') + r' ({}) '.format( get_workteam(monthly_date)[0] )
        self.children[4].color = fg
        print('updated monthlyreport days')

class MyTodoBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.cols = 10
        self.orientation = 'horizontal'
        self.padding = 0,0,0,0
        self.spacing = 0
        self.create_layout()

    def get_Dday(self,date) -> int:
        from calendar import monthrange
        start,end = monthrange(date.year, date.month)
        return end-date.day

    def get_fingerDday(self,today):
        dday = self.get_Dday(today) + 5 if today.day > 5 else 5 - today.day
        fg = Color.Dday.fg if dday <= 5 else Color.Dday.past
        return dday,fg
        #window['d_fingercommute'].update(value='D-{}'.format(dday),text_color=fg)

    def create_layout(self):
        from calendar import monthrange
        end = monthrange(today.year, today.month)[1]
        self.dday  = self.get_Dday(today)
        self.ddaylabels = list()
        for i in range(4):
            ddaylabel = MyNotiLabel()
            ddaylabel.text  = f'D-{str(self.dday)}'
            ddaylabel.color = Color.Dday.fg  if self.dday <= 5 else Color.Dday.past
            self.ddaylabels.append(ddaylabel)
        print(self.ddaylabels)
        # D-day(30)
        self.add_widget( MyNotiLabel(text=f'비품({end}) : ') );         self.add_widget( self.ddaylabels[0] )
        self.add_widget( MyNotiLabel(text=f'직무교육({end}) : ') );     self.add_widget( self.ddaylabels[1] )
        self.add_widget( MyNotiLabel(text=f'연차계획({end}) : ') );     self.add_widget( self.ddaylabels[2] )
        self.add_widget( MyNotiLabel(text=f'출근현황표({end}) : ') );   self.add_widget( self.ddaylabels[3] )
        self.add_widget( MyNotiLabel(text=f'지문인식기(05) : ') )
        # fingerprint 
        text,fg = self.get_fingerDday(today)
        self.fingerlabel = MyNotiLabel(text = f'D-{str(text)}', color = fg )
        self.add_widget(self.fingerlabel)
        #self.update()

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

    class Root(MDBoxLayout):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            self.orientation = 'vertical'
            self.add_widget( MyWeeklyReportGrid() )
            self.add_widget( MyMonthlyReportGrid() )
            self.add_widget( MyTodoBox() )

    class Test(MDApp):
        def build(self):
            return Root()
    Test().run()
