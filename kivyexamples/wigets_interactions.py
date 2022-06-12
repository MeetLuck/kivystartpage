from import_components import *



class MybuttonBox(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        button1 = Button(text='change label1 of other widget')
        button2 = Button(text='change label2 of other widget')
        self.ids['button1'] = button1
        self.ids['button2'] = button2
        self.add_widget(button1)
        self.add_widget(button2)
        button1.bind(on_press  = button1.parent.on_press)
        button2.bind(on_press  = button2.parent.on_press)
        #print(button1.root)
    def on_press(self,btn):
        print(f'========>{self.ids}==============')
        for child in self.children:
            print(child,dir(child))
        print(btn.parent)
        print(btn.parent.parent)
        print('app.root ===>',App.get_running_app().root)
        self.root = App.get_running_app().root
        print(self.root.mylabel1box.label1a.text)
        

class Mylabel1Box(BoxLayout):
    label1a = ObjectProperty()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.label1a = Label(text='Label1a in Mylabel1Box',color=(0,1,0,1),font_size=30)
        self.label1b = Label(text='Label1b in Mylabel1Box',color=(0,1,0,1),font_size=30)
        self.add_widget(self.label1a)
        self.add_widget(self.label1b)

class Mylabel2Box(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.label2a = Label(text='Label2a in Mylabel2Box',color=(0,1,0,1),font_size=30)
        self.label2b = Label(text='Label2b in Mylabel2Box',color=(0,1,0,1),font_size=30)
        self.add_widget(self.label2a)
        self.add_widget(self.label2b)

class MyRoot(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget( MybuttonBox() )
        self.mylabel1box = Mylabel1Box()
        self.add_widget( self.mylabel1box )
        self.add_widget( Mylabel2Box() )



class Test(App):
    def build(self):
        return MyRoot()
    def on_start(self):
        print('====>',self.root)


Test().run()
