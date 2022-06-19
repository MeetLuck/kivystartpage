from import_components import *

class PhoneField(TextInput):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.multiline = False
        self.hint_text = "enter 50 ~ 65"
        self.helper_text = "search TEL number"
        self.helper_text_mode = "on_focus"
        self.pos_hint = {'center_x':0.5,"center_y": 0.5}
        self.spacing = 0
        self.font_size = 30
        self.bold = True

class PhoneBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        self.spacing = 0
        #self.root = MDApp.get_running_app().root
        self.phonenumber = {50:'김규동: 010-8127-0040',51:'박종우:010-4746-8663'}
        self.create_layout()

    def create_layout(self):
        self.phoneinput = PhoneField()
        self.phoneinput.bind(text=self.on_text)
        self.add_widget(self.phoneinput)
        print(self.phoneinput)

    def on_text(self,textinput, value):
        if len(value) == 0:
            print(self.phonenumber)
        elif len(value) == 1:
            if value.startswith('5'):
                print(self.phonenumber)
            else:
                print('unknown phonenumber')
        elif len(value) == 2:
            if value.startswith('5'):
                print(self.phonenumber[int(value)])
        else:
            print('unknown number')


if __name__ == '__main__':

    class Test(MDApp):
        def build(self):
            return PhoneBox()
    Test().run()
