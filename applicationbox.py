from import_components import *

class AppButton(IB1):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.font_name = 'NotoSerifKR'
        self.bold = True
        self.color = base.fg
        #self.background_color = Color.files.bg
        #self.text_color = base.fg
        self.icon_color = base.fg
        #self.font_size = 16

class ApplicationBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.spacing = 0
        #self.root = MDApp.get_running_app().root
        self.create_layout()

    def create_layout(self):
        #print(minwonfile)
        self.firefox        =  AppButton(text='firefox',     icon='alpha-f-circle-outline',on_press=self.on_press)
        self.paint          =  AppButton(text='mspaint',     icon='alpha-p-circle-outline',     on_press=self.on_press)
        self.snippingtool   =  AppButton(text='snippingtool',icon='alpha-s-circle-outline',on_press=self.on_press)
        self.add_widget(self.firefox)
        self.add_widget(self.paint)
        self.add_widget(self.snippingtool)

    def on_press(self,btn):
        root = Path(__file__).parent
        if btn == self.firefox:         os.startfile('firefox')
        if btn == self.paint:           os.startfile('mspaint')
        if btn == self.snippingtool:    os.startfile('snippingtool')

if __name__ == '__main__':

    class Test(MDApp):
        def build(self):
            return ApplicationBox()
    Test().run()
