from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

class WidgetsExample(GridLayout):
    count: int = 1
    my_text = StringProperty("1")
    def on_button_click(self):
        print("Button Clicked")
        self.count += 1
        self.my_text = str(self.count)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()