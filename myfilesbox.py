from import_components import *

class MyFilesBox(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.create_layout()

    def create_layout(self):
        self.minwonbtn = Button(text='minwonfile')
        self.dailyreportbtn1 = Button(text='dailyreportfile1')
        self.dailyreportbtn2 = Button(text='dailyreportfile2')
        self.minwonbtn.bind(on_press=self.on_press)
        self.dailyreportbtn1.bind(on_press=self.on_press)
        self.dailyreportbtn2.bind(on_press=self.on_press)
        self.add_widget(self.minwonbtn)
        self.add_widget(self.dailyreportbtn1)
        self.add_widget(self.dailyreportbtn2)

    def on_press(self,btn):
        import os
        if btn == self.minwonbtn:
            print(btn.text)
        if btn == self.dailyreportbtn1:
            print(btn.text)
        if btn == self.dailyreportbtn2:
            print(btn.text)

    def update(self):
        pass
