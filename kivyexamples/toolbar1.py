from kivy.lang import Builder
from kivymd.app import MDApp


class Main(MDApp):
    def build(elf):
        return Builder.load_file('toolbar1.kv')


Main().run()
