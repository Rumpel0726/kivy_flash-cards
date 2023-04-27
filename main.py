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
            left_action_items: [["arrow-left", lambda x: app.button_back_2_click()]]        

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
            left_action_items: [["arrow-left", lambda x: app.button_back_2_click()]]        

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



