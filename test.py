from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image



class Container(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.img1 = Image(source = 'images/card1.jpg')
        self.btn = Button(text = 'bimbim')




class MyFirstApp(MDApp):
    def build(self):
    #     self.img1 = Image(source = 'images/card1.jpg')
    #     self.img1.add_widget(HoverItem())
    #     return self.img1
        self.btn = Button(text = 'bimbim', size_hint = (0.5, 0.5))
        self.btn.add_widget(HoverItem())
        return self.btn

class HoverItem(MyFirstApp, HoverBehavior):

    def on_enter(self, *args):
        self.btn.size_hint = (1.0, 1.0)
        print('in')

    def on_leave(self, *args):
        self.btn.size = (2000,200)
        print('out')

if __name__ == '__main__':
    MyFirstApp().run()

