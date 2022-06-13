from import_components import *

class moveB(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.font_name = 'NotoSerifKR'
        self.bold = True
        self.color = base.fg
        self.background_normal = ''
        self.background_color = 0,1,0,0 #self.background_color = Color.files.bg
        self.font_size = 14

class patrolG(MDGridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 4
        self.background_normal=''
        self.md_bg_color = 0,0,0,0


class MoveInOutBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.padding = 2
        self.spacing = 1
        self.create_layout()
        self.update()


    def create_layout(self):
        # create move-in,out button
        self.add_widget( moveB(text='전출입 및 승강기 현황'))
        # create interior button
        self.add_widget( moveB(text='세대공사'))
        # create dong-information button
        self.add_widget( moveB(text='동별세대수 및 공동현관문'))
        # create protection button 
        self.add_widget( moveB(text='보양재 현황'))
        # create interfloor noise button
        self.add_widget( moveB(text='층간소음'))


    def update(self):
        ...

if __name__ == '__main__':
    Window.size = 200,150
    class Test(MDApp):
        def build(self):
            return MyPatrolBox()
    Test().run()
