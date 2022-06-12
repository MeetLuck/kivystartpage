from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.base import EventLoop
from kivy.uix.textinput import TextInput


Config.set('input', 'mouse', 'mouse,disable_multitouch')



class RightClickTextInput(TextInput):   

    def on_touch_down(self, touch):

        super(RightClickTextInput,self).on_touch_down(touch)

        if touch.button == 'right':
            print("right mouse clicked")
            pos = super(RightClickTextInput,self).to_local(*self._long_touch_pos, relative=True)

            self._show_cut_copy_paste(
                pos, EventLoop.window, mode='paste')


kv_string = Builder.load_string("""
RightClickTextInput:
    use_bubble: True
    text: ('Palimm'*10+"\\n")*40
    multiline: True
    #readonly: True
""")

class MyApp(App):
    def build(self):
        return kv_string

if __name__ == '__main__':
    MyApp().run()
