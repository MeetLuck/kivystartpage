from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
MDScreen:
    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                MDToolbar:
                    title: "Navigation Drawer"
                    elevation: 10
                    pos_hint: {"top": 1}
                    md_bg_color: get_color_from_hex("#e7e4c0")
                    specific_text_color: get_color_from_hex("#4a4939")
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]
        MDNavigationDrawer:
            id: nav_drawer
            md_bg_color: get_color_from_hex("#f7f4e7")
            ContentNavigationDrawer:
                Label:
                    text:"aaa"
                Label:
                    text:"aaa"
'''
class ContentNavigationDrawer(MDBoxLayout):
    pass
class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)
TestNavigationDrawer().run()
