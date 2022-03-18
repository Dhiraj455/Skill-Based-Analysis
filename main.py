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
        'option1': '7',
        'option2': '8',
        'option3': '9',
        'option4': '10',
        'answer': '7'
    },
    1: {
        'question': 'Python is a __________ language.',
        'option1': 'High level',
        'option2': 'Interpreted',
        'option3': 'Compiled',
        'option4': 'All of the above',
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
    ProfileScreen:
    
<WelcomeScreen>:
    name: 'welcome'
    MDLabel:
        text: 'Welcome to KivyMD'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .7}
    MDFloatingActionButton:
        id: welcome_fab
        icon: 'android'
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
    MDFloatingActionButton:
        icon: 'account'
        md_bg_color: app.theme_cls.primary_color
        user_font_size: '40sp'
        pos_hint: {'center_x': .8, 'center_y': .8}
        on_press:
            root.manager.current = 'profile'
            root.manager.transition.direction = 'up'
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
        pos_hint: {'center_x': .1, 'center_y': .1}
        on_release:
            root.manager.current = 'quiz'
            root.manager.transition.direction = 'left'
        on_press: app.quiz()
    MDCard:
        size_hint: (0.9,0.1)
        pos_hint: {'center_x': .5, 'center_y': .6}
        md_bg_color: 0,0,0,0.5
        radius: 10
        MDLabel:
            text: '    Python'
            font_style: 'H6'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            pos_hint: {'center_y': .5}
        MDLabel:
            text: '22/30    '
            font_style: 'H6'
            halign: 'right'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            pos_hint: {'center_y': .5}
        MDIconButton:
            icon: 'book-open-variant'
            user_font_size: '40sp'
            pos_hint: {'center_x': .9, 'center_y': .5}
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
    MDCard:
        size_hint: (0.9,0.1)
        pos_hint: {'center_x': .5, 'center_y': .45}
        md_bg_color: 0,0,0,0.5
        radius: 10
        MDLabel:
            text: '    Graphic Design'
            font_style: 'H6'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            pos_hint: {'center_y': .5}
        MDLabel:
            text: '26/30    '
            font_style: 'H6'
            halign: 'right'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            pos_hint: {'center_y': .5}
        MDIconButton:
            icon: 'book-open-variant'
            user_font_size: '40sp'
            pos_hint: {'center_x': .9, 'center_y': .5}
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
    MDCard:
        size_hint: (0.9,0.1)
        pos_hint: {'center_x': .5, 'center_y': .3}
        md_bg_color: 0,0,0,0.5
        radius: 10
        MDLabel:
            text: '    Game Developer'
            font_style: 'H6'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            pos_hint: {'center_y': .5}
        MDLabel:
            text: '20/30    '
            font_style: 'H6'
            halign: 'right'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            pos_hint: {'center_y': .5}
        MDIconButton:
            icon: 'book-open-variant'
            user_font_size: '40sp'
            pos_hint: {'center_x': .9, 'center_y': .5}
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
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
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDLabel:
        id: question
        text: ''
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_y': .7}
    MDRaisedButton:
        id: option1
        font_style: 'H5'
        size_hint: (0.3,0.1)
        md_bg_color: 0,0,0,0.5
        radius: 30
        text: ''
        pos_hint: {'center_x': .3, 'center_y': .5}
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
    MDRaisedButton:
        id: option2
        font_style: 'H5'
        size_hint: (0.3,0.1)
        md_bg_color: 0,0,0,0.5
        radius: 30
        text: ''
        pos_hint: {'center_x': .7, 'center_y': .5}
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
    MDRaisedButton:
        id: option3
        font_style: 'H5'
        size_hint: (0.3,0.1)
        md_bg_color: 0,0,0,0.5
        radius: 30
        text: ''
        pos_hint: {'center_x': .3, 'center_y': .3}
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
    MDRaisedButton:
        id: option4
        font_style: 'H5'
        size_hint: (0.3,0.1)
        md_bg_color: 0,0,0,0.5
        radius: 30
        text: ''
        pos_hint: {'center_x': .7, 'center_y': .3}  
        theme_text_color: 'Custom'
        text_color: 1,1,1,1      
    MDProgressBar:
        id: progress
        value: 10
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x': .5, 'center_y': .1}
<ProfileScreen>:
    name: 'profile'
    MDScreen:
        MDLabel:
            text: 'My Profile'
            font_style: 'H3'
            halign: 'center'
            pos_hint: {'center_x': .5, 'center_y': .8}
        MDCard:
            size_hint: (0.3,0.3)
            pos_hint: {'center_x': .5, 'center_y': .6}
            radius: 30
            Image:
                source: 'people.jpg'
                size_hint: (0.9, 1)
                pos_hint: {'center_x': .5,'center_y': .5}
                size: self.texture_size
                halign: 'center'
        MDLabel:
            text: 'Name: Group 8'
            font_style: 'H5'
            halign: 'center'
            pos_hint: {'center_y': .4}
        MDLabel:
            text: 'Email: group8@gmail.com'
            font_style: 'H5'
            halign: 'center'
            pos_hint: {'center_y': .35}
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
"""
class WelcomeScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class ProfileScreen(Screen):
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
        # self.theme_cls.theme_style = 'Dark'
    
    def quiz(self):
        for i in range(0,2):
            self.str.get_screen('quiz').ids.question.text = ques_ans[i]['question']
            self.str.get_screen('quiz').ids.option1.text = ques_ans[i]['option1']
            self.str.get_screen('quiz').ids.option2.text = ques_ans[i]['option2']
            self.str.get_screen('quiz').ids.option3.text = ques_ans[i]['option3']
            self.str.get_screen('quiz').ids.option4.text = ques_ans[i]['option4']
            # self.str.ids.question.text = ques_ans[i]['question']
            # self.str.ids.option1.text = ques_ans[i]['option'][i]
            # self.str.ids.option2.text = ques_ans[i]['option'][i+1]
            # self.str.ids.option3.text = ques_ans[i]['option'][i+2]
            # self.str.ids.option4.text = ques_ans[i]['option'][i+3]

MainApp().run()
