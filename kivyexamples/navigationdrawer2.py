from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import NavigationLayout  # Do not remove

root_kv = """
<ContentNavigationDrawer@MDNavigationDrawer>:
    drawer_logo: "drawer_logo.png"

    NavigationDrawerSubheader:
        text: "Menu:"

    NavigationDrawerIconButton:
        icon: "access-point"
        text: "First"

    NavigationDrawerIconButton:
        icon: "account"
        text: "Second"


NavigationLayout:
    id: nav_layout

    ContentNavigationDrawer:
        id: nav_drawer

    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            id: toolbar
            title: "Toolbar title"
            md_bg_color: app.theme_cls.primary_color
            background_palette: "Primary"
            background_hue: "500"
            elevation: 10
            left_action_items:
                [["menu", lambda x: app.root.toggle_nav_drawer()]]

        BoxLayout:
            orientation: "vertical"
            padding: dp(16)

            MDRaisedButton:
                text: "Click me!"

            Widget:
"""


class MainApp(MDApp):

    def build(self):
        self.root = Builder.load_string(root_kv)


if __name__ == "__main__":
    MainApp().run()
