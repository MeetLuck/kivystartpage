# https://blog.kivy.org/2019/06/widget-interactions-between-python-and-kv/
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder

kv = '''
<RootWidget>:
    orientation: 'vertical'
    topright_label: id_topright
    BoxLayout:
        Label:
            text:'top left'
        Label:
            id: id_topright
            text:'top right'
    Button:
        text: 'print top right label'
        on_press: root.on_press(self)
'''

Builder.load_string(kv)

class RootWidget(BoxLayout):
    #topright_label = ObjectProperty()

    def on_press(self,btn):
        print(f'top right label is {self.topright_label.text}')

class Test(App):
    def build(self):
        return RootWidget()

Test().run()
