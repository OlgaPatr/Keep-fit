from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock
from kivy.uix.widget import Widget


Config.set("graphics", "width", 390) 
Config.set("graphics", "heigth", 600)
Config.set("graphics", "resizable", 0)

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class Time(Widget):
    time = NumericProperty(30)


class WindowManager(ScreenManager):
    time = Time()
    def update(self, dt):
        self.time.time -= 1
        if (self.time.time == 0):
            self.stop()
    def count_down(self):
        self.time.time = 30
        self.event = Clock.schedule_interval(self.update, 1.0)
    def stop(self):
        self.event.cancel()

kv = Builder.load_string('''
<WindowManager>:
    ScreenOne:
        id: 1
    ScreenTwo:
        id: 2
<ScreenOne>:
    name : "1"
    FloatLayout:
        orientation: 'vertical'
        canvas:
            Rectangle:
                source: 'C:/Users/79263/Downloads/Старт (3).png'
                size: 390, 600
                pos: self.pos
        Button:
            text: "НАЧНЁМ"
            font_size : '30sp'
            color: 3, 3, 3, 1
            pos: 80, 285
            size_hint: .6, .1
            background_color : 0, 0, 0, 0
            background_normal : ''
            back_color: 1, 0, 1, 1
            border_radius : 18
            bold: True
            canvas.before:
                Color:
                    rgba: self.back_color
                Line:
                    rounded_rectangle: (self.pos[0], self.pos[1], self.size[0], self.size[1], self.border_radius)
                    width : 1.2
            on_release:
                root.manager.transition.direction = "down"
                root.manager.transition.duration = 0
                root.manager.current = "2"
                root.manager.count_down()
<ScreenTwo>
    name : "2"
    FloatLayout:
        orientation: 'vertical'
        Button:
            text: "Закончим"
            font_size : '30sp'
            color: 3, 3, 3, 1
            pos: 80, 10
            size_hint: .6, 0.08
            background_color : 0, 0, 0, 0
            background_normal : ''
            back_color: 1, 0, 1, 1
            border_radius : 18
            bold: True
            canvas.before:
                Color:
                    rgba: self.back_color
                Line:
                    rounded_rectangle: (self.pos[0], self.pos[1], self.size[0], self.size[1], self.border_radius)
                    width : 1.2
            on_release:
                root.manager.current = "1"
                root.manager.stop()
        Label:
            text: str(root.manager.time.time)
            pos : 175, 500
            size_hint : .1, .1
            font_size : '30sp'

''')

class MyApp(App):
    def build(self):
        self.title = "Keep Fit"
        return WindowManager()


if __name__ == '__main__':
    
    MyApp().run()
