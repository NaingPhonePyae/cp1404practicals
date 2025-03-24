from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):

    def build(self):
        """Build Kivy GUI"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet the input name when pressed"""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def press_clear(self):
        """Clear the input name box and Greet button to default string"""
        self.root.ids.output_label.text = "Greet"
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
