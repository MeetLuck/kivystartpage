from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

class Example(App):
    def build(self):
        self.root = FloatLayout()
        self.label = Label(text="I'm aligned :)", size_hint=(1.0, 1.0), halign="left", valign="middle")
        self.label.bind(size=self.label.setter('text_size'))    
        self.root.add_widget(self.label)
        return self.root

Example().run()
