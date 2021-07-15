from kivy.app import App
from kivy.uix.label import Label

class HelloKivy(App):
    def build(self):
        lb1 = Label(text='Hello Kivy')
        return lb1
if __name__ == '__main__':
    HelloKivy().run()


