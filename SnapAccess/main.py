from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.settings import SettingsWithSidebar
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.config import Config
from os.path import join
import time
import sys
import subprocess
from kivy.properties import StringProperty
import os


# json files store passwords, switch info and added directory/paths
data_dir = App().user_data_dir
store = JsonStore(join(data_dir,'SnapAccess-password.json'))
store1 = JsonStore(join(data_dir,'SnapAccess-info.json'))



class MainWindow(Screen):
    password = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        Window.bind(on_key_down=self._on_keyboard_down)

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if sm.current == 'login' and keycode == 40:  # 40 - Enter key pressed
            self.login()

# function to check the password is correct
    def login(self):
        if 'password' in store:
            if self.password.text == store.get('password')['password_text']:
                sm.current = "main"
                self.reset()
            else:
                invalid_password()
                self.reset()
        else:
            # Handle the case when the 'password' key does not exist in the JsonStore
            sm.current = "main"

    def reset(self):
        self.password.text = ""

    # forgot password popup
    def forgot_pas(self):
        pop = Popup(title='Forgotten Password',
                    content=Label(text="If you can't remember \nyour password\n"
                                       "\nuninstall and reinstall \nthe app "),
                    size_hint=(None, None), size=(250, 200),
                    separator_color=(1, 0, 0, 1))
        pop.open()



class SecondWindow(Screen):
    try:
        change_name1 = store1.get('name1')['program_name']
        program_1_name = StringProperty(change_name1)
    except KeyError:
        program_1_name = StringProperty('program 1')

    try:
        change_name2 = store1.get('name2')['program_name']
        program_2_name = StringProperty(change_name2)
    except KeyError:
        program_2_name = StringProperty('program 2')

    try:
        change_name3 = store1.get('name3')['program_name']
        program_3_name = StringProperty(change_name3)
    except KeyError:
        program_3_name = StringProperty('program 3')

    try:
        change_name4 = store1.get('name4')['program_name']
        program_4_name = StringProperty(change_name4)
    except KeyError:
        program_4_name = StringProperty('program 4')



    def open_program_1(self):
        """Open program 1"""
        program1 = []

        program_numbers = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
        program_names = ['program_one', 'program_two', 'program_three', 'program_four',
                         'program_five', 'program_six', 'program_seven', 'program_eight',
                         'program_nine', 'program_ten']

        for number, name in zip(program_numbers, program_names):
            program_key = 'program' + number
            if program_key in store1 and name in store1[program_key]:
                program1.append(store1[program_key][name])

        self.open_programs(program1)  # Call method



    def open_program_2(self):
        """Open program 2"""
        program2 = []

        program_numbers = ['11', '21', '31', '41', '51', '61', '71', '81', '91', '110']
        program_names = ['program_one', 'program_two', 'program_three', 'program_four',
                         'program_five', 'program_six', 'program_seven', 'program_eight',
                         'program_nine', 'program_ten']

        for number, name in zip(program_numbers, program_names):
            program_key = 'program' + number
            if program_key in store1 and name in store1[program_key]:
                program2.append(store1[program_key][name])

        self.open_programs(program2)  # Call method to open programs



    def open_program_3(self):
        """Open program 3"""
        program3 = []

        program_numbers = ['12', '22', '32', '42', '52', '62', '72', '82', '92', '120']
        program_names = ['program_one', 'program_two', 'program_three', 'program_four',
                         'program_five', 'program_six', 'program_seven', 'program_eight',
                         'program_nine', 'program_ten']

        for number, name in zip(program_numbers, program_names):
            program_key = 'program' + number
            if program_key in store1 and name in store1[program_key]:
                program3.append(store1[program_key][name])

        self.open_programs(program3)  # Call method to open programs


    def open_program_4(self):
        """Open program 4"""
        program4 = []

        program_numbers = ['13', '23', '33', '43', '53', '63', '73', '83', '93', '130']
        program_names = ['program_one', 'program_two', 'program_three', 'program_four',
                         'program_five', 'program_six', 'program_seven', 'program_eight',
                         'program_nine', 'program_ten']

        for number, name in zip(program_numbers, program_names):
            program_key = 'program' + number
            if program_key in store1 and name in store1[program_key]:
                program4.append(store1[program_key][name])

        self.open_programs(program4)  # Call method to open programs



    def open_programs(self, program_number):
        """Use a for-loop to open programs in 'program_number' list object passed to method"""

        for path in program_number:
            path_run = 'start ' + str(path)

            if path != '':
                os.system(path_run)
                time.sleep(.02)
                subprocess.call('TASKKILL /F /IM cmd.exe', shell=False)

        try:
            if store.get('app_on')['app_on_value'] == 1:
                sys.exit()
            else:
                open_program()
        except KeyError:
            open_program()



class ThirdWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass

# incorrect password pop up function
def invalid_password():
    pop = Popup(title='invalid Password',
                content=Label(text="Incorrect Password"),
                size_hint=(None, None), size=(250, 200),
                separator_color=(1, 0, 0, 1),
                background_color=(1, 1, 1, 1))
    pop.open()

# opening programs popup
def open_program():
    pop = Popup(title='Opening Programs',
                content=Label(text="Your programs are now open"),
                size_hint=(None, None), size=(250, 200),
                separator_color=(1, 0, 0, 1))
    pop.open()


# loading kv file
kv = Builder.load_file("main.kv")

# sm variable for screen manager and added no transition
sm = ScreenManager(transition=NoTransition())

# set screens
screens = [MainWindow(name="login"), SecondWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

# checks if password is turned on and changes to login or main screen
try:
    if store.get('switch')['switch_value'] == 0:
        sm.current = "main"
    else:
        sm.current = "login"
except KeyError:
    sm.current = 'main'


#main app class
class MyMainApp(App):

    def build(self):
        self.title = 'SnapAccess'
        self.icon = r'C:\Users\Garry\dev\entree\epic-entree\image\logo_dark.png'
        self.settings_cls = SettingsWithSidebar
        self.use_kivy_settings = False
        Config.read('mymain.ini')
        Config.set('input','mouse','mouse,disable_multitouch')
        Config.set('kivy','window_icon','icon')
        return sm


# settings defaults and config
    def build_config(self, config):
        config.setdefaults('password', {
            'password_on': False,
            'password_text': '',
            'app_on': True})
        config.setdefaults('program1', {
            'program_name': 'Program 1',
            '1': '',
            '2': '',
            '3': '',
            '4': '',
            '5': '',
            '6': '',
            '7': '',
            '8': '',
            '9': '',
            '10': ''})
        config.setdefaults('program2', {
            'program_name': 'Program 2',
            '1': '',
            '2': '',
            '3': '',
            '4': '',
            '5': '',
            '6': '',
            '7': '',
            '8': '',
            '9': '',
            '10': '',})
        config.setdefaults('program3', {
            'program_name': 'Program 3',
            '1': '',
            '2': '',
            '3': '',
            '4': '',
            '5': '',
            '6': '',
            '7': '',
            '8': '',
            '9': '',
            '10': '',})
        config.setdefaults('program4', {
            'program_name': 'Program 4',
            '1': '',
            '2': '',
            '3': '',
            '4': '',
            '5': '',
            '6': '',
            '7': '',
            '8': '',
            '9': '',
            '10': '', })
        config.setdefaults('info', {
            'info_page': 'How to use'
        })

    def build_settings(self, settings):
        settings.add_json_panel('General Settings', self.config, 'password.json')
        settings.add_json_panel('Program 1', self.config, 'program1.json')
        settings.add_json_panel('Program 2', self.config, 'program2.json')
        settings.add_json_panel('Program 3', self.config, 'program3.json')
        settings.add_json_panel('Program 4', self.config, 'program4.json')
        settings.add_json_panel('How to use', self.config, 'info.json')

    # on the event of settings being changed this is called
    def on_config_change(self, config, section, key, value):

        # saving password
        if key == "password_text":
            password = value
            store.put('password', password_text=password)

        # saving password switch value
        if key == "password_on":
            switch = int(value)
            store.put('switch', switch_value=switch)

        if key == "app_on":
            app_on =  int(value)
            store.put('app_on', app_on_value=app_on)


        # saving data for program 1
        if section == 'program1' and key == 'program_name':
            program1 = value
            store1.put('name1',program_name=program1)

        if section == 'program1' and key == '1':
            program1 = value
            store1.put('program10',program_one=program1)
        if section == 'program1' and key == '2':
            program2 = value
            store1.put('program20',program_two=program2)
        if section == 'program1' and key == '3':
            program3 = value
            store1.put('program30',program_three=program3)
        if section == 'program1' and key == '4':
            program4 = value
            store1.put('program40',program_four=program4)
        if section == 'program1' and key == '5':
            program5 = value
            store1.put('program50', program_five=program5)
        if section == 'program1' and key == '6':
            program6 = value
            store1.put('program60', program_six=program6)
        if section == 'program1' and key == '7':
            program7 = value
            store1.put('program70', program_seven=program7)
        if section == 'program1' and key == '8':
            program8 = value
            store1.put('program80', program_eight=program8)
        if section == 'program1' and key == '9':
            program9 = value
            store1.put('program90', program_nine=program9)
        if section == 'program1' and key == '10':
            program10 = value
            store1.put('program100', program_ten=program10)


        # saving data for program 2
        if section == 'program2' and key == 'program_name':
            program2 = value
            store1.put('name2',program_name=program2)

        if section == 'program2' and key == '1':
            program1 = value
            store1.put('program11',program_one=program1)
        if section == 'program2' and key == '2':
            program2 = value
            store1.put('program21',program_two=program2)
        if section == 'program2' and key == '3':
            program3 = value
            store1.put('program31',program_three=program3)
        if section == 'program2' and key == '4':
            program4 = value
            store1.put('program41',program_four=program4)
        if section == 'program2' and key == '5':
            program5 = value
            store1.put('program51', program_five=program5)
        if section == 'program2' and key == '6':
            program6 = value
            store1.put('program61', program_six=program6)
        if section == 'program2' and key == '7':
            program7 = value
            store1.put('program71', program_seven=program7)
        if section == 'program2' and key == '8':
            program8 = value
            store1.put('program81', program_eight=program8)
        if section == 'program2' and key == '9':
            program9 = value
            store1.put('program91', program_nine=program9)
        if section == 'program2' and key == '10':
            program10 = value
            store1.put('program110', program_ten=program10)


        # saving data for program 3
        if section == 'program3' and key == 'program_name':
            program3 = value
            store1.put('name3',program_name=program3)

        if section == 'program3' and key == '1':
            program1 = value
            store1.put('program12',program_one=program1)
        if section == 'program3' and key == '2':
            program2 = value
            store1.put('program22',program_two=program2)
        if section == 'program3' and key == '3':
            program3 = value
            store1.put('program32',program_three=program3)
        if section == 'program3' and key == '4':
            program4 = value
            store1.put('program42',program_four=program4)
        if section == 'program3' and key == '5':
            program5 = value
            store1.put('program52', program_five=program5)
        if section == 'program3' and key == '6':
            program6 = value
            store1.put('program62', program_six=program6)
        if section == 'program3' and key == '7':
            program7 = value
            store1.put('program72', program_seven=program7)
        if section == 'program3' and key == '8':
            program8 = value
            store1.put('program82', program_eight=program8)
        if section == 'program3' and key == '9':
            program9 = value
            store1.put('program92', program_nine=program9)
        if section == 'program3' and key == '10':
            program10 = value
            store1.put('program120', program_ten=program10)

        # saving data for program 4
        if section == 'program4' and key == 'program_name':
            program4 = value
            store1.put('name4',program_name=program4)

        if section == 'program4' and key == '1':
            program1 = value
            store1.put('program13',program_one=program1)
        if section == 'program4' and key == '2':
            program2 = value
            store1.put('program23',program_two=program2)
        if section == 'program4' and key == '3':
            program3 = value
            store1.put('program33',program_three=program3)
        if section == 'program4' and key == '4':
            program4 = value
            store1.put('program43',program_four=program4)
        if section == 'program4' and key == '5':
            program5 = value
            store1.put('program53', program_five=program5)
        if section == 'program4' and key == '6':
            program6 = value
            store1.put('program63', program_six=program6)
        if section == 'program4' and key == '7':
            program7 = value
            store1.put('program73', program_seven=program7)
        if section == 'program4' and key == '8':
            program8 = value
            store1.put('program83', program_eight=program8)
        if section == 'program4' and key == '9':
            program9 = value
            store1.put('program93', program_nine=program9)
        if section == 'program4' and key == '10':
            program10 = value
            store1.put('program130', program_ten=program10)


if __name__ == '__main__':
    MyMainApp().run()
