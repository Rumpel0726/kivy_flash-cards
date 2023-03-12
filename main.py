from kivy.config import Config
#Config.set('graphics', 'resizable', '0')
#Config.set('graphics', 'width', '640')
#Config.set('graphics', 'height', '480')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.widget import Widget

class AppCore(Widget):
    pass

class TestApp(App):
    def build(self):
        return AppCore()

def run_app():
    TestApp().run()

if __name__ == '__main__':
    run_app()

"""
class AppCore(Widget):
    pass

'''
class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        # Число колонок
        self.cols = 1
        self.col_default_width = 100
        self.row_default_height = 350
        # Добавим виджет
        self.add_widget(Label(text='Флеш-Карточки', font_size=30), size_hint_x=100, size_hint_y=100)
        self.add_widget(Button(size_hint_x=100, size_hint_y=100))
        self.add_widget(Button(background_color=(1, 0, 0, 1), size_hint_x=100, size_hint_y=100))
'''


class MyApp(App):
    def build(self):
        return AppCore()

    # def btn_press(self, instance):
    #     print("Кнопка нажата")
    #     instance.text = 'hi wrld'


def run_app():
    MyApp.run()


if __name__ == "__main__":
    run_app()

'''return Button(text="Старт",
                             font_size=30,
                             on_press=self.btn_press,
                             background_color=(.30, .69, .31, 1),
                             background_normal='',
                             size_hint=(.5, .25),
                             pos=(0, 0))'''

"""



