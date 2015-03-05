__author__ = 'andrew.sielen'

from datetime import datetime
import pickle

from menu import Menu
from modules import *


class Email(object):
    def __init__(self):
        self.subject = ""
        self.name = "email"
        self.created_date = datetime.today().strftime('%y%m%d')
        self.modified_date = datetime.today().strftime('%y%m%d')
        self.type = ""
        self.utm_tags = ""
        self.is_template = True  # If true build the current_email with placeholders, if false ask to add real data for each module
        self.modules = []
        self.intro = Intro()
        self.end = End()
        self.change_name()
        self.change_type()


    def number_of_modules(self):
        return len(self.modules)

    def add_module(self, module=None):
        if module:
            self.modules.append(module)
        if self.is_template is False:
            module.edit()

    def __str__(self):
        module_names = ""
        for m in self.modules:
            module_names += "{}\n".format(m.module_class)
        return module_names

    def __repr__(self):
        return self.peek()

    def peek(self):
        view = ""
        for m in self.modules:
            view += m.char
        return view

    def get_self(self):
        """
        Returns an overview of all the modules in the email
        """
        module_names = self.get_email_info()
        for m in self.modules:
            module_names += "- {}\n".format(m.name)
        return module_names

    def get_details(self):
        """
        Returns an overview of all the modules in the email with info on vars that can be filled out
        """
        email_info = self.get_email_info()
        for m in self.modules:
            email_info += "- {}\n".format(m.name)
            for cv in m.c_vars:
                if cv in ("COUNT", "CLASS"):
                    continue
                else:
                    email_info += "--- {}: {}\n".format(cv, m.c_vars[cv])
        return email_info

    def get_email_info(self):
        info = "|----------------------------|\n"
        info += "Name: {}\n".format(self.name)
        info += "Type: {}\n".format(self.type)
        info += "Date: {}\n".format(self.created_date)
        info += "Subject: {}\n".format(self.subject)
        info += "UTM_TAGs: {}\n".format(self.utm_tags)
        info += "Peek: {}\n".format(self.peek())
        info += "|----------------------------|\n"
        return info

    def change_name(self):
        if self.name != "email":  # If the email doesn't have the base name
            print("Current Name: {}".format(self.name))
        new_name = input("What do you want to call this email? ")
        if len(new_name) > 30: new_name = new_name[:30]
        self.name = new_name
        print("New Name: {}".format(self.name))

    def change_type(self):
        if self.type != "":  # If the email doesn't have the base name
            print("Current Type: {}".format(self.type))
        new_type = input("What is this email for? ")
        if len(new_type) > 30: new_type = new_type[:30]
        self.type = new_type
        print("New Name: {}".format(self.type))

    def change_subject(self):
        if self.subject != "":  # If the email doesn't have the base name
            print("Current Subject: {}".format(self.subject))
        new_subject = input("What is the subject for this email? ")
        if len(new_subject) > 200: new_subject = new_subject[:200]
        self.subjet = new_subject
        print("New Subject: {}".format(self.subject))

    def change_utm(self):
        if self.utm_tags != "":
            print("Current UTM: {}".format(self.utm_tags))
        new_utm_tags = input("What is the utmtags for this email? ")
        self.utm_tags = new_utm_tags
        print("New UTM: {}".format(self.utm_tags))

    def change_is_template(self):
        if self.is_template is True:
            choice = input("Do you want to make this an email? Y/N").lower()[0]
            if choice == "y": self.is_template = False
        else:
            choice = input("Do you want to make this a template? Y/N").lower()[0]
            if choice == "y": self.is_template = True

    def save_email(self):
        print("Saving {}-{}".format(self.name, str(self.modified_date)))
        self.modified_date = datetime.today().strftime('%y%m%d')
        pickle.dump(self, open("AutoEmail-{}-{}.tmt".format(self.name, self.created_date), "wb"))
        print("Email Saved")

    def build_html(self):
        email_html = "{}".format(self.intro.get_html())
        for m in self.modules:
            email_html += m.get_html()
        email_html += "{}".format(self.end.get_html())
        email_html = email_html.replace("{UTM}", self.utm_tags)
        return email_html

    def write_html(self, html=""):
        if html:
            self.modified_date = datetime.today().strftime('%y%m%d')
            with open('AutoEmail-{}-{}.html'.format(self.name, str(self.modified_date)), 'w') as f:
                f.write(html)

    def edit(self):
        options = [("Add Module", self.menu_add_module),
                   ("Edit Module", self.menu_edit_module),
                   ("Edit All Modules", self.menu_edit_modules),
                   ("Edit Email", self.menu_edit_email),
                   ("View Email Info", self.menu_view_email_info),
                   ("View Email Details", self.menu_view_email_details),
                   ("Save Email", self.menu_save_email),
                   ("Make Html", self.menu_make_html)]
        print(self.get_email_info())
        Menu("Edit Email", options)

    def menu_add_module(self):
        def menu_add_header():
            def add_header_normal():
                self.add_module(module=Header())

            def add_header_newsletter():
                self.add_module(module=NewsHeader())

            def add_image_header():
                self.add_module(module=ImageHeader())

            options = [("Normal", add_header_normal),
                       ("Newsletter", add_header_newsletter),
                       ("Image", add_image_header)]
            Menu("Add Header", options, drop_down=True)

        def menu_add_body():
            def add_body_hero():
                self.add_module(module=Hero())

            def add_body_secondary():
                self.add_module(module=Secondary())

            def add_body_ternary():
                self.add_module(module=Ternary())

            def add_body_tips():
                self.add_module(module=Tips())

            def add_body_cta():
                self.add_module(module=CTA())

            def add_body_copy():
                self.add_module(module=Copy())

            def add_playlist():
                pass

            # self.add_module(module=)

            options = [("Add Hero", add_body_hero),
                       ("Add Secondary", add_body_secondary),
                       ("Add Ternary", add_body_ternary),
                       ("Add Tips", add_body_tips),
                       ("Add CTA", add_body_cta),
                       ("Add Copy", add_body_copy),
                       ("Add Playlis", add_playlist)]
            Menu("Add Body", options)

        def menu_add_footer():
            self.add_module(module=Footer())

        def menu_add_legal():
            self.add_module(module=Legal())

        options = [("Header", menu_add_header),
                   ("Body", menu_add_body),
                   ("Footer", menu_add_footer)]
        Menu("Add Module", options)

    def menu_edit_module(self):
        options = [(m.name, m.edit_menu) for m in self.modules]
        Menu("Module Edit", options, drop_down=True)

    def menu_edit_modules(self):
        modules_to_delete = []
        for module in self.modules:

            result = module.edit_menu()
            if result == "del":
                modules_to_delete.append(module)
        for module in modules_to_delete:
            self.modules.remove(module)

    def menu_edit_email(self):
        options = [("Change Name", self.change_name),
                   ("Change Subject Line", self.change_subject),
                   ("Change utm_tags", self.change_utm),
                   ("Change Type", self.change_type),
                   ("Is Template?", self.change_is_template)]
        Menu("Edit Email", options)

    def menu_view_email_info(self):
        print(self.get_self())

    def menu_view_email_details(self):
        print(self.get_details())

    def menu_save_email(self):
        self.save_email()

    def menu_make_html(self):
        self.write_html(self.build_html())