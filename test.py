from kivy.app import App
from kivy.uix.button import Button


class Application(App):
    def build(self):
        my_but=Button(text="hello", font_size=30, background_color="cyan")

        return my_but





Application().run()