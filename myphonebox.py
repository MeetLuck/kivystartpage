from import_components import *

class PhoneField(TextInput):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.multiline = False
        self.hint_text = "enter 50 ~ 65"
        self.helper_text = "search TEL number"
        self.helper_text_mode = "on_focus"
        self.pos_hint = {'center_x':0.5,"center_y": 0.5}
        self.spacing = 0
        self.font_size = 30
        self.bold = True


class PhoneBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.spacing = 0
        self.create_grid('50','이재진','60','김덕근')
        self.create_grid('51','박종우','61','장희은')
        self.create_grid('52','이종화','62','문완수')
        self.create_grid('53','',      '63','정찬선')
        self.create_grid('54','이대진','64','최서우')
        self.create_grid('55','박은호','65','허 명 ')
        self.create_grid('56','김인호','66','이한우')
        self.create_grid('57','김광영','67','이시철')
        self.create_grid('58','정경호','59','원형준')
        #phonenumbers = AsyncImage(source='images/phonenumbers.png')
        #phonenumbers.size = phonenumbers.texture_size 
        #self.add_widget(phonenumbers)
    def create_grid(self,tel1,name1,tel2,name2):
        grid = MDGridLayout(cols=4,line_color=get_color(base.fg,0.5) )
        grid.add_widget( B1(text=tel1) )
        grid.add_widget( L1(text=name1,font_size=12,text_color=get_color(base.fg,0.8)))
        grid.add_widget( B1(text=tel2) )
        grid.add_widget( L1(text=name2,font_size=12,text_color=get_color(base.fg,0.8)))
        self.add_widget(grid)



if __name__ == '__main__':

    class Test(MDApp):
        def build(self):
            return PhoneBox()
    Test().run()
