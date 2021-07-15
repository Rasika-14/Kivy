from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        btn = Button(text='Open', size_hint=(.2,.2) , pos=(250,250))
        return btn

if __name__ == '__main__':
    ButtonApp().run()