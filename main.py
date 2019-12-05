from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.lang import Builder


Config.set("graphics", "width", 390) 
Config.set("graphics", "heigth", 600)
Config.set("graphics", "resizable", 0)

Builder.load_string('''
<ScreenOne>:
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
                root.manager.current = "go"
<ScreenTwo>
    FloatLayout:
        orientation: 'vertical'
        Button:
            text: "ПОБЕДА"
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
                root.manager.current = "start"
''')
class ScreenOne(Screen):
    pass
class ScreenTwo(Screen):
    pass
screen_manager = ScreenManager()
screen_manager.add_widget(ScreenOne(name="start"))
screen_manager.add_widget(ScreenTwo(name="go"))
class MyApp(App):
    def build(self):
        self.title = "Keep Fit"
        return screen_manager
    

if __name__ == '__main__':
    MyApp().run()
