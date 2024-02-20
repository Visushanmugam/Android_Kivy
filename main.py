from multiprocessing.dummy import Process
from time import sleep
from datetime import datetime
from typing import Union
import random
import webbrowser
from twilio.rest import Client
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.pickers import MDColorPicker
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.properties import StringProperty, NumericProperty
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.clock import Clock
import sqlite3
from kivy.storage.jsonstore import JsonStore
import mysql.connector



Window.keyboard_anim_args = {'d':.2,'t':'in_out_expo'}
Window.softinput_mode = "below_target"



class Manager(MDScreenManager):# pylint: disable=missing-class-docstring
    pass




class Login(MDScreen):# pylint: disable=missing-class-docstring
    pass



class Signup1(MDScreen):# pylint: disable=missing-class-docstring
    text = StringProperty()



class Signup2(MDScreen):# pylint: disable=missing-class-docstring
    pass


class Signup3(MDScreen):# pylint: disable=missing-class-docstring
    pass



class Appscren(MDScreen):# pylint: disable=missing-class-docstring
    pass


class My_App(MDApp):# pylint: disable=missing-class-docstring, too-many-public-methods
    title = "Simple App" 
    icon = "Logo.jpg"

    # kivy app setup

    def build(self):# pylint: disable=missing-function-docstring
        self.theme_cls.material_style = "M3"
        self.strng = Builder.load_file("main.kv")
        self.conn = sqlite3.connect('db.sqlite3')
        self.cur = self.conn.cursor()
        return self.strng
    
    # login page methods
  
    def user_login(self):# pylint: disable=missing-function-docstring
        try:
            self.cur.execute("SELECT * from balauser where phone=%s", [self.strng.get_screen('login').ids.phone_login.text])
            for ph in self.cur.fetchall():
                if self.strng.get_screen('login').ids.phone_login.text == ph[0]:
                    if self.strng.get_screen('login').ids.password_login.text == ph[4]:                                         
                        self.store.put('userInfo', Phone=str(self.strng.get_screen('login').ids.phone_login.text),  Name=str(ph[1]), Brith=str(ph[2]), Mail=str(ph[3]), Password=str(self.strng.get_screen('login').ids.password_login.text), Gender=str(ph[5]))
                        self.data_value_set()
                        self.root.transition.direction = 'left'
                        self.root.current = "appscreen"
                        Snackbar(text="[color=#ddbb34]Login Sucess![/color]",snackbar_y="10",size_hint_x=1).open()
                    else:
                        self.strng.get_screen('login').ids.password_login.text =  ""
                        self.strng.get_screen('login').ids.password_login.helper_text =  "Incorrect password"
                        self.strng.get_screen('login').ids.password_login.line_color_normal =  "red"
                        self.strng.get_screen('login').ids.password_login.hint_text_color_normal =  "red"
                else:
                    self.strng.get_screen('login').ids.phone_login.text =  ""
                    self.strng.get_screen('login').ids.password_login.text =  ""
        except:
            Snackbar(text="[color=#ddbb34]check your internet and try again![/color]",snackbar_y="10",size_hint_x=1).open()
            self.strng.get_screen('login').ids.phone_login.text =  ""
            self.strng.get_screen('login').ids.password_login.text =  ""

    def register_account(self):# pylint: disable=missing-function-docstring
        signupname = str(self.strng.get_screen('signup1').ids.name_signup.text)
        signupgender = ""
        if f"{self.strng.get_screen('signup1').ids.male.md_bg_color}" == "[0.38823529411764707, 0.42745098039215684, 0.7764705882352941, 1.0]":
            signupgender = "Male"
        elif f"{self.strng.get_screen('signup1').ids.female.md_bg_color}" == "[0.38823529411764707, 0.42745098039215684, 0.7764705882352941, 1.0]":
            signupgender = "Female"
        elif f"{self.strng.get_screen('signup1').ids.male_female.md_bg_color}" == "[0.38823529411764707, 0.42745098039215684, 0.7764705882352941, 1.0]":
            signupgender = "Others"
        signupage = str(self.strng.get_screen('signup2').ids.brith_signup.text)
        signupphone = str(self.strng.get_screen('signup3').ids.phone_signup.text)
        signupmail = str(self.strng.get_screen('signup3').ids.mail_signup.text)
        signuppassword = str(self.strng.get_screen('signup3').ids.password_signup.text)
        if True:
            try:
                senddata = [signupphone, signupname, signupage, signupmail, signuppassword, signupgender]
                self.cur.execute("insert into balauser (phone, name, brith, mail, password, gender) value (%s, %s, %s, %s, %s, %s)", senddata)
                self.conn.commit() 
                self.root.current = "login"
                Snackbar(text="[color=#ddbb34]Register sucessfully![/color]",snackbar_y="10",size_hint_x=1).open()
            except:
                Snackbar(text="[color=#ddbb34]check your internet and try again![/color]",snackbar_y="10",size_hint_x=1).open()
                self.root.current = "login"           


My_App().run()
