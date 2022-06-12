from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.navigationdrawer import NavigationLayout
#from navigation_drawer import navigation_helper

Window.size = (300, 500)


navigation_helper='''
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Demo Application'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:5
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "mine.jpg"
                MDLabel:
                    text: "Attreya"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: "attreya01@gmail.com"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]
                ScrollView:
                    DrawerList:
                        id: md_list
                        
                        MDList:
                            OneLineIconListItem:
                                text: "Profile"
                            
                                IconLeftWidget:
                                    icon: "face-profile"
                                    
                           
                                    
                            OneLineIconListItem:
                                text: "Upload"
                            
                                IconLeftWidget:
                                    icon: "upload"
                                    
                           
                            OneLineIconListItem:
                                text: "Logout"
                            
                                IconLeftWidget:
                                    icon: "logout"
'''

class DemoApp(MDApp):
    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen

    def on_start(self):
        pass


DemoApp().run()
                           
