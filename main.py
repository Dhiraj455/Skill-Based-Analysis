#Hello World Page Using KivyMd
from kivymd.app import MDApp
# from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
# from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (450, 700)
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
    QuizScreen1:
    QuizScreen2:
    ProfileScreen:
    
<WelcomeScreen>:
    name: 'welcome'
    MDLabel:
        text: 'Welcome to Career Analysis'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .7}
    MDFloatingActionButton:
        id: welcome_fab
        icon: 'android'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.3}
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
        pos_hint: {'center_x': .9, 'center_y': .1}
        on_press:
            root.manager.current = 'profile'
            root.manager.transition.direction = 'up'
    MDLabel:
        text: 'Career Analysis For Student'
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
            text: '   Graphic Design'
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
            text: '   Game Developer'
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
                                MDFillRoundFlatIconButton:
                                    icon: "home"
                                    text: "Home"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_press: 
                                        root.manager.current = 'main'
                                        root.manager.transition.direction = 'left'
                                MDFlatButton:
                                    text: ""
                                MDFillRoundFlatIconButton:
                                    icon: "account-circle"
                                    text: "Profile"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_press: 
                                        root.manager.current = 'profile'
                                        root.manager.transition.direction = 'left'
                                MDFlatButton:
                                    text: ""
                                MDFillRoundFlatIconButton:
                                    icon: "book"
                                    text: "Test"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_release: 
                                        root.manager.current = 'quiz'
                                        root.manager.transition.direction = 'left'
                                MDFlatButton:
                                    text: ""
                                MDFillRoundFlatIconButton:
                                    icon: "logout"
                                    text: "Logout"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_press: 
                                        root.manager.current = 'signup'
                                        root.manager.transition.direction = 'left'   
<QuizScreen>:
    name: 'quiz'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Quiz'
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
            elevation:5
        Widget:
    MDLabel:
        text: 'Start Quiz'
        font_style: 'H3'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        pos_hint: {'center_y': .5}
    MDFlatButton:
        text: 'Start'
        pos_hint: {'center_x': .5, 'center_y': .4}
        on_press: app.quiz()
        on_release: 
            root.manager.current = 'quiz1'
            root.manager.transition.direction = 'left'
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
                        MDFillRoundFlatIconButton:
                            icon: "home"
                            text: "Home"
                            font_style: "Subtitle1"
                            font_size: "20sp"
                            padding: "10dp"
                            on_press:
                                root.manager.current = 'main'
                                root.manager.transition.direction = 'left'
                        MDFlatButton:
                            text: ""
                        MDFillRoundFlatIconButton:
                            icon: "account-circle"
                            text: "Profile"
                            font_style: "Subtitle1"
                            font_size: "20sp"
                            padding: "10dp"
                            on_press: 
                                root.manager.current = 'profile'
                                root.manager.transition.direction = 'left'
                        MDFlatButton:
                            text: ""
                        MDFillRoundFlatIconButton:
                            icon: "book"
                            text: "Test"
                            font_style: "Subtitle1"
                            font_size: "20sp"
                            padding: "10dp"
                            on_release: 
                                root.manager.current = 'quiz'
                                root.manager.transition.direction = 'left'
                        MDFlatButton:
                            text: ""
                        MDFillRoundFlatIconButton:
                            icon: "logout"
                            text: "Logout"
                            font_style: "Subtitle1"
                            font_size: "20sp"
                            padding: "10dp"
                            on_press: 
                                root.manager.current = 'signup'
                                root.manager.transition.direction = 'left'
                        
