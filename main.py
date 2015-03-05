from Elements.EmailClass import Email

__author__ = 'andrew.sielen'

from menu import Menu, Load_Menu
import dill
import os

class run(object):


    def __init__(self):
        self.loaded_templates = self.load_templates() #list of the template files it finds in the working directory
        self.current_email = None
        self.main_menu()


    def main_menu(self):
        options = [("Create Email", self.menu_create_email),
                   ("Load Template", self.menu_load_email),
                   ("Edit Email", self.menu_edit_email),
                   ("Save Email", self.menu_save_template)]
        if self.current_email != None:
            print(self.current_email.peek())
        Menu("- Main Menu -", choices=options, quit=True)

    def menu_create_email(self):
        self.current_email = Email()
        self.menu_edit_email()

    def menu_edit_email(self):
        if self.current_email is None:
            self.menu_create_email()
        self.current_email.edit()
        pass

    def menu_load_email(self):
        Load_Menu(name="- Load Email- ", choices=self.loaded_templates, function=self._load_email)

    def menu_save_template(self):
        self.current_email.save_email()

    def _load_email(self, file_name):
        self.current_email = dill.load(open(file_name, "rb"))


    def load_templates(self):
        filenames = os.listdir(os.getcwd())
        templates = []
        for file in filenames:
            if file.endswith(".tmt"):
                templates.append(file)
        return templates


run()