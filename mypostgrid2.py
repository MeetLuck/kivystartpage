from import_components import *
from dong_data import *

class PostButton(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.font_name = 'NotoSerifKR'
        self.bold = True
        self.color = base.fg #get_color(base.fg,0.6) #fg = 110/255,130/255,150/255,1
        self.background_normal = ''
        self.background_color = 0,1,0,0 #self.background_color = Color.files.bg
        #self.md_bg_color = base.bg
        self.font_size = 14

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
        self.cols = 15
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
        headings = '세대  층  EV1  보양재  초소  1F   B1a   B1b   B2a   B2b  B1c   B1d   B2c   B2d  9010'.split()
        for text in headings:
            self.add_widget( PopLabel(text=text) )
        dong_index = find_dong(dong)
        dong_list = dong_sedae_floor_post_ev[dong_index]
        #print(btn.text , dong_index)
        print('===>', dong_list, len(dong_list) )
        for text in dong_list[1:]:
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
        self.create_layout()
        self.update()

    def create_row(self,patrol):
        self.grid = Grid1x10() 
        for text in patrol:
            self.grid.add_widget( PostButton( text= text,on_press = self.on_press ) )
        self.add_widget(self.grid)

    def on_press(self,btn):
        # create content and add to the popup
        self.dialog = MDDialog( title='',size_hint=(None, None), width = 1200, md_bg_color = base.bg ,type="custom", content_cls=Content(btn), buttons=[ ])
        self.dialog.font_name = 'NotoSerifKR'
        self.dialog.open()
        print(btn.text)

    def create_layout(self):
        self.create_row('1초소  101 102 103 104 105 106 107 108 109'.split())
        self.create_row('2초소  102 103 104 105 106 111 112 113 114'.split())
        self.create_row('3초소  105 106 107 108 109 110 111 112 113'.split())
        self.create_row('5초소  115 116 117 118 119 120 121 121 122'.split())
        self.create_row('6초소  116 117 118 119 120 121 123 124 125'.split())
        self.create_row('7초소  122 123 124 125 126 127 130 131 132'.split())
        self.create_row('8초소  127 128 129 130 131 132 133 134 135'.split())
        self.create_row('9초소  134 135 136 137 140 141 142 143 144'.split())
        self.create_row('10초소 136 137 138 139 140 141 142 143 144'.split())

    def reset_grid(self,grid):
        grid.md_bg_color = 0,51/255,255/255,1
        for button in grid.children:
            button.color = base.fg

    def update(self):
        for idx,grid in enumerate(reversed(self.children)):
            print(idx,grid.children[0].text)
            if idx >= 3:  
                post = idx + 2
            else:
                post = idx + 1
            dongs = get_dongsforpost(post)
            print(post,dongs)
            for button in reversed(grid.children):
                if '초소' in button.text:
                    button.color = base.fg
                    continue
                if button.text not in map(str,dongs):
                    button.color = get_color(base.fg,0.5)
                    print(button.text)
                else:
                    button.color = base.fg

if __name__ == '__main__':
    Window.size = 400,150
    class Test(MDApp):
        def build(self):
            return MyPostGrid()
    Test().run()