<QuizScreen1>:       
    name: 'quiz1'
    MDLabel:
        text: 'Skill Quiz'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDLabel:
        id: question
        text: ''
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_y': .6}
    MDRaisedButton:
        id: option1
        font_style: 'H5'
        size_hint: (0.3,0.1)
        md_bg_color: 0,0,0,0.5
        radius: 30
        text: ''
        pos_hint: {'center_x': .3, 'center_y': .4}
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        on_release:
            root.manager.current = 'quiz2'
            root.manager.transition.direction = 'left'
        on_press:
            app.score()
    MDRaisedButton:
        id: option2
        font_style: 'H5'
        size_hint: (0.3,0.1)
        md_bg_color: 0,0,0,0.5
        radius: 30
        text: ''
        pos_hint: {'center_x': .7, 'center_y': .4}
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        on_press: 
            root.manager.current = 'quiz2'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        id: option3
        font_style: 'H5'
        size_hint: (0.3,0.1)
        md_bg_color: 0,0,0,0.5
        radius: 30
        text: ''
        pos_hint: {'center_x': .3, 'center_y': .2}
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        on_press: 
            root.manager.current = 'quiz2'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        id: option4
        font_style: 'H5'
        size_hint: (0.3,0.1)
        md_bg_color: 0,0,0,0.5
        radius: 30
        text: ''
        pos_hint: {'center_x': .7, 'center_y': .2}  
        theme_text_color: 'Custom'
        text_color: 1,1,1,1 
        on_press: 
            root.manager.current = 'quiz2'
            root.manager.transition.direction = 'left'     
    MDProgressBar:
        id: progress
        value: 10
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x': .5, 'center_y': .1}
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
                                MDFillRoundFlatIconButton:
                                    icon: "home"
                                    text: "Home"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_press: 
                                        root.manager.current = 'main'
                                        root.manager.transition.direction = 'left'
                                MDFlatButton:
                                    text: ""
                                MDFillRoundFlatIconButton:
                                    icon: "account-circle"
                                    text: "Profile"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_press: 
                                        root.manager.current = 'profile'
                                        root.manager.transition.direction = 'left'
                                MDFlatButton:
                                    text: ""
                                MDFillRoundFlatIconButton:
                                    icon: "book"
                                    text: "Test"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_release: 
                                        root.manager.current = 'quiz'
                                        root.manager.transition.direction = 'left'
                                MDFlatButton:
                                    text: ""
                                MDFillRoundFlatIconButton:
                                    icon: "logout"
                                    text: "Logout"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_press: 
                                        root.manager.current = 'signup'
                                        root.manager.transition.direction = 'left'
<QuizScreen2>:       
    name: 'quiz2'
    MDLabel:
        text: 'Skill Quiz'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDLabel:
        id: question
        text: ''
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_y': .6}
    MDRaisedButton:
        id: option1
        font_style: 'H5'
        size_hint: (0.3,0.1)
        md_bg_color: 0,0,0,0.5
        radius: 30
        text: ''
        pos_hint: {'center_x': .3, 'center_y': .4}
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
    MDRaisedButton:
        id: option2
        font_style: 'H5'
        size_hint: (0.3,0.1)
        md_bg_color: 0,0,0,0.5
        radius: 30
        text: ''
        pos_hint: {'center_x': .7, 'center_y': .4}
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
    MDRaisedButton:
        id: option3
        font_style: 'H5'
        size_hint: (0.3,0.1)
        md_bg_color: 0,0,0,0.5
        radius: 30
        text: ''
        pos_hint: {'center_x': .3, 'center_y': .2}
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
    MDRaisedButton:
        id: option4
        font_style: 'H5'
        size_hint: (0.3,0.1)
        md_bg_color: 0,0,0,0.5
        radius: 30
        text: ''
        pos_hint: {'center_x': .7, 'center_y': .2}  
        theme_text_color: 'Custom'
        text_color: 1,1,1,1      
    MDProgressBar:
        id: progress
        value: 10
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x': .5, 'center_y': .1}
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
                                MDFillRoundFlatIconButton:
                                    icon: "home"
                                    text: "Home"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_press: 
                                        root.manager.current = 'main'
                                        root.manager.transition.direction = 'left'
                                MDFlatButton:
                                    text: ""
                                MDFillRoundFlatIconButton:
                                    icon: "account-circle"
                                    text: "Profile"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_press: 
                                        root.manager.current = 'profile'
                                        root.manager.transition.direction = 'left'
                                MDFlatButton:
                                    text: ""
                                MDFillRoundFlatIconButton:
                                    icon: "book"
                                    text: "Test"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_release: 
                                        root.manager.current = 'quiz'
                                        root.manager.transition.direction = 'left'
                                MDFlatButton:
                                    text: ""
                                MDFillRoundFlatIconButton:
                                    icon: "logout"
                                    text: "Logout"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_press: 
                                        root.manager.current = 'signup'
                                        root.manager.transition.direction = 'left'
