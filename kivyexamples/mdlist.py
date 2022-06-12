from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
ScrollView:
    bg_color : 0,1,0,1

    MDList:

        OneLineListItem:
            text : '9'
            on_release: print("Click!")
        OneLineListItem:
            text : '10'
            on_release: print("Click!")
        OneLineListItem:
            text : '11'
            on_release: print("Click!")
        OneLineListItem:
            text : '13'
            on_release: print("Click!")
'''


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()
