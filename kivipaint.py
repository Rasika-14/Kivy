from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Ellipse,Line

class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(1,1,0)
            d = 30
            Ellipse(pos= )
            touch.ud['line'] = Line[touch.x, touch.y]

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()

   if __name__ == '__main__':
       MyPaintApp().run()
