from menu import Menu

__author__ = 'andrew.sielen'


class EmailModule(object):
    module_class = ""
    module_count = 0
    html = ""
    char = "$"  # used to represent the module in a quick view

    @classmethod
    def add_module(cls):
        cls.module_count += 1

    def __init__(self):
        self.add_module()
        self.position = str(self.module_count)  # Set the position as the current count
        self.c_vars = {'COUNT': self.position, 'CLASS': self.module_class}

    def __str__(self):
        rep = self.html
        for v in self.c_vars:
            if v == "COPY":
                copy = self.c_vars['COPY']
                copy = "<p>" + copy + "</p>"
                copy.replace("\n", "</p><p>")
                rep = rep.replace("{{{}}}".format(v), copy)
            else:
                rep = rep.replace("{{{}}}".format(v), self.c_vars[v])
        return rep

    def get_html(self):
        return self.__str__()

    @property
    def name(self):
        return "{}-{}".format(self.module_class, self.position)

    def get_var_values(self):
        values = ""
        for v in self.c_vars:
            values += "{{{}}} = {}\n".format(v, self.c_vars[v])
        return values

    def edit_menu(self):
        def menu_continue():
            return "cont"

        def menu_edit():
            self.edit()

        def menu_delete():
            return "del"

        options = [("Continue", menu_continue),
                   ("Edit", menu_edit),
                   ("Delete", menu_delete)]
        return Menu("Edit Module: {}".format(self.name), options, drop_down=True)

    def edit(self):  # This can be overridden by the child elements if there is something to edit
        if len(self.c_vars) < 3:
            print("Nothing to edit")
        else:
            for v in self.c_vars:
                if v in ('CLASS', 'COUNT'): continue
                self.c_vars[v] = input("Enter the value for {}: ".format(v))