from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty

class Timer(Label):
    done = BooleanProperty(False)

    def __init__(self, txt, total, **kwargs):
        self.done = False
        self.total = total
        self.current = 0 if "Пройшло" in txt else total
        self.txt = txt
        self.update_text()
        super().__init__(**kwargs)

    def start_count_up(self):
        Clock.schedule_interval(self.increment, 1)

    def start_count_down(self):
        Clock.schedule_interval(self.decrement, 1)

    def increment(self, dt):
        if self.current < self.total:
            self.current += 1
            self.update_text()
        if self.current >= self.total:
            self.done = True
            return False

    def decrement(self, dt):
        if self.current > 0:
            self.current -= 1
            self.update_text()
        if self.current <= 0:
            self.done = True
            return False

    def update_text(self):
        self.text = f"{self.txt} {self.current}"