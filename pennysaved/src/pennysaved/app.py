import pymysql.cursors
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class APennySaved(toga.App):

    def startup(self):

        main_box = toga.Box()
        LoginB = toga.Button('Login', on_press=Login(main_box, LoginB, SignupB))
        SignupB = toga.Button('Signup', on_press=Signup(main_box, LoginB, SignupB))
        main_box.add(LoginB)
        main_box.add(SignupB)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        


def Login(main_box, LoginB, SignupB):
	main_box.remove(LoginB)

def Signup(main_box, LoginB, SignupB):
	print("Signup")

def main():
    return APennySaved()

connection = pymysql.connect(host='johnny.heliohost.org',
                             user='agw_app',
                             password='AVz]~IJSu&$i',
                             db='agw_In_The_Jar',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

