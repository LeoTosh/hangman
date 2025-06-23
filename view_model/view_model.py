from kivy.properties import BooleanProperty, ListProperty, NumericProperty, StringProperty
from kivy.event import EventDispatcher

class HangmanViewModel(EventDispatcher):
    guesses = NumericProperty(6)
    secret_word = StringProperty()
    letters_guessed = ListProperty()
    word_state = StringProperty()
    score = NumericProperty(0)

    game_over = BooleanProperty(False)
    word_guessed= BooleanProperty(False)

    def __init__(self, model, **kwargs) -> None:
        super().__init__(**kwargs)
        self.model = model

        self.bind(guesses=self._check_game_over)
        self.bind(word_state=self._is_word_guessed)

    def start(self) -> None:
        self.model.start()
        
        self.guesses = self.model.guesses
        self.secret_word = self.model.secret_word
        print(self.secret_word)
        self.word_state = self.model.word_state
        self.letters_guessed = self.model.letters_guessed
        self.score = self.model.score
    
    def guess_letter(self, letter: str) -> None:
        
        if letter in self.model.secret_word:
            self.model.letters_guessed.append(letter)
            self.model.word_state = self.model.get_guessed_word()
            self.model.cal_score()
            self.score = self.model.score
            self.word_state = self.model.word_state            
        elif not self.model.is_letter_in_secret_word(letter) and self.model.is_vowel(letter):
            self.model.guesses -= 2
            self.guesses = self.model.guesses
            self.model.cal_score()
            self.score = self.model.score
        else:
            self.model.guesses -= 1
            self.guesses = self.model.guesses
            self.model.cal_score()
            self.score = self.model.score


    def _check_game_over(self, *args) -> None:
        if self.model.game_over():
            self.game_over = True

    def _is_word_guessed(self, *args) -> None:
        if self.model.is_word_guessed():
            self.word_guessed = True

    def reset_game(self) -> None:
        self.model.reset()
        self.start()
        
        self.word_guessed = False
        self.game_over = False


        

if __name__ == "__main__":
    HangmanViewModel(HangmanModel())