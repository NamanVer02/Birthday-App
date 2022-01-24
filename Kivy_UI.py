import imp
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('Kivy_Design.kv')
Window.size = (350, 600)

class TheLayout(Widget):
        pass

class TheApp(App):
    def build(self):
        return TheLayout()

if __name__ == '__main__':
    TheApp().run()
