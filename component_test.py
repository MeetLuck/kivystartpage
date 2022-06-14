from import_components import *

class Button1(MDFlatButton):
    def __init__(self,font_size=14,theme_text_color='Custom',line_color=(0,0,0,0),text_color=base.fg,**kwargs):
        super().__init__(font_size=font_size,theme_text_color='Custom',line_color=(0,0,0,0),text_color=text_color,**kwargs)
        self.background_normal = ''
        self.font_name = 'NotoSerifKR'


class Root(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.md_bg_color = 0,0,0.2,1
        self.add_widget( Button1(font_size=30, text='Button1'))
        self.add_widget( Button1(font_size=10, text='Button2', line_color = (1,0,0,1)))

class Test(MDApp):
    def build(self):
        return Root()

Test().run()
    
