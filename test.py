from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Container(BoxLayout):
    pass

class MyFirstApp(App):
    def build(self):
        BoxL = BoxLayout()
        return Container()
    

if __name__ == '__main__':
    MyFirstApp().run()