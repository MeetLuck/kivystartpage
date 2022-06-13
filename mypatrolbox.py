from import_components import *

class patrolB(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.font_name = 'NotoSerifKR'
        self.bold = True
        self.color = get_color(base.fg,0.6) #fg = 110/255,130/255,150/255,1
        self.background_normal = ''
        self.background_color = 0,1,0,0 #self.background_color = Color.files.bg
        self.font_size = 20

class patrolG(MDGridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 4
        self.background_normal=''
        self.md_bg_color = 0,0,0,0


class MyPatrolBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.padding = 2
        self.spacing = 1
        self.create_layout()
        self.update()

    def create_row(self,patrol):
        self.grid = patrolG() 
        for text in patrol:
            self.grid.add_widget( patrolB( text= text ) )
        self.add_widget(self.grid)

    def create_layout(self):
        daynight = get_dayornight(datetime.now())
        #dayornight=['day1','day2','night1','night2','off1','off2']
        if daynight in ['day1','day2']:
            self.create_row('09 2 6 9'.split())
            self.create_row('10 1 5 8'.split())
            self.create_row('11 3 7 10'.split())
            self.create_row('13 2 6 9'.split())
            self.create_row('14 1 5 8'.split())
            self.create_row('15 3 7 10'.split())
        elif daynight in ['night1','night2']:
            self.create_row('23 2 6 9'.split())
            self.create_row('24 1 5 8'.split())
            self.create_row('01 3 7 10'.split())
            self.create_row('02 2 6 9'.split())
            self.create_row('03 1 5 8'.split())
            self.create_row('04 3 7 10'.split())

    def reset_grid(self,grid):
        grid.md_bg_color = 0,51/255,255/255,1
        for button in grid.children:
            button.color = base.fg

    def update(self):
        hour = datetime.now().hour
        for grid in reversed(self.children):
            patrol_time = int( list(reversed(grid.children))[0].text )
            if hour in [7,8,9] and patrol_time == 9:
                self.reset_grid(grid)
            elif hour in [12,13] and patrol_time == 13:
                self.reset_grid(grid)
            elif patrol_time == hour:
                self.reset_grid(grid)
            else:
                for button in grid.children:
                    button.color = get_color(base.fg, 0.6)
                print('not in patrol time',hour)
                grid.md_bg_color = 0,0,0,0

if __name__ == '__main__':
    Window.size = 200,150
    class Test(MDApp):
        def build(self):
            return MyPatrolBox()
    Test().run()
