from typing import Protocol

from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from pathlib import Path

from view.popup_widget import PopupWidget, PopupModalView

class HangmanViewModel(Protocol):
    guesses: int
    secret_word: str
    letters_guessed: list[str]
    word_state: str
    score: int

    game_over: bool
    word_guessed: bool

    def start(self) -> None: ...
    def guess_letter(self, letter: str) -> None: ...
    def reset_game(self) -> None: ...


class HangmanLayout(BoxLayout):
    view_model = ObjectProperty()
    word_state = StringProperty()
    attempts_left = NumericProperty()
    secret_word = StringProperty()
    score = NumericProperty(0)

    def __init__(self, view_model: HangmanViewModel, **kwargs) -> None:
        super().__init__(**kwargs)
        self.view_model = view_model
        
        #Set initial values
        self.word_state = self.view_model.word_state
        self.attempts_left = self.view_model.guesses
        self.score = self.view_model.score
        self.secret_word = self.view_model.secret_word

        # Bind to changes in view_model
        self.view_model.bind(word_state=self.setter("word_state"))
        self.view_model.bind(guesses=self.setter("attempts_left"))
        self.view_model.bind(score=self.setter("score"))
        self.view_model.bind(secret_word=self.setter("secret_word"))

        self.view_model.bind(game_over=self.on_game_over)
        self.view_model.bind(word_guessed=self.on_word_guessed)
    
    def start_hangman(self) -> None:
        self.view_model.start()
        self.ids.screen_manager.current = "hangman"

    def on_game_over(self, instance, value) -> None:
        if value:
            #scrn = self.ids.game_screen
            #layout= FloatLayout()
            overlay: PopupModalView = PopupModalView(size=self.size, auto_dismiss=False)
            popup: PopupWidget = PopupWidget(
                heading="Game Over",
                first_label=f"Score: {self.score}",
                second_label=str(self.secret_word).upper(),
                first_btn_text="PLAY AGAIN",
                when_press_first= lambda *a: self.play_again(overlay),
                second_btn_text= "QUIT",
                when_press_second= lambda *a: self.quit_game(overlay)
            )

            overlay.add_widget(popup)
            overlay.open()
    
    def on_word_guessed(self, instance, value) -> None:
        if value:
            #scrn = self.ids.game_screen
            overlay: PopupModalView = PopupModalView(size=self.size, auto_dismiss=False)
            popup: PopupWidget = PopupWidget(
                heading="Word Guessed",
                first_label=f"Score: {self.view_model.score}",
                second_label=str(self.secret_word).upper(),
                first_btn_text="PLAY AGAIN",
                when_press_first= lambda *a: self.play_again(overlay),
                second_btn_text= "QUIT",
                when_press_second= lambda *a: self.quit_game(overlay)
            )

            overlay.add_widget(popup)
            overlay.open()

    def quit_confirm(self) -> None:

        overlay: PopupModalView = PopupModalView(size=self.size, auto_dismiss=True)
        popup: PopupWidget = PopupWidget(
            heading="Quit Game",
            first_label="Are sure you want to QUIT?",
            first_btn_text="RETURN",
            when_press_first= lambda *a: overlay.dismiss(),
            second_btn_text= "QUIT",
            when_press_second= lambda *a: self.quit_game(overlay)
        )
        overlay.add_widget(popup)
        
        overlay.open()

    def play_again(self, overlay: PopupModalView) -> None:
        self.view_model.reset_game()
        
        #for loop to reset buttons press during game
        for btn in self.ids.game_screen.letters:
            btn.disabled = False
        
        overlay.dismiss()

    def quit_game(self, overlay) -> None:
        self.ids.screen_manager.current = "start"
        self.view_model.reset_game()
        overlay.dismiss()
        
        for btn in self.ids.game_screen.letters:
            btn.disabled = False
        

kv_path: Path = Path(__file__).parent / "hangman_view.kv"
Builder.load_file(str(kv_path))