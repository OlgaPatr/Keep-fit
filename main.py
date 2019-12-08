from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.config import Config
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.app import App

Config.set("graphics", "width", 390) 
Config.set("graphics", "heigth", 600)
Config.set("graphics", "resizable", 0)

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class Time(Widget):
    time = NumericProperty(30)

class Num(Widget):
    num = NumericProperty(1)

class WindowManager(ScreenManager):

    time = Time()
    num = Num()
    
    def update(self, dt):
        self.time.time -= 1
        if (self.time.time == 0):
            self.num.num += 1
            self.event.cancel()
            self.count_down()
            
    def count_down(self):
        self.time.time = 30
        self.event = Clock.schedule_interval(self.update, 1.0)
    
    def stop(self):
        self.num.num = 1
        self.event.cancel()

with open("design.kv", encoding='utf8') as design:
    Builder.load_string(design.read())
  
class MyApp(App):
    def build(self):
        self.title = "Keep Fit"
        return WindowManager()


if __name__ == '__main__':
    MyApp().run()
