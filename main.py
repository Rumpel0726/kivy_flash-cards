import sqlite3

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen
import sqlite3

sm = ScreenManager()
Builder.load_string('''
<MainActivity>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: "#1E1E15"

        MDTopAppBar:
            title: "MDTopAppBar"

        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#1E1E15"
            padding: 10
            spacing: 10

            MDLabel:
                text: " "
                halign: "center"

            MDRoundFlatButton:
                text: "Ввод вопросов"
                text_color: "white"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release: app.button_1_click()

            MDRoundFlatButton:
                text: "Список вопросов"
                text_color: "white"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release: app.button_3_click()                

            MDRoundFlatButton:
                text: "MDRoundFlatButton"
                text_color: "white"
                pos_hint: {"center_x": .5, "center_y": .5}                        

            MDLabel:
                text: " "
                halign: "center"

<Activity_2>:             
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: "#1E1E15"

        MDTopAppBar:
            title: "Ввод вопроса"
            anchor_title: "right"
            left_action_items: [["back", lambda x: app.button_back_2_click()]]        

        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#1E1E15"
            padding: 30
            spacing: 30

            MDLabel:
                text: " "
                halign: "center"

            MDTextField:
                id: question_name
                hint_text: "Введите вопрос"
                helper_text: "This will disappear when you click off"
                helper_text_mode: "on_focus"
                pos_hint: {"center_x": .5, "center_y": .5} 
                multiline: "true"

            MDTextField:
                id: question_value
                hint_text: "Введите ответ"
                helper_text: "This will disappear when you click off"
                helper_text_mode: "on_focus"   
                pos_hint: {"center_x": .5, "center_y": .5}
                multiline: "true"                     

            MDRoundFlatButton:
                text: "Сохранить"
                text_color: "white"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release: app.button_save_click()

            MDLabel:
                text: " "
                halign: "center"

<Activity_3>:             
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: "#1E1E15"

        MDTopAppBar:
            title: "Список вопросов"
            anchor_title: "right"
            left_action_items: [["back", lambda x: app.button_back_2_click()]]        

        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#1E1E15"
            padding: 30
            spacing: 30

            ScrollView:

                MDList:
                    id: container
''')

conn = sqlite3.connect("app_database.db")
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS my_questions(id_ integer primary key, question_name text, question_value text)""")
conn.commit()


class MainActivity(Screen):
    pass


class Activity_2(Screen):
    pass


class Activity_3(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        sm.add_widget(MainActivity(name='MainActivity'))
        sm.add_widget(Activity_2(name='Activity_2'))
        sm.add_widget(Activity_3(name='Activity_3'))

        return sm

    def button_1_click(self):
        sm.transition.direction = 'left'
        sm.current = 'Activity_2'

    def button_back_2_click(self):
        sm.transition.direction = 'right'
        sm.current = 'MainActivity'

    def button_3_click(self):
        sm.transition.direction = 'left'
        sm.current = 'Activity_3'

        c.execute("SELECT * FROM my_questions")
        records = c.fetchall()

        sm.get_screen('Activity_3').ids.container.clear_widgets()
        for record in records:
            # word = f'{word}\n{record[0]}'
            # self.root.ids.word_label.text = f'{word}'
            sm.get_screen('Activity_3').ids.container.add_widget(
                OneLineListItem(text=f"{record[1]}")
            )

    def button_save_click(self):
        name_ = sm.get_screen('Activity_2').ids.question_name.text
        print("Name: ", name_)
        value_ = sm.get_screen('Activity_2').ids.question_value.text
        print("Value: ", value_)

        c.execute('INSERT INTO my_questions(question_name, question_value) VALUES(:nm, :val)',
                  {'nm': name_, 'val': value_})
        conn.commit()


MainApp().run()



























'''
from kivy.config import Config
from kivymd.uix.button import MDFlatButton, MDFloatingActionButton, MDRoundFlatButton

#Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '380')
Config.set('graphics', 'height', '675')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivy.lang import Builder


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        btn1 = MDRoundFlatButton(text='Hello World', pos_hint={'center_x': 0.5, 'center_y': 0.5})

        btn2 = MDRoundFlatButton(text='Hello World', pos_hint={'center_x': 0.5, 'center_y': 0.4})

        btn3 = MDRoundFlatButton(text='Hello World', pos_hint={'center_x': 0.5, 'center_y': 0.3})

        screen.add_widget(btn1)
        screen.add_widget(btn2)
        screen.add_widget(btn3)
        return screen


DemoApp().run()




"""
class AppCore(Widget):
    pass

'''
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

'''
'''return Button(text="Старт",
                             font_size=30,
                             on_press=self.btn_press,
                             background_color=(.30, .69, .31, 1),
                             background_normal='',
                             size_hint=(.5, .25),
                             pos=(0, 0))'''

