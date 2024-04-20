from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

Window.size = (300, 100)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "Приложение"

class MyApp(App):

    def build(self):
        box = BoxLayout()
        btn = Button(text = "Кнопка")
        label = Label(text='Прога пашет')
        box.add_widget(label)
        box.add_widget(btn)

        return box

if __name__ == '__main__':
    MyApp().run()
