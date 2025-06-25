import random


class HangmanModel:
    def __init__(self) -> None:
        #number of attempts and warnings
        self.guesses: int = 6
        self.score: int = 0

        self.secret_word: str = ""
        self.letters_guessed: list[str] = []
        self.word_state: str = ""

    def load_words(self) -> list[str]:
        """
        Returns a list of valid words. Words are strings of lowercase letters.
        
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        filename: str = "./model/words.txt"
        with open(filename) as in_file:
            wordlist: list[str] = in_file.readline().split()
        #print(len(wordlist))
        return wordlist


    def choose_word(self) -> str:
        """
        wordlist (list): list of words (strings)
        
        Returns a word from wordlist at random
        """
        return random.choice(self.load_words())

    def start(self) -> None:
        """
        Returns None
        Start game by initialising secret word and word state.
        """
        if not self.secret_word:
            self.secret_word = self.choose_word()
            self.word_state = self.get_guessed_word()

    def is_word_guessed(self) -> bool:
        '''
        secret_word: string, the word the user is guessing; assumes all letters are
        lowercase
        letters_guessed: list (of letters), which letters have been guessed so far;
        assumes that all letters are lowercase
        returns: boolean, True if all the letters of secret_word are in letters_guessed;
        False otherwise
        '''
        if not self.letters_guessed or not self.secret_word:
            return False
        return all(letter in self.letters_guessed for letter in self.secret_word)
        
    def get_guessed_word(self) -> str:
        '''
        secret_word: string, the word the user is guessing
        letters_guessed: list (of letters), which letters have been guessed so far
        returns: string, comprised of letters, underscores (_), and spaces that represents
        which letters in secret_word have been guessed so far.
        '''

        return "".join(letter if letter in self.letters_guessed else "_ " for letter in self.secret_word)

    def is_letter_in_secret_word(self, letter: str) -> bool:
        return True if letter in self.secret_word else False
    
    def game_over(self) -> bool:
        """
        Returns None
        Logic to check if game is over.
        """
        return True if self.guesses <= 0 else False

    def cal_score(self) -> None:
        """
        Returns None
        Logic to calculate score.
        """
        unique_correct: int = len(set(self.letters_guessed))
        #total_unique: int = len(set(self.secret_word))
        self.score = round((unique_correct * 10) * (self.guesses * 2))
    
    def reset(self) -> None:
        """
        Returns None
        reset every key value to defult before game start.
        """
        self.score = 0
        self.guesses = 6
        self.secret_word = ""
        self.letters_guessed = []
        self.word_state= ""

    @staticmethod
    def is_vowel(letter: str) -> bool:
        vowel: list[str] = ["a", "e", "i", "o", "u"]
        return True if letter in vowel else False


if __name__ == "__main__":
    game: HangmanModel = HangmanModel()
    game.start()
    print(game.secret_word)
    print(game.cal_score())
    print(game.is_vowel("b"), game.game_over())
