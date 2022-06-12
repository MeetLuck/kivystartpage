from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "MDTopAppBar"
        left_action_items: [["menu", "This is the navigation"]]
        right_action_items: [ ["attachment", lambda x: x], ["calendar", lambda x: x], ["dots-vertical", lambda x: x], ]

    MDLabel:
        text: "Content"
        halign: "center"
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def callback(self, button):
        Snackbar(text="Hello World").open()

Test().run()
