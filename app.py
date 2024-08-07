from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

from instructions import *
from timer import *
from ruffier import test

lbl_color = (.58, .20, 0, 1)
btn_color = (.100, .97, 0, 1)
name = ""
age = 7
P1 = 0
P2 = 0
P3 = 0

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        inst_label = Label(text=txt_instruction, color=lbl_color, font_size=25, bold=True, halign='center', size_hint=(1, .7))

        name_lbl = Label(text="Введіть ім'я", color=lbl_color, bold=True, font_size=30)
        self.name_input = TextInput(text="Микола", multiline=False)
        age_lbl = Label(text="Введіть вік", color=lbl_color, bold=True, font_size=30)
        self.age_input = TextInput(text="7", multiline=False)

        self.btn = Button(
            text="Почати",
            bold=True,
            font_size=30,
            background_color=btn_color,
            size_hint=(.4, .2),
            pos_hint={'center_x': .5}
        )

        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint = (.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(.8, None), height='30sp')

        line1.add_widget(name_lbl)
        line1.add_widget(self.name_input)

        line2.add_widget(age_lbl)
        line2.add_widget(self.age_input)

        main_line = BoxLayout(orientation='vertical', padding=15, spacing=20)
        main_line.add_widget(inst_label)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)
        self.add_widget(main_line)

    def next(self):
        global name, age
        name = self.name_input.text
        age = check_int(self.age_input.text)
        if (age is False or age < 7) or name == '':
            self.age_input.text = '7'
            self.name_input.text = "Микола"
        else:
            self.manager.current = 'second'

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        inst_lbl = Label(text=txt_test1, color=lbl_color, font_size=25, bold=True, halign='center', size_hint=(1, .5))

        self.lbl_time = Timer(txt="Пройшло секунд:", total=15, bold=True, font_size=35, size_hint=(1, .2))
        self.lbl_time.bind(done=self.end_timer)
        lbl_result = Label(text="Введіть результат", color=lbl_color, font_size=30, bold=True, halign='center')
        self.result_input = TextInput(text='1', multiline=False)
        self.result_input.set_disabled(True)
        self.btn = Button(
            text="Почати",
            bold=True,
            font_size=30,
            background_color=btn_color,
            size_hint=(.4, .2),
            pos_hint={'center_x': .5}
        )
        self.btn.on_press = self.next

        line1 =BoxLayout(size_hint=(.8, None), height='30sp')
        line1.add_widget(lbl_result)
        line1.add_widget(self.result_input)

        main_line = BoxLayout(orientation='vertical', padding=15, spacing=20)
        main_line.add_widget(inst_lbl)
        main_line.add_widget(self.lbl_time)
        main_line.add_widget(line1)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def end_timer(self, *args):
        self.result_input.set_disabled(False)
        self.next_screen = True
        self.btn.text = 'Продовжити'

    def next(self):
        global p1
        if self.next_screen is False:
            self.lbl_time.start_count_up()
        else:
            p1 = check_int(self.result_input.text)
            if p1 is False or p1 <= 1:
                self.result_input.text = '1'
            else:
                self.manager.current = 'third'

class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        inst_lbl = Label(text=txt_test2, color=lbl_color, font_size=25, bold=True, halign='center', size_hint=(1, .5))
        self.lbl_sits = Timer(txt="Залишилось присідань:", total=30, bold=True, font_size=35, size_hint=(1, .2))
        self.lbl_sits.bind(done=self.end_timer)
        self.lbl_seconds = Timer(txt="Залишилось секунд:", total=45, bold=True, font_size=35, size_hint=(1, .2))
        self.lbl_seconds.bind(done=self.end_timer)
        self.btn = Button(
            text="Почати",
            bold=True,
            font_size=30,
            background_color=btn_color,
            size_hint=(.4, .2),
            pos_hint={'center_x': .5}
        )
        self.btn.on_press = self.next

        main_line = BoxLayout(orientation='vertical', padding=15)
        main_line.add_widget(inst_lbl)
        main_line.add_widget(self.lbl_sits)
        main_line.add_widget(self.lbl_seconds)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def end_timer(self, *args):
        self.next_screen = True
        self.btn.text = 'Продовжити'

    def next(self):
        if self.next_screen is False:
            self.lbl_sits.start_count_down(num=1.5)
            self.lbl_seconds.start_count_down()
        else:
            self.manager.current = 'fourth'

class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.stage = 0

        inst_label = Label(text=txt_test3, color=lbl_color, font_size=25, bold=True, halign='center', size_hint=(1, .7))

        self.pulse = Label(text="Рахуйте пульс", bold=True, font_size=35, size_hint=(1, .1))
        self.seconds = Timer(txt="", total=15, bold=True, font_size=35, size_hint=(1, .1))
        self.seconds.bind(done=self.end_timer)

        result1_lbl = Label(text="Результат", color=lbl_color, bold=True, font_size=30)
        self.result1_input = TextInput(text="1", multiline=False)
        self.result1_input.set_disabled(True)
        result2_lbl = Label(text="Результат після відпочинку", color=lbl_color, bold=True, font_size=30)
        self.result2_input = TextInput(text="1", multiline=False)
        self.result2_input.set_disabled(True)

        self.btn = Button(
            text="Почати",
            bold=True,
            font_size=30,
            background_color=btn_color,
            size_hint=(.4, .2),
            pos_hint={'center_x': .5}
        )
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(.8, None), height='30sp')

        line1.add_widget(result1_lbl)
        line1.add_widget(self.result1_input)

        line2.add_widget(result2_lbl)
        line2.add_widget(self.result2_input)

        main_line = BoxLayout(orientation='vertical', padding=15, spacing=20)
        main_line.add_widget(inst_label)
        main_line.add_widget(self.pulse)
        main_line.add_widget(self.seconds)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)
        self.add_widget(main_line)

    def end_timer(self, *args):
        if self.seconds.done:
            if self.stage == 0:
                self.stage = 1
                self.seconds.restart(30)
                self.result1_input.set_disabled(False)
                self.pulse.text = "Відпочивайте"
            elif self.stage == 1:
                self.stage = 2
                self.seconds.restart(15)
                self.pulse.text = "Міряйте пульс"
            elif self.stage == 2:
                self.next_screen = True
                self.pulse.text = "Введіть пульс"
                self.result2_input.set_disabled(False)
                self.btn.set_disabled(False)

    def next(self):
        global p2, p3
        if self.next_screen is False:
            self.seconds.start_count_up()
            self.btn.set_disabled(True)
        else:
            p2 = check_int(self.result1_input.text)
            p3 = check_int(self.result2_input.text)
            if p2 is False or p2 <= 1:
                self.result1_input.text = '1'
            elif p3 is False or p3 <= 1:
                self.result2_input.text = '1'
            else:
                self.manager.current = 'result'

class ResultsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lbl = Label(text="", font_size=40)
        self.add_widget(self.lbl)
        self.bind(on_enter=self.before)

    def before(self, *args):
        global p1, p2, p3, age, name
        text = test(p1, p2, p3, age)
        self.lbl.text = name + '\n' + text


class HeartCheck(App):
    def build(self):
        Window.clearcolor = (.87, .85, 0, 1)
        self.title = "Тест Руф'є"
        self.icon = 'icon.png'
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(SecondScreen(name="second"))
        sm.add_widget(ThirdScreen(name="third"))
        sm.add_widget(FourthScreen(name="fourth"))
        sm.add_widget(ResultsScreen(name='result'))
        return sm

app = HeartCheck()
app.run()