from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
FloatLayout:

    Image:
        source: 'logo.png'
        size_hint: None, None
        size: "80dp", "80dp"
        pos_hint: {"top": 1, "x": 0}

    MDBottomNavigation:
        panel_color: 1, 1, 1, 1
        text_color_normal: 0, 0, 0, 1
        text_color_active: 0, 0, 0, 1

        MDBottomNavigationItem:
            name: 'menu'
            text: 'Menu'
            icon: 'menu'
            MDLabel:
                text: 'Menu options will appear here'
                halign: 'center'
                theme_text_color: 'Primary'
                font_style: 'H6'

        MDBottomNavigationItem:
            name: 'home'
            text: 'Home'
            icon: 'home'
            MDLabel:
                text: 'Home - Awareness & Updates'
                halign: 'center'
                theme_text_color: 'Primary'
                font_style: 'H6'

        MDBottomNavigationItem:
            name: 'setting'
            text: 'seting'
            icon: 'cog'
            text_color_active: 1, 0, 0, 1  # قرمز فعال
            text_color_normal: 1, 0, 0, 1  # قرمز عادی
            MDLabel:
                text: 'Setting...'
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: 1, 0, 0, 1
                font_style: 'H6'

        MDBottomNavigationItem:
            name: 'chat'
            text: 'Chat'
            icon: 'chat'
            MDLabel:
                text: 'Secure Chat with Support'
                halign: 'center'
                theme_text_color: 'Primary'
                font_style: 'H6'

        MDBottomNavigationItem:
            name: 'help'
            text: 'Help'
            icon: 'help-circle'
            MDLabel:
                text: 'Guides, FAQ and Resources'
                halign: 'center'
                theme_text_color: 'Primary'
                font_style: 'H6'
'''

class Model2App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)

if __name__ == '__main__':
    Model2App().run()
