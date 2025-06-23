from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from pathlib import Path


kv_path: Path = Path(__file__).parent / "start_screen.kv"
Builder.load_file(str(kv_path))

class StartScreen(Screen):
    pass