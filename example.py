from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Container(BoxLayout):
    pass

class MyFirstApp(App):
    def build(self):
        BoxL = BoxLayout()
        b1= Button(text = 'lol')
        b2= Button(text = 'kek')
        BoxL.add_widget(b1)
        BoxL.add_widget(b2)
        return Container()
    

if __name__ == '__main__':
    MyFirstApp().run()