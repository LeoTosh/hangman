from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from pathlib import Path
from kivy.properties import NumericProperty, ObjectProperty, StringProperty, ListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from pathlib import Path
from kivy.app import App

import string


class GameScreen(Screen):
    view_model = ObjectProperty()
    score = StringProperty("0")
    attempts_left = NumericProperty(6)
    word_state = StringProperty("")


class TopWidgets(BoxLayout):
    pass

class AlphakeyButton(Button):
    custom_color = ListProperty([0.482, 0.627, 0.902, 1])

class AlphakeyWidget(GridLayout):
    letters = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint_y = None
        self.height = "240dp"
        
        #generate buttons automatically

        
        for i, letter in enumerate(string.ascii_lowercase):
            if 7 < i <= 15:
                button_color = (0.996, 0.682, 0.333, 1)
            elif 15 < i <= 23:
                button_color = (0.38, 0.663, 0.473, 1)
            else:
                button_color = (0.992, 0.549, 0.4, 1)

            btn = AlphakeyButton(text=letter, 
                size_hint_y=None, 
                height=50,
                font_size="20sp",
                custom_color=button_color)
            
            btn.bind(on_press=self.on_letter_pressed) #when the button is pressed call the on_letter_pressed method
            self.add_widget(btn)
    
    def on_letter_pressed(self, button):
        button.disabled = True
        letter = button.text
        app = App.get_running_app()
        app.root.view_model.guess_letter(letter)
        self.letters.append(button)

kv_path: Path = Path(__file__).parent / "game_screen.kv"
Builder.load_file(str(kv_path))