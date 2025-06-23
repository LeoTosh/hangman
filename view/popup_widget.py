from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget
from pathlib import Path

kv_path: Path = Path(__file__).parent / "popup_widget.kv"
Builder.load_file(str(kv_path))


class PopupWidget(Widget):
    heading = StringProperty("pop-up")
    first_label = StringProperty("")
    second_label = StringProperty("")
    first_btn_text = StringProperty("PLAY AGAIN")
    second_btn_text = StringProperty("QUIT")

    when_press_first = ObjectProperty(None)
    when_press_second = ObjectProperty(None)

class PopupModalView(ModalView):
    pass