from import_components import *


class PostGrid(MDGridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 10
        self.rows = 9
        self.padding = 2
        self.spacing = 1
        self.create_layout()
        self.update()

    def create_layout(self):
        post1 = '1초소 101 102 103 104 105 106 107'
        post1 = '1초소 101 102 103 104 105 106 107'
        post1 = post1.split() + [''] * 2
        print( post1 )
        for dong in post1:
            if dong in map(str,[102,104,106]):
                color = get_color(base.fg, 0.6)
                bold = False
            elif '초소' in dong:
                color = Color.cmds.fg
                bold = True
            else:
                color = base.fg
                bold = True
            button = B1(text=dong,text_color=color)
            button.bold = bold
            self.add_widget(button)


    def update(self):
        ...

if __name__ == '__main__':
    Window.size = 200,150
    class Test(MDApp):
        def build(self):
            return PostGrid()
    Test().run()
