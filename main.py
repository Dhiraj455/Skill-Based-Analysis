#Hello World Page Using KivyMd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
# from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

ques_ans = {
    0: {
        'question': 'How Many Continents are there in the World?',
        'option': ['7', '8', '9', '10'],
        'answer': '7'
    },
    1: {
        'question': 'Which Is India\'s Capital?',
        'option': ['New Delhi', 'Mumbai', 'Chennai', 'Kolkata'],
        'answer': 'New Delhi'
    },
}

str = """
ScreenManager:
    WelcomeScreen:
    LoginScreen:
    SignupScreen:
    MainScreen:
    QuizScreen:
    
<WelcomeScreen>:
    name: 'welcome'
    MDLabel:
        text: 'Welcome to KivyMD'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .7}
    MDFloatingActionButton:
        id: welcome_fab
        icon: 'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.5}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'signup'
            root.manager.transition.direction = 'left'

<SignupScreen>:
    name: 'signup'
    MDLabel:
        text: 'Signup'
        halign: 'center'
        font_style: 'H2'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDTextField:
        hint_text: 'Username'
        pos_hint: {'center_x': .5, 'center_y': .7}
        size_hint: (0.7,0.1)
    MDTextField:
        hint_text: 'Email'
        pos_hint: {'center_x': .5, 'center_y': .6}
        size_hint: (0.7,0.1)
    MDTextField:
        hint_text: 'Password'
        pos_hint: {'center_x': .5, 'center_y': .5}
        required: True
        size_hint: (0.7,0.1)
        password: True
    MDFloatingActionButton:
        id: signup_fab
        icon: 'check'
        md_bg_color: app.theme_cls.primary_color
        user_font_size: '40sp'
        pos_hint: {'center_x': .5, 'center_y': .3}
        on_press: 
            root.manager.current = 'login'
            root.manager.transition.direction = 'down'
    MDFloatingActionButton:
        id: next
        icon: 'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':.1,'center_y':.3}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'welcome'
            root.manager.transition.direction = 'left'
<LoginScreen>:
    name: 'login'
    MDLabel:
        text: 'Login'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDTextField:
        hint_text: 'Username'
        pos_hint: {'center_x': .5, 'center_y': .7}
        required: True
        size_hint: (0.7,0.1)
    MDTextField:
        hint_text: 'Password'
        pos_hint: {'center_x': .5, 'center_y': .5}
        required: True
        size_hint: (0.7,0.1)
        password: True
    MDFloatingActionButton:
        icon: 'check'
        md_bg_color: app.theme_cls.primary_color
        user_font_size: '40sp'
        pos_hint: {'center_x': .5, 'center_y': .3}
        on_press: 
            root.manager.current = 'welcome'
            root.manager.transition.direction = 'down'
    MDFloatingActionButton:
        icon: 'arrow-left'
        md_bg_color: app.theme_cls.primary_color
        user_font_size: '40sp'
        pos_hint: {'center_x': .1, 'center_y': .3}
        on_press: 
            root.manager.current = 'signup'
            root.manager.transition.direction = 'left'
    MDFloatingActionButton:
        icon: 'arrow-right'
        md_bg_color: app.theme_cls.primary_color
        user_font_size: '40sp'
        pos_hint: {'center_x': .9, 'center_y': .3}
        on_press: 
            root.manager.current = 'main'
            root.manager.transition.direction = 'right'
<MainScreen>:
    name: 'main'
    MDLabel:
        text: 'Skill Based Analysis'
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDLabel:
        text: 'Recents'
        font_style: 'H6'
        halign: 'center'
        pos_hint: {'center_x': .1, 'center_y': .7}
    MDFloatingActionButton:
        icon: 'plus'
        md_bg_color: app.theme_cls.primary_color
        user_font_size: '40sp'
        pos_hint: {'center_x': .1, 'center_y': .3}
        on_press:
            root.manager.current = 'quiz'
            root.manager.transition.direction = 'left'
    MDScreen:
        MDNavigationLayout:
            ScreenManager:
                MDScreen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Menu'
                            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                            elevation:5
                        Widget:
            MDNavigationDrawer:
                id: nav_drawer
                ContentNavigationDrawer:
                    orientation: 'vertical'
                    padding: "15dp"
                    spacing: "15dp"
                    MDLabel:
                        text: "Menu"
                        font_style: "Subtitle1"
                        size_hint_y: None
                        height: self.texture_size[1]
                    ScrollView:
                        DrawerList:
                            id: md_list
                            MDList:
                                OneLineIconListItem:
                                    text: "Home"
                                    IconLeftWidget:
                                        icon: "home"
                                OneLineIconListItem:
                                    text: "Profile"
                                    IconLeftWidget:
                                        icon: "account-circle"
                                OneLineIconListItem:
                                    text: "Test"
                                    IconLeftWidget:
                                        icon: "book"
                                OneLineIconListItem:
                                    text: "Logout"
                                    IconLeftWidget:
                                        icon: "logout"
<QuizScreen>:
    name: 'quiz'
    MDLabel:
        text: 'Skill Quiz'
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDLabel:
        id: question
        text: ''
        font_style: 'H6'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .7}
    MDFlatButton:
        id: option1
        text: ''
        pos_hint: {'center_x': .3, 'center_y': .5}
    MDFlatButton:
        id: option2`
        text: ''
        pos_hint: {'center_x': .7, 'center_y': .5}
    MDFlatButton:
        id: option3
        text: ''
        pos_hint: {'center_x': .3, 'center_y': .3}
    MDFlatButton:
        id: option4
        text: ''
        pos_hint: {'center_x': .7, 'center_y': .3}
                         
"""
class WelcomeScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class ContentNavigationDrawer(BoxLayout):
    pass
class DrawerList(ThemableBehavior, MDList):
    pass
class QuizScreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(SignupScreen(name='signup'))
sm.add_widget(MainScreen(name='main'))

class MainApp(MDApp):
    def build(self):
        self.str = Builder.load_string(str)
        return self.str

    def on_start(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.accent_hue = '500'
        self.theme_cls.theme_mode = 'Light'
    

MainApp().run()
