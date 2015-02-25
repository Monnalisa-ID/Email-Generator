__author__ = 'andrew.sielen'

from menu import AMenu, LMenu
import modules
import pickle
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
        AMenu("Main Menu", options)

    def menu_create_email(self):
        self.current_email = modules.Email()
        self.menu_edit_email()

    def menu_edit_email(self):
        if self.current_email is None:
            self.menu_create_email()
        self.current_email.edit()
        pass

    def menu_load_email(self):
        LMenu("Load Email", self.loaded_templates, function=self._load_email)

    def menu_save_template(self):
        self.current_email.save_email()

    def _load_email(self, file_name):
        self.current_email = pickle.load(open(file_name, "rb"))


    def load_templates(self):
        filenames = os.listdir(os.getcwd())
        templates = []
        for file in filenames:
            if file.endswith(".tmt"):
                templates.append(file)
        return templates


run()