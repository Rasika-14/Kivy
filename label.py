from kivy.app import App
from kivy.uix.label import Label

class HelloKivy(App):
    def build(self):
        lbl = Label(text='Hello Kivy')
        return lbl
if __name__ == '__main__':
    HelloKivy().run()

    
