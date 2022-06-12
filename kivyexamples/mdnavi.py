from kivy.app import App
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.lang import Builder

kv = '''
MDNavigationLayout:
    MDNavigationDrawer:
        Button:
            text: "Screen 1"
            on_release:
                screen_manager.current = "screen1"
        Button:
            text: "Screen 2"
            on_release:
                screen_manager.current = "screen2"
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Your app"
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['menu', lambda x: root.toggle_nav_drawer()]]
        ScreenManager:
            id: screen_manager
            Screen:
                name: "screen1"
                MDLabel:
                    text: "Screen 1"
            Screen:
                name: "screen2"
                MDLabel:
                    text: "Screen 2"
'''


class MainApp(MDApp):
    theme_cls = ThemeManager()
    def build(self):
        return Builder.load_string(kv)


MainApp().run()

