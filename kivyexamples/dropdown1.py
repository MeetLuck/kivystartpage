from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App

Builder.load_string('''

<CustomDropDown>:
    Button:
        text: "My first item"
        size_hint_y: None
        height: 40
        on_press: root.select('My first item')
    Button:
        text: "My second item"
        size_hint_y: None
        height: 40
        on_press: root.select('My second item')
        ''')

class CustomDropDown(DropDown):
    ...

class Test(App):
    def build(self):
        btn = Button(text='Select Item',size_hint=(0.5,0.1),pos_hint={'center_x':0.5,'center_y':0.5})
        dropdown = CustomDropDown()
        dropdown.bind(on_select = lambda obj, text: setattr(btn,'text',text))
        btn.bind(on_press = dropdown.open)
        return btn

Test().run()
