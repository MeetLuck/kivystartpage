from import_components import *

class MoveButton(IB1):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.font_name = 'NotoSerifKR'
        self.bold = True
        #self.color = Color.files.fg
        #self.background_color = Color.files.bg
        #self.text_color = Color.cmds.fg
        self.icon_color = base.fg
        #self.font_size = 16

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
        self.padding = 0
        self.spacing = 1
        self.create_layout()
        self.update()


    def create_layout(self):
        # create move-in,out button
        self.movin      = MoveButton(text='전출입 및 승강기 현황',    icon='truck-outline',on_press=self.on_press)
        self.interior   = MoveButton(text='세대공사',                 icon='tools',on_press=self.on_press)
        self.donginfo   = MoveButton(text='동별 세대수 및 공동현관문',icon='home-city',on_press=self.on_press)
        self.protectev  = MoveButton(text='보양재 현황',              icon='elevator-passenger-outline',on_press=self.on_press)
        self.internoise = MoveButton(text='층간소음',                 icon='bullhorn-outline',on_press=self.on_press)
        self.add_widget(self.movin)
        self.add_widget(self.interior)
        self.add_widget(self.donginfo)
        self.add_widget(self.internoise)

    def on_press(self,*args):
        ...
    def update(self):
        ...

if __name__ == '__main__':
    Window.size = 200,150
    class Test(MDApp):
        def build(self):
            return MyPatrolBox()
    Test().run()
