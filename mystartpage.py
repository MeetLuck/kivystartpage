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
        self.app = MDApp.get_running_app()
        self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self._keyboard.bind( on_key_down = self.key_down)


    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down = self.key_down)
        self._keyboard = None

    def key_down(self,keyboard, keycode, text, modifiers):
        print( str(keycode) )
        #self.app.label.text = str(keycode)

    def update_date(self,date:tuple):
        print(date,type(date))
        self.offworkers.update(date)
        self.myfiles.update(date)

    def on_long_touch(self, *args):
        print("<on_long_touch> event", args)

    def update(self,*args):
        #print('update ...',args)
        self.ids['id_time'].text = datetime.now().strftime('%m/%d %H:%M:%S')
        #self.ids['id_mypatrol'].update()


class Mystartpage(MDApp):

    def build(self):
        Window.clearcolor = 0,16/255,38/255,1
        self.root = MyStartBox()
    def on_start(self):
        print('=============>>>>>>>on_start')
        Clock.schedule_interval(self.root.update, 1) # seconds

Mystartpage().run()
