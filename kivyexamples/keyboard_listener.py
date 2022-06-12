# complex example

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label

Builder.load_string('''
#:set rng range(4)
#:import R random.random
#:import dp kivy.metrics.dp
<MyLabel>:
    font_size: dp(100)
    on_text:
        self.color = [R() for i in rng]
''')


class MyLabel(Label):
    def __init__(self, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.app.label = self


class Listener(Widget):
    def __init__(self, **kwargs):
        super(Listener, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.app.label.text = str(keycode)


class My(App):
    def build(self):
        self.listener = Listener()
        return MyLabel()


if __name__ == '__main__':
    My().run()
