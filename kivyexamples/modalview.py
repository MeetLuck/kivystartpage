
#ModalView widget is used to create modal views. By default, the view will cover the whole “main” window.

#Remember that the default size of a Widget is size_hint=(1, 1).
#If you don’t want your view to be fullscreen, either use size hints with values lower than 1 (for instance size_hint=(.8, .8))
#or deactivate the size_hint and use fixed size attributes.


#By default, any click outside the view will dismiss it. If you don’t want that, you can set ModalView.auto_dismiss to False:
'''
view = ModalView(size_hint=(None, None), size=(400, 400), auto_dismiss=False)
content = Button(text='Close me!')
view.add_widget(content)
view.open()
content.bind(on_press=view.dismiss)
'''
# bind the on_press event of the button to the dismiss function
#To manually dismiss/close the view, use the ModalView.dismiss() method of the ModalView instance:
#view.dismiss()
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
 
 
kv = """
<Main>:
    Button:
        text: "Open Dialog"
        on_press: root.show_popup()
 
"""
 
Builder.load_string(kv)
 
class Main(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = 1,0,0.15,1
    def show_popup(self):
        P = ModalView(size_hint=(0.4, 0.6), background='',background_color=(0,0,1,0),auto_dismiss=False)
        container = MDBoxLayout(orientation='vertical', padding=(24))
        container.md_bg_color = 0,1,0,1
         
        for i in range(10):
            container.add_widget(Button(text=str(i)))
        P.add_widget(container)
        P.open()
         
class MyApp(App):
    def build(self):
        return Main()
  
MyApp().run()
