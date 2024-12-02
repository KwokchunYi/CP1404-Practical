from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class DynamicLabelsApp(App):
    def build(self):
        self.names = ["Alice", "Bob", "Charlie", "Diana"]
        layout = BoxLayout(orientation='vertical')

        for name in self.names:
            label = Label(text=name)
            layout.add_widget(label)

        return layout

DynamicLabelsApp().run()
