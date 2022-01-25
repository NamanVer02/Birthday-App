import pickle
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('AddBirthdays.kv')
Window.size = (350, 600)


try:
    data = pickle.load(open('data.dat', 'rb'))
except FileNotFoundError:
    data = []


class TheLayout(Widget):
    pass


class TheApp(App):
    def build(self):
        return TheLayout()

    
    def Add(self):
        first_name = self.root.ids.first_name.text
        last_name = self.root.ids.last_name.text
        nickname = self.root.ids.nickname.text
        phone = self.root.ids.phone.text
        birthday = self.root.ids.birthday.text

        data.append([first_name+last_name, nickname, phone, birthday])
        print(data)
        pickle.dump(data, open('data.dat', 'wb'))



if __name__ == '__main__':
    TheApp().run()
