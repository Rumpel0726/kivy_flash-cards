import sqlite3

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.screen import MDScreen
import sqlite3
import random as rn
from kivymd.toast import toast

sm = ScreenManager()
Builder.load_string('''
<MainActivity>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: "#1E1E15"

        MDTopAppBar:
            title: "Флеш-карточки"

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
                on_release: app.button_vvod_click()

            MDRoundFlatButton:
                text: "Список вопросов"
                text_color: "white"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release: app.button_list_click()                

            MDRoundFlatButton:
                text: "Тренероваться"
                text_color: "white"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release: app.button_train_click()

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

<Activity_4>:             
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: "#1E1E15"

        MDTopAppBar:
            title: "Редактор вопроса"
            anchor_title: "right"
            left_action_items: [["arrow-left", lambda x: app.button_back_3_click()]]        

        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#1E1E15"
            padding: 30
            spacing: 30

            MDLabel:
                text: " "
                halign: "center"
            
            MDLabel:
                text: " "
                id: question_id
                halign: "center"
                opacity: 0
            
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
                on_release: app.button_save_changes_click()

            MDRoundFlatButton:
                text: "Удалить"
                text_color: "white"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release: app.button_delete_click()

            MDLabel:
                text: " "
                halign: "center"
                
                
<Activity_5>:             
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: "#1E1E15"

        MDTopAppBar:
            title: "Тренеровка"
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
            
            MDLabel:
                text: " "
                id: question_id
                halign: "center"
                opacity: 0
                                
            MDLabel:
                text: " "
                halign: "center"
            
            MDBoxLayout:
                orientation: "vertical"
                md_bg_color: "#1E1E15"
                padding: 30
                spacing: 30
                
                MDLabel:
                    text: "Вопрос: "
                    halign: "center"
                
                MDLabel:
                    id: question_name
                    halign: "center"

            MDLabel:
                text: " "
                halign: "center"
                
            MDBoxLayout:
                id: answer_box
                opacity: 0
                orientation: "vertical"
                md_bg_color: "#1E1E15"
                padding: 30
                spacing: 30            
                
                MDLabel:
                    text: "Ответ: "
                    halign: "center"
                
                MDLabel:
                    id: question_value
                    halign: "center"             

            MDRoundFlatButton:
                text: "Показать ответ"
                text_color: "white"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release: app.button_show_hide_que_click()
            
            MDLabel:
                text: "Оценка: "
                halign: "center"
            
            MDBoxLayout:
                orientation: "horizontal"
                md_bg_color: "#1E1E15"
                padding: 10
                spacing: 5
                pos_hint: {"center_x": .5, "center_y": .5}
                
                MDRoundFlatButton:
                    text: "5"
                    text_color: "white"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size: 50, 50
                    on_release: app.button_grade_click(5)
                
                MDRoundFlatButton:
                    text: "4"
                    text_color: "white"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: app.button_grade_click(4)
                
                MDRoundFlatButton:
                    text: "3"
                    text_color: "white"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: app.button_grade_click(3)
                
                MDRoundFlatButton:
                    text: "2"
                    text_color: "white"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: app.button_grade_click(2)
                
                MDRoundFlatButton:
                    text: "1"
                    text_color: "white"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release: app.button_grade_click(1)
                

            MDLabel:
                text: " "
                halign: "center"

''')

