from import_components import *

class MyPostBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.padding = 2
        self.spacing = 1
        #self.root = MDApp.get_running_app().root