<ProfileScreen>:
    name: 'profile'
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            MDScreen:
                size_hint_y: 1
                MDLabel:
                    text: 'My Profile'
                    font_style: 'H3'
                    halign: 'center'
                    pos_hint: {'center_x': .5, 'center_y': .8}
                MDCard:
                    size_hint: (0.45,0.25)
                    pos_hint: {'center_x': .5, 'center_y': .7}
                    radius: 30
                    Image:
                        source: 'people.jpg'
                        size_hint: (0.9, 1)
                        pos_hint: {'center_x': .5,'center_y': .5}
                        size: self.texture_size
                        halign: 'center'
                MDLabel:
                    text: 'Dhiraj Shelke'
                    font_style: 'H5'
                    halign: 'center'
                    pos_hint: {'center_x': .5, 'center_y': .5}
                MDLabel:
                    text: 'Status'
                    font_style: 'H4'
                    pos_hint: {'center_x': .6,'center_y': .4}
                Image:
                    source: 'Capture.jpg'
                    size_hint: (0.8, 0.8)
                    pos_hint: {'center_x': .5,'center_y': .2}
                    size: self.texture_size
                    halign: 'center'
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
                                MDFillRoundFlatIconButton:
                                    icon: "home"
                                    text: "Home"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_press: 
                                        root.manager.current = 'main'
                                        root.manager.transition.direction = 'left'
                                MDFlatButton:
                                    text: ""
                                MDFillRoundFlatIconButton:
                                    icon: "account-circle"
                                    text: "Profile"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_press: 
                                        root.manager.current = 'profile'
                                        root.manager.transition.direction = 'left'
                                MDFlatButton:
                                    text: ""
                                MDFillRoundFlatIconButton:
                                    icon: "book"
                                    text: "Test"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_release: 
                                        root.manager.current = 'quiz'
                                        root.manager.transition.direction = 'left'
                                MDFlatButton:
                                    text: ""
                                MDFillRoundFlatIconButton:
                                    icon: "logout"
                                    text: "Logout"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_press: 
                                        root.manager.current = 'signup'
                                        root.manager.transition.direction = 'left'
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
class QuizScreen1(Screen):
    pass
class QuizScreen2(Screen):
    pass
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(SignupScreen(name='signup'))
sm.add_widget(MainScreen(name='main'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(QuizScreen1(name='quiz1'))
sm.add_widget(QuizScreen2(name='quiz2'))
class MainApp(MDApp):
    def build(self):
        self.str = Builder.load_string(str)
        return self.str

    def on_start(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.theme_style = 'Dark'
    
    def quiz(self):
        self.str.get_screen('quiz1').ids.question.text = ques_ans[0]['question']
        self.str.get_screen('quiz1').ids.option1.text = ques_ans[0]['option1']
        self.str.get_screen('quiz1').ids.option2.text = ques_ans[0]['option2']
        self.str.get_screen('quiz1').ids.option3.text = ques_ans[0]['option3']
        self.str.get_screen('quiz1').ids.option4.text = ques_ans[0]['option4']
        self.str.get_screen('quiz2').ids.question.text = ques_ans[1]['question']
        self.str.get_screen('quiz2').ids.option1.text = ques_ans[1]['option1']
        self.str.get_screen('quiz2').ids.option2.text = ques_ans[1]['option2']
        self.str.get_screen('quiz2').ids.option3.text = ques_ans[1]['option3']
        self.str.get_screen('quiz2').ids.option4.text = ques_ans[1]['option4']

MainApp().run()
