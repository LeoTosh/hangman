from kivy.core.window import Window
Window.title = "Hangman Game"
Window.size = (360, 720)

from kivy.app import App

from model.hangman_model import HangmanModel
from view.hangman_view import HangmanLayout
from view_model.view_model import HangmanViewModel




class HangmanApp(App):
    def build(self):
        model: HangmanModel = HangmanModel()
        view_model: HangmanViewModel = HangmanViewModel(model=model)
        view: HangmanLayout = HangmanLayout(view_model=view_model)
        return view

if __name__ == "__main__":
    
    HangmanApp().run()