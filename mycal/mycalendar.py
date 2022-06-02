from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.config import Config
from os.path import dirname,abspath,join
from functools import partial

#Window.clearcolor = (0.5,0.5,0.5,1)
Window.size = 300,120
#kvfile = join(dirname(__file__),'mycalendar.kv')

class MyButton(Button):
    def __init__(self, color = (0,0,0,1),background_color=(0.8,0.8,0.8,0), **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.background_color = background_color
        self.background_normal = ''

class MyCalendar(BoxLayout):

    import calendar
    from datetime import datetime
    now = datetime.now()
    year,month,day = now.year, now.month, now.day
    TextCalendar = calendar.TextCalendar(calendar.SUNDAY)
    unsel = type("unselect", (), {'bg':(0.8,0.8,0.8,0)})
    sel = type("select", (), {'bg':(0.8,0.8,0.8,1)})
    today = type("today", (), {'fg':(0,0.8,0,1)})

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.create_layout()
        self.date = self.year, self.month, self.day

    def create_layout(self):
        self.create_leftbox()
        self.rightgrid = GridLayout(size_hint =( 0.8,1), padding = 0, spacing = 0, rows = 7, cols = 7)
        self.add_widget(self.leftbox)
        self.add_widget(self.rightgrid)
        self.create_weekdays()
        self.create_dates()
        #self.update_dates(self.year,self.month)
        print(self.unsel.bg)

    def create_leftbox(self):
        self.leftbox = BoxLayout( size_hint = (0.2,1), orientation='vertical' )
        self.box1 = BoxLayout( size_hint =(1,0.28), orientation='horizontal')
        self.minusbutton = MyButton(bold=True,  markup=True, text = '[size=16][b]<[/b][/size]')#, on_release = self.on_change_month(-1) )
        self.plusbutton =  MyButton(bold=True,  markup=True, text = '[size=16][b]>[/b][/size]')#, on_release = self.on_change_month(+1) )
        self.minusbutton.bind(on_release = partial(self.on_change_month,-1) )
        self.plusbutton.bind(on_release = partial(self.on_change_month,+1)  )
        self.box1.add_widget(self.minusbutton)
        self.box1.add_widget(self.plusbutton)
        self.monthbutton = MyButton( size_hint = (1,0.72), color = (0,1,0,0.5),bold = True, text = str(self.month))
        self.monthbutton.font_size = self.monthbutton.height * 0.7
        self.monthbutton.color = (0,0,0,0.5)
        self.leftbox.add_widget(self.box1)
        self.leftbox.add_widget(self.monthbutton)

    def create_weekdays(self):
        for col,weekday in enumerate('SUN MON TUS WED THU FRI SAT'.split()):
            button = Button(text=weekday)
            button.font_size = 12
            button.background_color = 0.6,0.6,0.6,1
            button.background_normal=''
            if weekday == 'SUN':   button.color = 1,0,0,1
            elif weekday == 'SAT': button.color = 0,0,1,1
            else:                  button.color = 0,0,0,1
            self.rightgrid.add_widget(button)

    def create_dates(self):
        for row in range(1,6+1):
            for col in range(7):
                button = MyButton()
                button.background_color = 0,0,0,1
                button.bind(on_press = self.on_click)
                id = f'rc{row}{col}'
                self.ids[id] = button 
                self.rightgrid.add_widget(button)
        self.update_dates(self.year,self.month)

    def initialize(self):
        print(self.unsel, self.unsel.bg)
        for row in range(1,6+1):
            for col in range(7):
                id = f'rc{row}{col}'
                button = self.ids[id]
                button.text = ''
                button.bold = False
                button.background_color = self.unsel.bg
                button.color = 0,0,0,1

    def update_dates(self,year,month):
        self.initialize()
        row = 1
        for ayear,amonth,aday,aweekday in self.TextCalendar.itermonthdays4(year,month): 
            col = (aweekday+1) % 7
            id = f'rc{row}{col}'
            button = self.ids[id]
            button.text = str(aday)
            if amonth == month:
                if col == 0: button.color = 1,0,0,1 # SUNDAY
                if col == 6: button.color = 0,0,1,1 # SATERDAY
                if (ayear, amonth, aday) == (self.now.year, self.now.month, self.now.day):
                    button.bold = True
                    button.color = self.today.fg
                    button.background_color = self.sel.bg
            else:  # not this month
                button.color = 0,0,0,0.3
            if col == 6: row += 1
            #print(id,button.text)

    def on_click(self,btn):
        for id in self.ids:
            if self.ids[id] == btn:
                btn.background_color = self.sel.bg
            else:
                self.ids[id].background_color = self.unsel.bg
        self.update_date(btn.text)
    def update_date(self,text):
        self.date = self.year, self.month, int(text)
        #print(self.date)
        #self.root.on_click(self.date)


    def on_change_month(self,nextmonth,btn):
        print('==>',nextmonth)
        self.month = int(self.monthbutton.text)
        if nextmonth == -1: self.month += -1
        if nextmonth == +1: self.month += +1
        if self.month == 13: 
            self.year += 1
            self.month = self.month % 12
        if self.month == 0:
            self.year += -1
            self.month = 12
        self.monthbutton.text = str(self.month)
        self.update_dates(self.year, self.month)

if __name__ ==  '__main__':
    class TestApp(MDApp):
        def build(self):
            return MyCalendar()
    TestApp().run()
