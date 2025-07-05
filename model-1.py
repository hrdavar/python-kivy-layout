from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout

KV = '''
ScreenManager:
    HomeScreen:
    ReportScreen:
    ChatScreen:
    HelpScreen:

<BottomNavBar@BoxLayout>:
    size_hint_y: None
    height: '60dp'
    spacing: '10dp'
    padding: '10dp'
    orientation: 'horizontal'
    Button:
        text: 'Home'
        on_release: app.switch_screen('home')
    Button:
        text: 'Report'
        on_release: app.switch_screen('report')
    Button:
        text: 'Menu'
        on_release: app.open_menu()
    Button:
        text: 'Chat'
        on_release: app.switch_screen('chat')
    Button:
        text: 'Help'
        on_release: app.switch_screen('help')

<MenuModal@ModalView>:
    size_hint: .8, .5
    auto_dismiss: True
    BoxLayout:
        orientation: 'vertical'
        spacing: '10dp'
        padding: '20dp'
        Button:
            text: 'contact us'
        Button:
            text: 'My Saved'
        Button:
            text: 'Settings'

<HomeScreen>:
    name: 'home'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Home'
        BottomNavBar:

<ReportScreen>:
    name: 'report'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Report Suspicious Activity'
        BottomNavBar:

<ChatScreen>:
    name: 'chat'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Secure Chat with Support'
        BottomNavBar:

<HelpScreen>:
    name: 'help'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Guides, FAQ and Resources'
        BottomNavBar:
'''

class HomeScreen(Screen):
    pass

class ReportScreen(Screen):
    pass

class ChatScreen(Screen):
    pass

class HelpScreen(Screen):
    pass

class Model1App(App):
    def build(self):
        self.root = Builder.load_string(KV)
        return self.root

    def switch_screen(self, name):
        self.root.current = name

    def open_menu(self):
        modal = ModalView(size_hint=(0.8, 0.5))
        modal_box = Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    spacing: '10dp'
    padding: '20dp'
    Button:
        text: 'contact us'
    Button:
        text: 'My Saved'
    Button:
        text: 'Settings'
        ''')
        modal.add_widget(modal_box)
        modal.open()

if __name__ == '__main__':
    Model1App().run()
