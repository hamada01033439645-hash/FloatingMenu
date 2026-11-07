from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class FloatingMenu(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=20, spacing=12)
        root.add_widget(Label(text='GAME FLOATING MENU', font_size=24))

        for name in ['ESP', 'GOD MODE', 'INFINITE AMMO', 'AIMBOT']:
            btn = Button(text=name + ' : OFF', size_hint_y=None, height=55)

            def toggle(instance):
                if instance.text.endswith('OFF'):
                    instance.text = instance.text.replace('OFF', 'ON')
                else:
                    instance.text = instance.text.replace('ON', 'OFF')

            btn.bind(on_press=toggle)
            root.add_widget(btn)

        root.add_widget(Label(text='Demo interface only'))
        return root

FloatingMenu().run()
