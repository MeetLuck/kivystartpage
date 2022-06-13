from import_components import *

from mycal.mycalendar import MyCalendar
from myoffworkers import *
from myfilesbox import *
from mycmdsbox  import *
from myfoldersbox import *
from myservicesbox import *
from mynotification import *
from mypostbox import *
from mypatrolbox import *
from mymoveinout import *

Window.size = 1200,900
Window.top = 80
Window.left = 350
#Window.borderless = True
Config.set('graphics','resizable', True)

class MyStartBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.update_date(self.mycalendar.date)

    def update_date(self,date:tuple):
        print(date,type(date))
        self.offworkers.update(date)
        self.myfiles.update(date)

    def on_long_touch(self, *args):
        print("<on_long_touch> event", args)

    def update(self):
        self.ids['id_mypatrol'].update()



class Mystartpage(MDApp):

    def build(self):
        Window.clearcolor = 0,16/255,38/255,1
        self.root = MyStartBox()

Mystartpage().run()
