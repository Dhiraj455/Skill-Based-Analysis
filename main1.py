#Hello World Page Using KivyMd
from tabnanny import check
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.storage.jsonstore import JsonStore
import json
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.uix.screenmanager import ScreenManager, Screen
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from kivy_garden.graph import Graph  
# from kivy.garden.matplotlib import FigureCanvasKivyAgg

Window.size = (450, 700)
ques_ans = {
    "skill":"Python",
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
        'answer': 'Interpreted'
    },
    2: {
        'question': 'Which of the following is not a reserved word in Python?',
        'option1': 'class',
        'option2': 'for',
        'option3': 'print',
        'option4': 'exec',
        'answer': 'exec'
    },
    3: {
        'question': 'Which of the following is not a valid identifier in Python?',
        'option1': '2names',
        'option2': '2_names',
        'option3': 'names2',
        'option4': 'None of the above',
        'answer': '2_names'
    },
    4: {
        'question':"Who developed Python Programming Language?",
        'option1': 'Guido Van Rossum',
        'option2': 'Dennis Ritchie',
        'option3': 'Linus Torvalds',
        'option4': 'James Gosling',
        'answer': 'Guido Van Rossum'
    },
    5: {
        'question':"Which of the following is the correct extension of the Python file?",
        'option1': '.py',
        'option2': '.pyc',
        'option3': '.pyo',
        'option4': '.pyw',
        'answer': '.py'
    },
    6: {
        'question':"Which of the following is the correct syntax to create a class named as Dog?",
        'option1': "class Dog:",
        'option2': "class = Dog",
        'option3': "class : Dog",
        'option4': "class := Dog",
        'answer': "class Dog:"
    },
    7: {
        'question':"Which type of Programming does Python support?",
        'option1': 'Object Oriented',
        'option2': 'Functional',
        'option3': 'Both of the above',
        'option4': 'None of the above',
        'answer': 'Both of the above'
    },
    8: {
        'question':"Which of the following is used to define a block of code in Python language?",
        'option1': 'Identation',
        'option2': 'Key',
        'option3': 'Brackets',
        'option4': '< >',
        'answer': 'Identation'
    },
    9: {
        'question':'What is a correct syntax to output "Hello World" in Python?',
        'option1': 'echo "Hello World"',
        'option2': 'print("Hello World")',
        'option3': 'echo("Hello World")',
        'option4': 'p("Hello World")',
        'answer': 'print("Hello World")'
    },
}
str1 = """
ScreenManager:
    WelcomeScreen:
    LoginScreen:
    SignupScreen:
    MainScreen:
    QuizScreen:
    QuizScreen1:
    QuizScreen2:
    QuizScreen3:
    QuizScreen4:
    QuizScreen5:
    QuizScreen6:
    QuizScreen7:
    QuizScreen8:
    QuizScreen9:
    QuizScreen10:
    ResultScreen:
    ProfileScreen:
    AnalysisScreen:
    HistoryScreen:

<WelcomeScreen>:
    name: 'welcome'
    MDLabel:
        text: 'Welcome to Career Analysis'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .7}
    MDRoundFlatButton:
        text: 'Login'
        pos_hint: {'center_x':.3,'center_y':.2}
        font_style: 'Subtitle1'
        on_press:
            root.manager.current = 'login'
            root.manager.transition.direction = 'left'
    MDRoundFlatButton:
        text: 'Signup'
        pos_hint: {'center_x':.7,'center_y':.2}
        font_style: 'Subtitle1'
        on_press:
            root.manager.current = 'signup'
            root.manager.transition.direction = 'right'

<SignupScreen>:
    name: 'signup'
    MDLabel:
        text: 'Signup'
        halign: 'center'
        font_style: 'H2'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDTextField:
        id: username_text_field
        hint_text: 'Username'
        pos_hint: {'center_x': .5, 'center_y': .7}
        size_hint: (0.7,0.1)
    MDTextField:
        id: email_text_field
        hint_text: 'Email'
        pos_hint: {'center_x': .5, 'center_y': .6}
        size_hint: (0.7,0.1)
    MDTextField:
        id: password_text_field
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
            app.store_username()
            root.manager.current = 'login'
            root.manager.transition.direction = 'down'
    MDRoundFlatButton:
        text: 'Back'
        pos_hint: {'center_x':.2,'center_y':.3}
        font_style: 'Subtitle1'
        on_press:
            root.manager.current = 'signup'
            root.manager.transition.direction = 'left'
    MDRoundFlatButton:
        text: 'Login'
        pos_hint: {'center_x':.8,'center_y':.3}
        font_style: 'Subtitle1'
        on_press:
            root.manager.current = 'login'
            root.manager.transition.direction = 'right'
<LoginScreen>:
    name: 'login'
    MDLabel:
        text: 'Login'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDTextField:
        id: username_text_field
        hint_text: 'Username'
        pos_hint: {'center_x': .5, 'center_y': .7}
        required: True
        size_hint: (0.7,0.1)
    MDTextField:
        id: password_text_field
        hint_text: 'Password'
        pos_hint: {'center_x': .5, 'center_y': .5}
        required: True
        size_hint: (0.7,0.1)
        password: True
    MDFloatingActionButton:
        icon: 'check'
        md_bg_color: app.theme_cls.primary_color
        user_font_size: '40sp'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_press: 
            app.check_username()
    MDFloatingActionButton:
        id: main_button
        icon: 'arrow-right'
        disabled: True
        md_bg_color: app.theme_cls.primary_color
        user_font_size: '40sp'
        pos_hint: {'center_x': .8, 'center_y': .2}
        on_press:
            root.manager.current = 'main'
            root.manager.transition.direction = 'right'
            app.check_login()
    MDRoundFlatButton:
        text: 'Signup'
        pos_hint: {'center_x':.2,'center_y':.2}
        font_style: 'Subtitle1'
        on_press:
            root.manager.current = 'signup'
            root.manager.transition.direction = 'right'
<MainScreen>:
    name: 'main'
    MDLabel:
        text: 'Career Analysis For Student'
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDLabel:
        text: 'Skills'
        font_style: 'H6'
        halign: 'center'
        pos_hint: {'center_x': .1, 'center_y': .7}
    MDCard:
        size_hint: (0.4,0.1)
        pos_hint: {'center_x': .25, 'center_y': .6}
        md_bg_color: 0,0,0,0.5
        radius: 10
        MDLabel:
            text: '    Python'
            font_style: 'H6'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            pos_hint: {'center_y': .5}
        MDIconButton:
            icon: 'plus'
            user_font_size: '40sp'
            pos_hint: {'center_x': .9, 'center_y': .5}
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            on_press:
                root.manager.current = 'quiz'
                root.manager.transition.direction = 'left'
                app.quiz('Python')
    MDCard:
        size_hint: (0.4,0.1)
        pos_hint: {'center_x': .75, 'center_y': .6}
        md_bg_color: 0,0,0,0.5
        radius: 10
        MDLabel:
            text: '   Java'
            font_style: 'H6'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            pos_hint: {'center_y': .5}
        MDIconButton:
            icon: 'plus'
            user_font_size: '40sp'
            pos_hint: {'center_x': .9, 'center_y': .5}
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            on_press:
                root.manager.current = 'quiz'
                root.manager.transition.direction = 'left'
                app.quiz("Java")
    MDCard:
        size_hint: (0.4,0.1)
        pos_hint: {'center_x': .25, 'center_y': .45}
        md_bg_color: 0,0,0,0.5
        radius: 10
        MDLabel:
            text: '   Javascript'
            font_style: 'H6'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            pos_hint: {'center_y': .5}
        MDIconButton:
            icon: 'plus'
            user_font_size: '40sp'
            pos_hint: {'center_x': .9, 'center_y': .5}
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            on_press:
                root.manager.current = 'quiz'
                root.manager.transition.direction = 'left'
                app.quiz('Javascript')
    MDCard:
        size_hint: (0.4,0.1)
        pos_hint: {'center_x': .75, 'center_y': .45}
        md_bg_color: 0,0,0,0.5
        radius: 10
        MDLabel:
            text: '   C++'
            font_style: 'H6'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            pos_hint: {'center_y': .5}
        MDIconButton:
            icon: 'plus'
            user_font_size: '40sp'
            pos_hint: {'center_x': .9, 'center_y': .5}
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            on_press:
                root.manager.current = 'quiz'
                root.manager.transition.direction = 'left'
                app.quiz('C++')
    MDCard:
        size_hint: (0.9,0.1)
        pos_hint: {'center_x': .5, 'center_y': .3}
        md_bg_color: 0,0,0,0.5
        radius: 10
        MDLabel:
            text: '   Graphic Design'
            font_style: 'H6'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            pos_hint: {'center_y': .5}
        MDIconButton:
            icon: 'plus'
            user_font_size: '40sp'
            pos_hint: {'center_x': .9, 'center_y': .5}
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            on_press:
                root.manager.current = 'quiz'
                root.manager.transition.direction = 'left'
                app.quiz('Graphic Design')
    MDCard:
        size_hint: (0.9,0.1)
        pos_hint: {'center_x': .5, 'center_y': .15}
        md_bg_color: 0,0,0,0.5
        radius: 10
        MDLabel:
            text: '   Web Development'
            font_style: 'H6'
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            pos_hint: {'center_y': .5}
        MDIconButton:
            icon: 'plus'
            user_font_size: '40sp'
            pos_hint: {'center_x': .9, 'center_y': .5}
            theme_text_color: 'Custom'
            text_color: 1,1,1,1
            on_press:
                root.manager.current = 'quiz'
                root.manager.transition.direction = 'left'
                app.quiz('Web Development')
    MDScreen:
        MDNavigationLayout:
            ScreenManager:
                MDScreen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Home'
                            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                            elevation:5
                        Widget:
            MDNavigationDrawer:
                id: nav_drawer
                ContentNavigationDrawer:
                    orientation: 'vertical'
                    theme_text_color: 'Custom'
                    text_color: 1,1,1,1
                    md_bg_color: 0,0,0,0.5
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
                                    icon: "history"
                                    text: "History"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_release: 
                                        root.manager.current = 'history'
                                        root.manager.transition.direction = 'left'
                                        app.show_history()
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
    MDFloatingActionButton:
        icon: 'account'
        md_bg_color: 1,0,1,1
        user_font_size: '50sp'
        pos_hint: {'center_x': .9, 'center_y': .915}
        on_press:
            root.manager.current = 'profile'
            root.manager.transition.direction = 'up' 

<HistoryScreen>:
    name: 'history'
    MDLabel:
        text: 'Recent Activities'
        font_style: 'H5'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        pos_hint: {'center_x': .5, 'center_y': .87}
    MDCard:
        id: status
        text : "4"
        size_hint: (0.9, 0.7)
        pos_hint: {'center_x': .5, 'center_y': .48}
    MDFloatingActionButton:
        icon: 'magnify'
        md_bg_color: app.theme_cls.primary_color
        user_font_size: '40sp'
        pos_hint: {'center_x': .9, 'center_y': .07}
        on_press:
            root.manager.current = 'analysis'
            root.manager.transition.direction = 'left'
            app.analysis()
    MDScreen:
        MDNavigationLayout:
            ScreenManager:
                MDScreen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'History'
                            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                            elevation:5
                        Widget:
            MDNavigationDrawer:
                id: nav_drawer
                ContentNavigationDrawer:
                    orientation: 'vertical'
                    theme_text_color: 'Custom'
                    text_color: 1,1,1,1
                    md_bg_color: 0,0,0,0.5
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
                                    icon: "history"
                                    text: "History"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_release: 
                                        root.manager.current = 'history'
                                        root.manager.transition.direction = 'left'
                                        app.show_history()
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
        pos_hint: {'center_y': .5}
    MDFlatButton:
        text: 'Start'
        pos_hint: {'center_x': .5, 'center_y': .4}
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
                            icon: "history"
                            text: "History"
                            font_style: "Subtitle1"
                            font_size: "20sp"
                            padding: "10dp"
                            on_release: 
                                root.manager.current = 'history'
                                root.manager.transition.direction = 'left'
                                app.show_history()
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
        font_style: 'H3'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDLabel:
        id: question
        text: ''
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDFillRoundFlatButton:
        id: option1
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .6}
        on_press: app.check1("quiz1")
    MDFillRoundFlatButton:
        id: option2
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .6}
        on_press: app.check2("quiz1")
    MDFillRoundFlatButton:
        id: option3
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .4}
        on_press: app.check3("quiz1")
    MDFillRoundFlatButton:
        id: option4
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .4}
        on_press: app.check4("quiz1")
    MDFlatButton:
        text: 'Next'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_press: 
            root.manager.current = 'quiz2'
            root.manager.transition.direction = 'left'
            app.next("quiz1")
    MDProgressBar:
        id: progress
        value: 10
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x': .5, 'center_y': .1}
<QuizScreen2>:       
    name: 'quiz2'
    MDLabel:
        text: 'Skill Quiz'
        font_style: 'H3'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDLabel:
        id: question
        text: ''
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDFillRoundFlatButton:
        id: option1
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .6}
        on_press: app.check1("quiz2")
    MDFillRoundFlatButton:
        id: option2
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .6}
        on_press: app.check2("quiz2")
    MDFillRoundFlatButton:
        id: option3
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .4}
        on_press: app.check3("quiz2")
    MDFillRoundFlatButton:
        id: option4
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .4}
        on_press: app.check4("quiz2")
    MDFlatButton:
        text: 'Next'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_press: 
            root.manager.current = 'quiz3'
            root.manager.transition.direction = 'left'
            app.next("quiz2")
    MDProgressBar:
        id: progress
        value: 20
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x': .5, 'center_y': .1}
<QuizScreen3>:       
    name: 'quiz3'
    MDLabel:
        text: 'Skill Quiz'
        font_style: 'H3'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDLabel:
        id: question
        text: ''
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDFillRoundFlatButton:
        id: option1
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .6}
        on_press: app.check1("quiz3")
    MDFillRoundFlatButton:
        id: option2
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .6}
        on_press: app.check2("quiz3")
    MDFillRoundFlatButton:
        id: option3
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .4}
        on_press: app.check3("quiz3")
    MDFillRoundFlatButton:
        id: option4
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .4}
        on_press: app.check4("quiz3")
    MDFlatButton:
        text: 'Next'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_press: 
            root.manager.current = 'quiz4'
            root.manager.transition.direction = 'left'
            app.next("quiz3")
    MDProgressBar:
        id: progress
        value: 30
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x': .5, 'center_y': .1}
<QuizScreen4>:       
    name: 'quiz4'
    MDLabel:
        text: 'Skill Quiz'
        font_style: 'H3'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDLabel:
        id: question
        text: ''
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDFillRoundFlatButton:
        id: option1
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .6}
        on_press: app.check1("quiz4")
    MDFillRoundFlatButton:
        id: option2
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .6}
        on_press: app.check2("quiz4")
    MDFillRoundFlatButton:
        id: option3
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .4}
        on_press: app.check3("quiz4")
    MDFillRoundFlatButton:
        id: option4
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .4}
        on_press: app.check4("quiz4")
    MDFlatButton:
        text: 'Next'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_press: 
            root.manager.current = 'quiz5'
            root.manager.transition.direction = 'left'
            app.next("quiz4")
    MDProgressBar:
        id: progress
        value: 40
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x': .5, 'center_y': .1}
<QuizScreen5>:       
    name: 'quiz5'
    MDLabel:
        text: 'Skill Quiz'
        font_style: 'H3'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDLabel:
        id: question
        text: ''
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDFillRoundFlatButton:
        id: option1
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .6}
        on_press: app.check1("quiz5")
    MDFillRoundFlatButton:
        id: option2
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .6}
        on_press: app.check2("quiz5")
    MDFillRoundFlatButton:
        id: option3
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .4}
        on_press: app.check3("quiz5")
    MDFillRoundFlatButton:
        id: option4
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .4}
        on_press: app.check4("quiz5")
    MDFlatButton:
        text: 'Next'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_press: 
            root.manager.current = 'quiz6'
            root.manager.transition.direction = 'left'
            app.next("quiz5")
    MDProgressBar:
        id: progress
        value: 50
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x': .5, 'center_y': .1}
<QuizScreen6>:       
    name: 'quiz6'
    MDLabel:
        text: 'Skill Quiz'
        font_style: 'H3'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDLabel:
        id: question
        text: ''
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDFillRoundFlatButton:
        id: option1
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .6}
        on_press: app.check1("quiz6")
    MDFillRoundFlatButton:
        id: option2
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .6}
        on_press: app.check2("quiz6")
    MDFillRoundFlatButton:
        id: option3
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .4}
        on_press: app.check3("quiz6")
    MDFillRoundFlatButton:
        id: option4
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .4}
        on_press: app.check4("quiz6")
    MDFlatButton:
        text: 'Next'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_press: 
            root.manager.current = 'quiz7'
            root.manager.transition.direction = 'left'
            app.next("quiz6")
    MDProgressBar:
        id: progress
        value: 60
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x': .5, 'center_y': .1}
<QuizScreen7>:       
    name: 'quiz7'
    MDLabel:
        text: 'Skill Quiz'
        font_style: 'H3'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDLabel:
        id: question
        text: ''
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDFillRoundFlatButton:
        id: option1
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .6}
        on_press: app.check1("quiz7")
    MDFillRoundFlatButton:
        id: option2
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .6}
        on_press: app.check2("quiz7")
    MDFillRoundFlatButton:
        id: option3
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .4}
        on_press: app.check3("quiz7")
    MDFillRoundFlatButton:
        id: option4
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .4}
        on_press: app.check4("quiz7")
    MDFlatButton:
        text: 'Next'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_press: 
            root.manager.current = 'quiz8'
            root.manager.transition.direction = 'left'
            app.next("quiz7")
    MDProgressBar:
        id: progress
        value: 70
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x': .5, 'center_y': .1}
<QuizScreen8>:       
    name: 'quiz8'
    MDLabel:
        text: 'Skill Quiz'
        font_style: 'H3'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDLabel:
        id: question
        text: ''
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDFillRoundFlatButton:
        id: option1
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .6}
        on_press: app.check1("quiz8")
    MDFillRoundFlatButton:
        id: option2
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .6}
        on_press: app.check2("quiz8")
    MDFillRoundFlatButton:
        id: option3
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .4}
        on_press: app.check3("quiz8")
    MDFillRoundFlatButton:
        id: option4
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .4}
        on_press: app.check4("quiz8")
    MDFlatButton:
        text: 'Next'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_press: 
            root.manager.current = 'quiz9'
            root.manager.transition.direction = 'left'
            app.next("quiz8")
    MDProgressBar:
        id: progress
        value: 80
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x': .5, 'center_y': .1}
<QuizScreen9>:       
    name: 'quiz9'
    MDLabel:
        text: 'Skill Quiz'
        font_style: 'H3'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDLabel:
        id: question
        text: ''
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDFillRoundFlatButton:
        id: option1
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .6}
        on_press: app.check1("quiz9")
    MDFillRoundFlatButton:
        id: option2
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .6}
        on_press: app.check2("quiz9")
    MDFillRoundFlatButton:
        id: option3
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .4}
        on_press: app.check3("quiz9")
    MDFillRoundFlatButton:
        id: option4
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .4}
        on_press: app.check4("quiz9")
    MDFlatButton:
        text: 'Next'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_press: 
            root.manager.current = 'quiz10'
            root.manager.transition.direction = 'left'
            app.next("quiz9")
    MDProgressBar:
        id: progress
        value: 90
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x': .5, 'center_y': .1}
<QuizScreen10>:       
    name: 'quiz10'
    MDLabel:
        text: 'Skill Quiz'
        font_style: 'H3'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .9}
    MDLabel:
        id: question
        text: ''
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDFillRoundFlatButton:
        id: option1
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .6}
        on_press: app.check1("quiz10")
    MDFillRoundFlatButton:
        id: option2
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .6}
        on_press: app.check2("quiz10")
    MDFillRoundFlatButton:
        id: option3
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .3, 'center_y': .4}
        on_press: app.check3("quiz10")
    MDFillRoundFlatButton:
        id: option4
        text: ''
        font_style: 'H6'
        size_hint: (0.4,0.1)
        radius: 30
        md_bg_color: 0, 0, 1, 0
        theme_text_color: 'Primary'
        pos_hint: {'center_x': .7, 'center_y': .4}
        on_press: app.check4("quiz10")
    MDFlatButton:
        text: 'Next'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_press: 
            root.manager.current = 'result'
            root.manager.transition.direction = 'left'
            app.next("quiz10")
            app.result()
    MDProgressBar:
        id: progress
        value: 100
        size_hint: (0.7, 0.05)
        pos_hint: {'center_x': .5, 'center_y': .1}
<ResultScreen>:
    name: 'result'
    MDLabel:
        text: 'Skill Quiz'
        font_style: 'H3'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .8}
    MDLabel:
        id: result
        text: ''
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .6}
    MDFlatButton:
        text: 'Home'
        pos_hint: {'center_x': .5, 'center_y': .2}
        on_press:
            root.manager.current = 'main'
            root.manager.transition.direction = 'right'
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
                    pos_hint: {'center_x': .5, 'center_y': .85}
                MDLabel:
                    id: name
                    text: ''
                    font_style: 'H5'
                    halign: 'center'
                    pos_hint: {'center_x': .5, 'center_y': .75}
                MDLabel:
                    id: email
                    text: ''
                    font_style: 'H5'
                    halign: 'center'
                    pos_hint: {'center_x': .5, 'center_y': .7}
                MDLabel:
                    text: 'Status'
                    font_style: 'H4'
                    pos_hint: {'center_x': .6,'center_y': .6}
                MDCard:
                    id: status
                    text : "4"
                    size_hint: (0.9, 0.4)
                    pos_hint: {'center_x': .5, 'center_y': .35}
                MDFloatingActionButton:
                    icon: 'magnify'
                    md_bg_color: app.theme_cls.primary_color
                    user_font_size: '40sp'
                    pos_hint: {'center_x': .9, 'center_y': .07}
                    on_press:
                        root.manager.current = 'analysis'
                        root.manager.transition.direction = 'left'
                        app.analysis()
    MDScreen:
        MDNavigationLayout:
            ScreenManager:
                MDScreen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Profile'
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
                                    icon: "history"
                                    text: "History"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_release: 
                                        root.manager.current = 'history'
                                        root.manager.transition.direction = 'left'
                                        app.show_history()
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
<AnalysisScreen>:
    name: 'analysis'
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            MDScreen:
                size_hint_y: 1
                MDLabel:
                    text: 'Analysis'
                    font_style: 'H3'
                    halign: 'center'
                    pos_hint: {'center_x': .5, 'center_y': .85}
                MDCard:
                    id: analysis
                    size_hint: (0.9, 0.37)
                    pos_hint: {'center_x': .5, 'center_y': .55}
    MDScreen:
        MDNavigationLayout:
            ScreenManager:
                MDScreen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Analysis'
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
                                    icon: "history"
                                    text: "History"
                                    font_style: "Subtitle1"
                                    font_size: "20sp"
                                    padding: "10dp"
                                    on_release: 
                                        root.manager.current = 'history'
                                        root.manager.transition.direction = 'left'
                                        app.show_history()
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
class QuizScreen3(Screen):
    pass
class QuizScreen4(Screen):
    pass
class QuizScreen5(Screen):
    pass
class QuizScreen6(Screen):
    pass
class QuizScreen7(Screen):
    pass
class QuizScreen8(Screen):
    pass
class QuizScreen9(Screen):
    pass
class QuizScreen10(Screen):
    pass
class ResultScreen(Screen):
    pass
class AnalysisScreen(Screen):
    pass
class HistoryScreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(SignupScreen(name='signup'))
sm.add_widget(MainScreen(name='main'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(QuizScreen1(name='quiz1'))
sm.add_widget(QuizScreen2(name='quiz2'))
sm.add_widget(QuizScreen3(name='quiz3'))
sm.add_widget(QuizScreen4(name='quiz4'))
sm.add_widget(QuizScreen5(name='quiz5'))
sm.add_widget(QuizScreen6(name='quiz6'))
sm.add_widget(QuizScreen7(name='quiz7'))
sm.add_widget(QuizScreen8(name='quiz8'))
sm.add_widget(QuizScreen9(name='quiz9'))
sm.add_widget(QuizScreen10(name='quiz10'))
sm.add_widget(ResultScreen(name='result'))
sm.add_widget(AnalysisScreen(name='analysis'))
sm.add_widget(HistoryScreen(name='history'))
class MainApp(MDApp):
    def build(self):
        self.str1 = Builder.load_string(str1)
        return self.str1

    def on_start(self):
        self.store = JsonStore('user.json')
        f = open('user.json','r')
        x = json.load(f)
        # self.theme_cls.theme_style = "Dark"
        # self.str1.get_screen('profile').manager.current = 'profile'
        try:
            if x != {}:
                self.str1.get_screen('login').manager.current = 'login'
            
        except KeyError:
            self.str1.get_screen('welcome').manager.current = 'welcome'
    def analysis(self):
        f = open('user.json','r+')
        x = json.load(f)
        length = len(x)
        self.username = self.str1.get_screen('login').ids.username_text_field.text
        self.password_text = self.str1.get_screen('login').ids.password_text_field.text
        for i in range(0,length):
            if x[f'Userinfo{i}']['name'] == self.username and x[f'Userinfo{i}']['password'] == self.password_text:
                df = pd.read_csv(f'./Data/UserData/user{i}.csv',usecols=["Skill","Score"])
                print(df["Skill"])
                l = len(df["Skill"])
                print(l)
                sum = 0
                skill = []
                score = []
                for i in range(0,l):
                    if skill.__contains__(df.iloc[i]["Skill"]):
                            continue
                    else:
                        print(skill)
                        skill.append(df.iloc[i]["Skill"])
                print(skill)
                for i in skill:
                    for j in range(0,l):
                        if i == df.iloc[j]["Skill"]:
                            sum += df.iloc[j]["Score"]
                    score.append(sum)
                    sum = 0
                print(score)
                df1 = pd.DataFrame({"Skill":skill,"Score":score})
                print(df1)
                x = np.array(df1["Skill"])
                y = np.array(df1["Score"])
                plt.pie(y, labels = x)
                plt.show()
                # plt.plot(df.Skill, df.Score)
                # plt.show()
                # self.str1.get_screen('analysis').ids.analysis.add_widget(FigureCanvasTkAgg(plt.gcf()))

    def check_login(self):
        f = open('user.json','r')
        x = json.load(f)
        length = len(x)
        self.username_text = self.str1.get_screen('login').ids.username_text_field.text
        self.password_text = self.str1.get_screen('login').ids.password_text_field.text
        for i in range(0,length):
            if x[f'Userinfo{i}']['name'] == self.username_text and x[f'Userinfo{i}']['password'] == self.password_text:
                self.str1.get_screen('login').manager.current = 'main'
                self.str1.get_screen('main').manager.current = 'main'
                self.str1.get_screen('main').manager.transition.direction = 'left'
                self.username_changer()
                break
            else:
                # cancel = MDFlatButton(text='Cancel',on_press = self.close_username_dialogue)
                # self.dialog = MDDialog(title = 'Wrong Username or Password',text = 'Please try again',size_hint = (0.8,0.3),buttons = [cancel])
                # self.dialog.open()
                self.str1.get_screen('login').manager.current = 'login'
                print("User Not Found")
                pass

    def check_username(self):
        f = open('user.json','r')
        x = json.load(f)
        length = len(x)
        self.username = self.str1.get_screen('login').ids.username_text_field.text
        self.password_text = self.str1.get_screen('login').ids.password_text_field.text
        for i in range(0,length):
            if x[f'Userinfo{i}']['name'] == self.username and x[f'Userinfo{i}']['password'] == self.password_text:
                self.str1.get_screen('login').ids.main_button.disabled = False
            else:
                # cancel_btn_username_dialogue = MDFlatButton(text="Retry", on_release=self.close_username_dialogue)
                # self.dialog = MDDialog(title="Invalid Username", text="Wrong Username Please Try Again !!", size_hint=(0.8, 0.3), buttons=[cancel_btn_username_dialogue])
                # self.dialog.open()
                self.str1.get_screen('login').manager.current = 'login'
                print("User Not Found")
                pass
    
    def close_username_dialogue(self,obj):
        self.dialog.dismiss()

    def store_username(self):
        f = open('user.json','r+')
        self.store1 = JsonStore('id.json')
        x = json.load(f)
        id = self.store1.get('id')["id"]
        self.username_text = self.str1.get_screen('signup').ids.username_text_field.text
        self.password = self.str1.get_screen('signup').ids.password_text_field.text
        self.email = self.str1.get_screen('signup').ids.email_text_field.text
        if x == {}:
            self.store.put('Userinfo0',id=id-1,name=self.username_text, password=self.password, email=self.email)
            with open("./Data/UserData/user0.csv",'w+') as f1:
                    writer1 = csv.writer(f1)
                    writer1.writerow(["UserID","Name","Skill","Score"])
                    f1.close()
        else:
            self.store.put(f'Userinfo{id}',id=id ,name=self.username_text,email= self.email, password= self.password)
            with open("./Data/UserData/user"+str(id)+".csv",'w+') as f1:
                    writer1 = csv.writer(f1)
                    writer1.writerow(["UserID","Name","Skill","Score"])
                    f1.close()
            id += 1
            self.store1.put('id',id=id)
        self.username_changer()
    
    def username_changer(self):
        f = open('user.json','r+')
        x = json.load(f)
        length = len(x)
        self.username = self.str1.get_screen('login').ids.username_text_field.text
        self.password_text = self.str1.get_screen('login').ids.password_text_field.text
        main_list = []
        for i in range(0,length):
            if x[f'Userinfo{i}']['name'] == self.username and x[f'Userinfo{i}']['password'] == self.password_text:
                self.email = x[f'Userinfo{i}']['email']
                self.str1.get_screen('profile').ids.name.text = self.username
                self.str1.get_screen('profile').ids.email.text = self.email
                df = pd.read_csv(f'./Data/UserData/user{i}.csv',usecols=["Skill","Score"])
                size = len(df)
                for j in range(0,size):
                    main_list.append([df.iloc[j]["Skill"],df.iloc[j]["Score"]])
                # self.str1.get_screen('profile').ids.status.Fi
                break
            else:
                pass
        self.data_tables = MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            column_data=[
                ("Skill", dp(30)),
                ("Score", dp(30)),
            ],
            row_data = main_list,
            elevation = 4,)
        if self.str1.get_screen('profile').ids.status.text == "":
            self.str1.get_screen('profile').ids.status.add_widget(self.data_tables)
        else:
            self.str1.get_screen('profile').ids.status.clear_widgets()
            self.str1.get_screen('profile').ids.status.add_widget(self.data_tables)
    
    def show_history(self):
        f = open('user.json','r+')
        x = json.load(f)
        length = len(x)
        self.username = self.str1.get_screen('login').ids.username_text_field.text
        self.password_text = self.str1.get_screen('login').ids.password_text_field.text
        main_list = []
        for i in range(0,length):
            if x[f'Userinfo{i}']['name'] == self.username and x[f'Userinfo{i}']['password'] == self.password_text:
                self.email = x[f'Userinfo{i}']['email']
                self.str1.get_screen('profile').ids.name.text = self.username
                self.str1.get_screen('profile').ids.email.text = self.email
                df = pd.read_csv(f'./Data/UserData/user{i}.csv',usecols=["Skill","Score"])
                size = len(df)
                for j in range(0,size):
                    main_list.append([df.iloc[j]["Skill"],df.iloc[j]["Score"]])
                # self.str1.get_screen('profile').ids.status.Fi
                break
            else:
                pass
        self.data_tables = MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            rows_num = 10,
            column_data=[
                ("Skill", dp(30)),
                ("Score", dp(30)),
            ],
            row_data = main_list,
            elevation = 4,)
        print(main_list)
        if self.str1.get_screen('history').ids.status.text == "":
            self.str1.get_screen('history').ids.status.add_widget(self.data_tables)
        else:
            self.str1.get_screen('history').ids.status.clear_widgets()
            self.str1.get_screen('history').ids.status.add_widget(self.data_tables)
    
    def check1(self,x):
        print("You Clicked")
        print(x)
        self.str1.get_screen(x).ids.option1.md_bg_color = (0,0,1,1)
        self.str1.get_screen(x).ids.option1.theme_text_color = 'Custom'  
        self.str1.get_screen(x).ids.option2.md_bg_color = (0,0,1,0)
        self.str1.get_screen(x).ids.option2.theme_text_color = 'Primary' 
        self.str1.get_screen(x).ids.option3.md_bg_color = (0,0,1,0)
        self.str1.get_screen(x).ids.option3.theme_text_color = 'Primary' 
        self.str1.get_screen(x).ids.option4.md_bg_color = (0,0,1,0)
        self.str1.get_screen(x).ids.option4.theme_text_color = 'Primary' 
    
    def check2(self,x):
        print("You Clicked")
        print(x)
        self.str1.get_screen(x).ids.option2.md_bg_color = (0,0,1,1)
        self.str1.get_screen(x).ids.option2.theme_text_color = 'Custom'  
        self.str1.get_screen(x).ids.option1.md_bg_color = (0,0,1,0)
        self.str1.get_screen(x).ids.option1.theme_text_color = 'Primary' 
        self.str1.get_screen(x).ids.option3.md_bg_color = (0,0,1,0)
        self.str1.get_screen(x).ids.option3.theme_text_color = 'Primary' 
        self.str1.get_screen(x).ids.option4.md_bg_color = (0,0,1,0)
        self.str1.get_screen(x).ids.option4.theme_text_color = 'Primary' 
    
    def check3(self,x):
        print("You Clicked")
        print(x)
        self.str1.get_screen(x).ids.option3.md_bg_color = (0,0,1,1)
        self.str1.get_screen(x).ids.option3.theme_text_color = 'Custom'  
        self.str1.get_screen(x).ids.option2.md_bg_color = (0,0,1,0)
        self.str1.get_screen(x).ids.option2.theme_text_color = 'Primary' 
        self.str1.get_screen(x).ids.option1.md_bg_color = (0,0,1,0)
        self.str1.get_screen(x).ids.option1.theme_text_color = 'Primary' 
        self.str1.get_screen(x).ids.option4.md_bg_color = (0,0,1,0)
        self.str1.get_screen(x).ids.option4.theme_text_color = 'Primary' 
    
    def check4(self,x):
        print("You Clicked")
        print(x)
        self.str1.get_screen(x).ids.option4.md_bg_color = (0,0,1,1)
        self.str1.get_screen(x).ids.option4.theme_text_color = 'Custom'  
        self.str1.get_screen(x).ids.option2.md_bg_color = (0,0,1,0)
        self.str1.get_screen(x).ids.option2.theme_text_color = 'Primary' 
        self.str1.get_screen(x).ids.option3.md_bg_color = (0,0,1,0)
        self.str1.get_screen(x).ids.option3.theme_text_color = 'Primary' 
        self.str1.get_screen(x).ids.option1.md_bg_color = (0,0,1,0)
        self.str1.get_screen(x).ids.option1.theme_text_color = 'Primary'  

    def quiz(self,skill):
        if skill == "Python":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
        elif skill == "Java":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
        elif skill == "C++":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
        elif skill == "Graphic Design":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
        elif skill == "Web Development":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
        elif skill == "Javascript":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
        else:
            cancel_btn_username_dialogue = MDFlatButton(text="Retry", on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title="No Skill", text="There Are No Skill Selected", size_hint=(0.8, 0.3), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
            self.str1.get_screen('main').manager.current = 'main'
            pass
        x = len(df)
        for i in range(0,x):
            self.str1.get_screen(f'quiz{i+1}').ids.question.text = df.iloc[i]['question']
            self.str1.get_screen(f'quiz{i+1}').ids.option1.text = df.iloc[i]['option1']
            self.str1.get_screen(f'quiz{i+1}').ids.option2.text = df.iloc[i]['option2']
            self.str1.get_screen(f'quiz{i+1}').ids.option3.text = df.iloc[i]['option3']
            self.str1.get_screen(f'quiz{i+1}').ids.option4.text = df.iloc[i]['option4']

    def next(self,sc):
        self.store1 = JsonStore('id.json')
        score = self.store1.get('score')["score"]
        x = self.str1.get_screen(sc).ids
        df = pd.read_csv('./Data/Questions/quiz1.csv')
        if x.option1.md_bg_color == [0,0,1,1]:
            if x.option1.text ==  df.iloc[int(sc[-1])-1]['answer']:
                score += 2
                self.store1.put('score',score=score)
                print(score)
            else:
                pass
        elif x.option2.md_bg_color == [0,0,1,1]:
            if x.option2.text ==  df.iloc[int(sc[-1])-1]['answer']:
                score += 2
                self.store1.put('score',score=score)
                print(score)
            else:
                pass
        elif x.option3.md_bg_color == [0,0,1,1]:
            if x.option3.text ==  df.iloc[int(sc[-1])-1]['answer']:
                score += 2
                self.store1.put('score',score=score)
                print(score)
            else:
                pass
        elif x.option4.md_bg_color == [0,0,1,1]:
            if x.option4.text ==  df.iloc[int(sc[-1])-1]['answer']:
                score += 2
                self.store1.put('score',score=score)
                print(score)
            else:
                pass
        else:
            print(score)

    def store_data(self,skill,score):
        f = open('user.json','r')
        x = json.load(f)
        length = len(x)
        self.username_text = self.str1.get_screen('login').ids.username_text_field.text
        self.password_text = self.str1.get_screen('login').ids.password_text_field.text
        for i in range(0,length):
            if x[f'Userinfo{i}']['name'] == self.username_text and x[f'Userinfo{i}']['password'] == self.password_text:
                with open('./Data/UserData/user'+str(x[f'Userinfo{i}']["id"])+".csv",'a+') as f1:
                    writer1 = csv.writer(f1)
                    writer1.writerow([x[f'Userinfo{i}']["id"],x[f'Userinfo{i}']["name"],skill,score])
                    f1.close()
                break
    def result(self):
        x = self.store1.get('score')["score"]
        self.str1.get_screen('result').ids.result.text = ""+str(x)+"/20"
        self.store_data(ques_ans["skill"],str(x))
        x*=0
        self.store1.put('score',score=x)

MainApp().run()