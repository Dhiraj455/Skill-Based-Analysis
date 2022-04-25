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
from backend_kivy import FigureCanvasKivy
# from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

Window.size = (450, 700)
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
        self.str1 = Builder.load_file('file2.kv')
        return self.str1

    def on_start(self):
        self.store = JsonStore('user.json')
        f = open('user.json','r')
        x = json.load(f)
        # self.theme_cls.theme_style = "Dark"
        self.str1.get_screen('welcome').manager.current = 'welcome'
        # self.str1.get_screen('profile').manager.current = 'profile'
    
    def analysis(self):
        f = open('user.json','r+')
        x = json.load(f)
        length = len(x)
        self.username = self.str1.get_screen('login').ids.username_text_field.text
        self.password_text = self.str1.get_screen('login').ids.password_text_field.text
        try: 
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
                    res = dict(zip(skill, score))
                    x = max(res.values())
                    y = min(res.values())
                    for i in res:
                        if res[i] == x:
                            self.str1.get_screen('analysis').ids.strong.text = i
                        elif res[i] == y:
                            self.str1.get_screen('analysis').ids.weak.text = i
                    print(score)
                    df1 = pd.DataFrame({"Skill":skill,"Score":score})
                    print(df1)
                    x = np.array(df1["Skill"])
                    y = np.array(df1["Score"])
                    plt.bar(x,y)
                    # plt.show()
                    # plt.plot(df.Skill, df.Score)
                    # plt.show()
                    if self.str1.get_screen('analysis').ids.analysis.text == "":
                        self.str1.get_screen('analysis').ids.analysis.add_widget(FigureCanvasKivy(plt.gcf()))
                        self.str1.get_screen('analysis').ids.analysis.text = "1"
                    else:
                        self.str1.get_screen('analysis').ids.analysis.clear_widgets()
                        self.str1.get_screen('analysis').ids.analysis.add_widget(FigureCanvasKivy(plt.gcf()))
        except:
            pass
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
                self.str1.get_screen('login').manager.current = 'login'
                print("User Not Found")
                pass
        self.str1.get_screen('login').ids.main_button.disabled = True

    def check_username(self):
        f = open('user.json','r')
        x = json.load(f)
        length = len(x)
        user_check = False
        self.username = self.str1.get_screen('login').ids.username_text_field.text
        self.password_text = self.str1.get_screen('login').ids.password_text_field.text
        if self.username == '' or self.password_text == '':
            self.dialogpop(True,True)
        else:
            for i in range(0,length):
                if x[f'Userinfo{i}']['name'] == self.username and x[f'Userinfo{i}']['password'] == self.password_text:
                    self.str1.get_screen('login').ids.main_button.disabled = False
                    user_check = True
                else:
                    self.str1.get_screen('login').manager.current = 'login'
                    print("User Not Found")
                    pass
        self.dialogpop(False,user_check)

    def dialogpop(self,login,user):
        if login == True and user == False:
            cancel_btn_username_dialogue = MDFlatButton(text="Retry", on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title="Invalid Username", text="Wrong Username Please Try Again !!", size_hint=(0.8, 0.3), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
            pass
        # elif login == False and user == True:
        #     cancel = MDFlatButton(text='Cancel',on_press = self.close_username_dialogue)
        #     self.dialog = MDDialog(title = 'Invalid Username',text = 'Wrong Username Please Try Again !!',size_hint = (0.8,0.3),buttons = [cancel])
        #     self.dialog.open()
        #     pass
        elif login == True and user == True:
            cancel = MDFlatButton(text='Cancel',on_press = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Invalid Credential',text = 'Please Put Correct Credential',size_hint = (0.8,0.3),buttons = [cancel])
            self.dialog.open()
            pass
        else:
            print("Wrong")
    
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
        if self.username_text == '' or self.password == '' or self.email == '':
            self.dialogpop(True,True)
            self.str1.get_screen('signup').manager.current = 'signup'
            pass
        elif x == {}:
            self.store.put('Userinfo0',id=id-1,name=self.username_text, password=self.password, email=self.email)
            with open("./Data/UserData/user0.csv",'w+') as f1:
                    writer1 = csv.writer(f1)
                    writer1.writerow(["UserID","Name","Skill","Score"])
                    f1.close()
            self.str1.get_screen('signup').manager.current = 'login'
            self.str1.get_screen('signup').transition.direction = 'left'
        else:
            self.store.put(f'Userinfo{id}',id=id ,name=self.username_text,email= self.email, password= self.password)
            with open("./Data/UserData/user"+str(id)+".csv",'w+') as f1:
                    writer1 = csv.writer(f1)
                    writer1.writerow(["UserID","Name","Skill","Score"])
                    f1.close()
            self.str1.get_screen('signup').manager.current = 'login'
            self.str1.get_screen('signup').manager.transition.direction = 'left'
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
            pagination_menu_pos = 'auto',
            column_data=[
                ("Skill", dp(30)),
                ("Score", dp(30)),
            ],
            row_data = main_list,
            elevation = 4,)
        if self.str1.get_screen('profile').ids.status.text == "":
            self.str1.get_screen('profile').ids.status.add_widget(self.data_tables)
            self.str1.get_screen('history').ids.status.text="1"
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
            pagination_menu_pos = 'auto',
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
            self.str1.get_screen('history').ids.status.text = "1"
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
        self.store1 = JsonStore('id.json')
        if skill == "Python":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
            self.store1.put('skill',skill=skill)
        elif skill == "Java":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
            self.store1.put('skill',skill=skill)
        elif skill == "C++":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
            self.store1.put('skill',skill=skill)
        elif skill == "Graphic Design":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
            self.store1.put('skill',skill=skill)
        elif skill == "Web Development":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
            self.store1.put('skill',skill=skill)
        elif skill == "Javascript":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
            self.store1.put('skill',skill=skill)
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
        if self.store1["skill"]["skill"] == "Python":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
        elif self.store1["skill"]["skill"] == "Java":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
        elif self.store1["skill"]["skill"] == "C++":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
        elif self.store1["skill"]["skill"] == "Graphic Design":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
        elif self.store1["skill"]["skill"] == "Web Development":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
        elif self.store1["skill"]["skill"] == "Javascript":
            df = pd.read_csv('./Data/Questions/quiz1.csv')
        else:
            pass                                               
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
        self.store1 = JsonStore('id.json')
        skill = self.store1.get('skill')["skill"]
        x = self.store1.get('score')["score"]
        self.str1.get_screen('result').ids.result.text = ""+str(x)+"/20"
        self.store_data(skill,str(x))
        x*=0
        self.store1.put('score',score=x)
        self.username_changer()

MainApp().run()