conn = sqlite3.connect("app_database.db")
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS my_questions(id_ integer primary key, question_name text, question_value text, 
                                                                                question_grade int)""")
conn.commit()


class MainActivity(Screen):
    pass


class Activity_2(Screen):
    pass


class Activity_3(Screen):
    pass


class Activity_4(Screen):
    pass

class Activity_5(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        sm.add_widget(MainActivity(name='MainActivity'))
        sm.add_widget(Activity_2(name='Activity_2'))
        sm.add_widget(Activity_3(name='Activity_3'))
        sm.add_widget(Activity_4(name='Activity_4'))
        sm.add_widget(Activity_5(name='Activity_5'))

        return sm

    def button_vvod_click(self):
        sm.transition.direction = 'left'
        sm.current = 'Activity_2'
        sm.get_screen('Activity_2').ids.question_name.text = ""
        sm.get_screen('Activity_2').ids.question_value.text = ""

    def button_train_click(self):
        c.execute("SELECT count(id_) FROM my_questions")
        records = c.fetchone()
        print(records[0])
        if records[0] == 0:
            self.show_toast("Вы не можете тренероваться с пустым списком карточек!")
            return

        sm.transition.direction = 'left'
        sm.current = 'Activity_5'
        self.show_next_question()

    def show_next_question(self):
        sm.get_screen('Activity_5').ids.answer_box.opacity = 0
        c.execute("SELECT count(id_) FROM my_questions")
        records = c.fetchone()
        print(records[0])

        nid = rn.randint(1, records[0])

        c.execute("SELECT * FROM my_questions")
        ind = 1
        records_all = c.fetchall()

        for record in records_all:
            if ind == nid:
                self.show_question_info('Activity_5', record[0])
                break
            ind += 1

    def button_back_2_click(self):
        sm.transition.direction = 'right'
        sm.current = 'MainActivity'

    def button_back_3_click(self):
        sm.transition.direction = 'right'
        sm.current = 'Activity_3'

    def button_list_click(self):
        self.refresh_mdlist()

    def refresh_mdlist(self):
        sm.transition.direction = 'left'
        sm.current = 'Activity_3'

        c.execute("SELECT * FROM my_questions")
        ind = 0
        records = c.fetchall()

        sm.get_screen('Activity_3').ids.container.clear_widgets()
        for record in records:
            ind += 1
            # word = f'{word}\n{record[0]}'
            # self.root.ids.word_label.text = f'{word}'
            sm.get_screen('Activity_3').ids.container.add_widget(
                TwoLineListItem(text=f"{ind}. {record[1]}",
                                secondary_text=f"Оценка: {record[3]}",
                                on_release=self.mdlist_click, id=f"{record[0]}")
            )

    def button_save_click(self):
        name_ = sm.get_screen('Activity_2').ids.question_name.text
        print("Name: ", name_)
        value_ = sm.get_screen('Activity_2').ids.question_value.text
        print("Value: ", value_)
        if name_ == "":
            self.show_toast("Поле 'вопрос' должно быть заполенным!")
            return

        if value_ == "":
            self.show_toast("Поле 'ответ' должно быть заполенным!")
            return
        c.execute('INSERT INTO my_questions(question_name, question_value, question_grade) VALUES(:nm, :val, :grade)',
                  {'nm': name_, 'val': value_, 'grade': 1})
        conn.commit()
        self.show_toast("Карточка успешно сохранена!")

    def mdlist_click(self, select_card):
        print(select_card.id)
        sm.transition.direction = 'left'
        sm.current = 'Activity_4'

        self.show_question_info('Activity_4', select_card.id)

    def show_question_info(self, act_name, id):
        c.execute("SELECT * FROM my_questions WHERE id_=" + str(id))
        records = c.fetchall()

        for record in records:
            sm.get_screen(act_name).ids.question_name.text = f'{record[1]}'
            sm.get_screen(act_name).ids.question_value.text = f'{record[2]}'
            sm.get_screen(act_name).ids.question_id.text = f'{record[0]}'

    def button_save_changes_click(self):
        name_ = sm.get_screen('Activity_4').ids.question_name.text
        print("Name: ", name_)
        value_ = sm.get_screen('Activity_4').ids.question_value.text
        print("Value: ", value_)
        id_ = sm.get_screen('Activity_4').ids.question_id.text
        print("ID: ", id_)
        if name_ == "":
            self.show_toast("Поле 'вопрос' должно быть заполенным!")
            return

        if value_ == "":
            self.show_toast("Поле 'ответ' должно быть заполенным!")
            return
        c.execute('UPDATE my_questions SET question_name=:nm, question_value=:val, question_grade=:grade WHERE id_=:id',
                  {'nm': name_, 'val': value_, 'id': id_, 'grade': 1})
        conn.commit()
        self.show_toast("Карточка успешно изменена!")

    def button_delete_click(self):
        id_ = sm.get_screen('Activity_4').ids.question_id.text
        print("ID: ", id_)

        c.execute('DELETE FROM my_questions WHERE id_=:id',
                  {'id': id_})
        conn.commit()
        self.refresh_mdlist()

    def button_show_hide_que_click(self):
        sm.get_screen('Activity_5').ids.answer_box.opacity = 1

    def button_grade_click(self, grade):
        que_id = sm.get_screen('Activity_5').ids.question_id.text
        c.execute('UPDATE my_questions SET question_grade=:que_gr WHERE id_=:id',
                  {'que_gr': grade, 'id': que_id})
        conn.commit()
        self.show_toast("Следующий вопрос")
        self.show_next_question()

    def show_toast(self, mess):
        toast(mess)

MainApp().run()
