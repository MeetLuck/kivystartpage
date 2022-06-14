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
import time

Window.size = 1200,900
Window.top = 80
Window.left = 350
#Window.borderless = True
Config.set('graphics','resizable', True)

class MyStartBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.status = self.ids['id_status']
        self.patrol = self.ids['id_mypatrol']
        self.update()
        self.app = MDApp.get_running_app()
        self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self._keyboard.bind( on_key_down = self.key_down)
        self._keyboard.bind( on_key_up = self.key_up)

    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down = self.key_down)
        self._keyboard = None

    def key_up(self,keyboard, keycode):
        time.sleep(0.1)
        if keycode[1] == str(1): os.startfile(minwonfile)
        if keycode[1] == str(2): os.startfile(self.dailyreportfile)
        if keycode[1] == str(3): os.startfile(self.commutefile)
        if keycode[1] == str(4): os.system( 'python {}'.format(minwonpyfile) )
        if keycode[1] == str(5): os.startfile(hpscanfile)
        if keycode[1] == str(6): os.startfile(workfolder)                                      
        if keycode[1] == str(7): os.startfile(commutefolder)
        if keycode[1] == str(8): os.startfile(weeklyworkfolder)
        if keycode[1] == str(9): os.system('explorer.exe /n,{}'.format(infofolder) )

    def key_down(self,keyboard, keycode, text, modifiers):
        # (49, '1')
        if keycode[1] == str(1): self.status.text = f'opening {minwonfile}'
        if keycode[1] == str(2): self.status.text = f'opening {self.dailyreportfile}'
        if keycode[1] == str(3): self.status.text = f'opening {self.commutefile}'
        if keycode[1] == str(4): self.status.text = f'python {minwonpyfile}'
        if keycode[1] == str(5): self.status.text = f'opening {hpscanfile}'
        if keycode[1] == str(6): self.status.text = f'opening {workfolder}'
        if keycode[1] == str(7): self.status.text = f'opening {commutefolder}'
        if keycode[1] == str(8): self.status.text = f'opening {weeklyworkfolder}'
        if keycode[1] == str(9): self.status.text = f'opening {infofolder}'

    def update_date(self,date:tuple):
        self.date = datetime(*date )
        self.status.text = self.date.strftime('%m/%d') + ' clicked ...'
        self.offworkers.update(date)
        self.myfiles.update(date)
        self.commutefile = get_monthlycommutefile(self.date)
        self.dailyreportfile = get_dailyreportfile(self.date)[0]

    def update_time(self,*args):
        print('==========> update by time',args)
        self.patrol.update()
        self.status.text = datetime.now().strftime('%m/%d %H:%M:%S')

    def update(self):
        self.update_date(self.mycalendar.date)
        self.update_time()


class Mystartpage(MDApp):

    def build(self):
        Window.clearcolor = 0,16/255,38/255,1
        self.root = MyStartBox()
    def on_start(self):
        print('=============>>>>>>>on_start')
        Clock.schedule_interval(self.root.update_time, 30) # seconds

Mystartpage().run()
