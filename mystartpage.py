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
from mystatusbox import *
from applicationbox import *
from mypostgrid import *
import time

Window.size = 1250,900
Window.top = 80
Window.left = 350
#Window.borderless = True

class MyStartBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #md_bg_color: 0,16/255,38/255,1
        self.md_bg_color = base.bg
        self.status = self.ids['id_statusbox']
        self.mainstatus = self.status.statuslabel
        self.selectstatus =self.status.selectlabel
        self.timestatus =self.status.timelabel
        self.patrol = self.ids['id_mypatrol']
        self.update()
        self.app = MDApp.get_running_app()
        self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self._keyboard.bind( on_key_down = self.key_down)
        self._keyboard.bind( on_key_up = self.key_up)

    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down = self.key_down)
        self._keyboard.unbind(on_key_up = self.key_up)
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
        if keycode[1] == 'f':    os.startfile('firefox')
        if keycode[1] == 'p':    os.startfile('mspaint')
        if keycode[1] == 's':    os.startfile('snippingtool')

    def key_down(self,keyboard, keycode, text, modifiers):
        # (49, '1')
        if keycode[1] == str(1): self.mainstatus.text = f'loading {minwonfile}'
        if keycode[1] == str(2): self.mainstatus.text = f'loading {self.dailyreportfile}'
        if keycode[1] == str(3): self.mainstatus.text = f'loading {self.commutefile}'
        if keycode[1] == str(4): self.mainstatus.text = f'python {minwonpyfile}'
        if keycode[1] == str(5): self.mainstatus.text = f'loading {hpscanfile}'
        if keycode[1] == str(6): self.mainstatus.text = f'loading {workfolder}'
        if keycode[1] == str(7): self.mainstatus.text = f'loading {commutefolder}'
        if keycode[1] == str(8): self.mainstatus.text = f'loading {weeklyworkfolder}'
        if keycode[1] == str(9): self.mainstatus.text = f'loading {infofolder}'
        if keycode[1] == 'f':    self.mainstatus.text = f'loading firefox'
        if keycode[1] == 'p':    self.mainstatus.text = f'loading paint'
        if keycode[1] == 's':    self.mainstatus.text = f'loading snippingtool'

    def update_date(self,date:tuple):
        self.date = datetime(*date )
        self.selectstatus.text = self.date.strftime('%m/%d')
        self.offworkers.update(date)
        self.myfiles.update(date)
        self.commutefile = get_monthlycommutefile(self.date)
        #print(self.date, type(self.date))
        self.dailyreportfile = get_dailyreportfile(self.date)[0]

    def update_time(self,*args):
        self.patrol.update()
        self.timestatus.text = datetime.now().strftime('%H:%M:%S')

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
