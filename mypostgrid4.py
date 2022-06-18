from import_components import *
from dong_data import *

class PostButton(Button,HoverBehavior):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.font_name = 'NotoSerifKR'
        self.bold = True
        self.color = base.fg #get_color(base.fg,0.6) #fg = 110/255,130/255,150/255,1
        self.background_normal = ''
        self.background_color = 0,1,0,0 #self.background_color = Color.files.bg
        #self.md_bg_color = base.bg
        self.font_size = 14

    def on_enter(self, *args):
        self.tmp = self.color 
        self.color = (1,1,1,1)

    def on_leave(self, *args):
        self.color = self.tmp

class MDPostButton(MDFlatButton,HoverBehavior): # XXX to large space
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.font_name = 'NotoSerifKR'
        self.bold = True
        self.text_color = base.fg #get_color(base.fg,0.6) #fg = 110/255,130/255,150/255,1
        #self.background_normal = ''
        #self.background_color = 0,1,0,0 #self.background_color = Color.files.bg
        #self.md_bg_color = base.bg
        self.theme_text_color='Custom'
        self.font_size = 12

    def on_enter(self, *args):
        self.tmp = self.text_color 
        self.text_color = (1,1,1,1)

    def on_leave(self, *args):
        self.text_color = self.tmp

class PopLabel(MDLabel):
    def __init__(self,text_color = base.fg, bold = False, font_size=base.font_size, **kwargs):
        super().__init__( text_color = text_color, bold = bold, font_size=font_size,**kwargs)
        self.font_name = base.font_name
        self.theme_text_color = "Custom"
        self.line_color = get_color(base.fg, 0.3)
        self.halign = 'center'
        #self.size = self.texture_size
        #   text_color: 0, 0, 1, 1
        #self.bind(size=self.setter('text_size'))    

class Content(MDGridLayout):
    def __init__(self,button,**kwargs):
        super().__init__(**kwargs)
        self.cols = 16
        self.rows = 2
        #self.size_hint_x = None
        self.size_hint_y = None
        #self.width = 200
        self.height = 100
        self.md_bg_color = base.bg
        #self.md_bg_color = 0,0,0,0
        dong = button.text
        self.create_layout(dong)

    def create_layout(self,dong):
        headings = '동 세대  층  EV1  보양재  초소  1F   B1a   B1b   B2a   B2b  B1c   B1d   B2c   B2d  9010'.split()
        for text in headings:
            self.add_widget( PopLabel(text=text) )
        dong_index = find_dong(dong)
        dong_list = dong_sedae_floor_post_ev[dong_index]
        #print(btn.text , dong_index)
        print('===>', dong_list, len(dong_list) )
        for text in dong_list[:]:
            self.add_widget( PopLabel(text=str(text)) )

class Grid1x10(MDGridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 10
        self.spacing = 0
        self.background_normal=''
        self.md_bg_color = 0,0,0,0

class MyPostGrid(MDGridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 9
        self.posts = [1,2,3,5,6,7,8,9,10]
        self.create_layout()
        self.modalview = ModalView(size_hint=(None,None),size=(1000,200), background='',background_color=(0,0,1,0),auto_dismiss=True)
        self.update()

    def create_row(self,patrol):
        self.grid = Grid1x10() 
        for text in patrol:
            self.grid.add_widget( PostButton( text= text,on_press = self.on_press ) )
        self.add_widget(self.grid)

    def on_press(self,btn):
        self.modalview.add_widget(Content(btn))
        self.modalview.open()
        print(btn.text)

    def create_layout(self):
        self.create_row('1  101 102 103 104 105 106 107 108 109'.split())
        self.create_row('2  102 103 104 105 106 111 112 113 114'.split())
        self.create_row('3  105 106 107 108 109 110 111 112 113'.split())
        self.create_row('5  115 116 117 118 119 120 121 122 123'.split())
        self.create_row('6  116 117 118 119 120 121 123 124 125'.split())
        self.create_row('7  122 123 124 125 126 127 130 131 132'.split())
        self.create_row('8  127 128 129 130 131 132 133 134 135'.split())
        self.create_row('9  134 135 136 137 140 141 142 143 144'.split())
        self.create_row('10 136 137 138 139 140 141 142 143 144'.split())

    def reset_grid(self,grid):
        grid.md_bg_color = 0,51/255,255/255,1
        for button in grid.children:
            button.color = base.fg

    def get_post(self,idx):
        # XXX 
        # idx           -> 0,1,2,3,4,5,6,7,8,9
        # skip post 4   -> 1,2,3,5,6,7,8,9,10 
        return self.posts[idx]

    def is_post(self,button):
        if int(button.text) in self.posts:
            return True
        else:
            return False

    def update(self):
        for idx,grid in enumerate(reversed(self.children)):
            #print(idx,grid.children[0].text)
            post = self.get_post(idx)
            dongs = get_dongsforpost(post)
            print('==>post,dongs',post,dongs)
            for button in reversed(grid.children):
                if self.is_post(button):
                    button.color = get_color(base.fg, 0.7)
                    continue
                if button.text in map(str,dongs):
                    button.color = base.fg
                else:
                    button.color = get_color(base.fg,0.5)

if __name__ == '__main__':
    Window.size = 1200,250
    class Test(MDApp):
        def build(self):
            return MyPostGrid()
    Test().run()
