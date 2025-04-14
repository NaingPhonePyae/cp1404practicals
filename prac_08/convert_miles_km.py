from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """

    status_text = StringProperty()

    def build(self):
        """build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation (could be button press or other call), output result to label widget """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.status_text = str(result)

    def handle_increment(self, increment):
        """Handle increments of miles input with 1 and -1 up down increments, update miles displayed"""
        value = self.get_validated_miles() + increment
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Get valid miles input from text entry widget using 0 if invalid"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


if __name__ == '__main__':
    MilesConverterApp().run()
