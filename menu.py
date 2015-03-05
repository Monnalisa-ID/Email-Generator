__author__ = 'andrew.sielen'
__version__ = 200
# Basic menu system v2.0

class AMenu(object):
    """
    Basic menu in the format:
    1: Item
    2: Item
    3: Item
    Q: Back/Quit

    Need to pass a list of option strings with functions attached
    drop_down=True means the menu wont open itself again when closed
    """

    def __init__(self, name="", options=None, drop_down=False):
        self.name = name
        self.options = {}
        assert len(options) <= 34
        for idx, opt in enumerate(options):
            self.options[self.chars[idx]] = opt
        self.options["Q"] = ("Back", AMenu.back)
        self.options_list = list(self.options.keys())
        self.options_list.sort()
        self.drop_down = drop_down #If this is True, the menu auto quits after a selection
        self._choose()

    chars = ('1','2','3','4','5','6','7','8','9',
             'A','C','D','E','F','G','H','I',
             'J','K','L','M','N','O','P','R','S',
             'T','U','V','W','X','Y','Z')
            #Used to create the order of the menu

    @staticmethod
    def quit():
         return 'kill'

    @staticmethod
    def back():
         return 'kill'

    kill = 'kill'

    def _options_menu(self):
        print("\n- {} -".format(self.name))
        for entry in self.options_list:
            print("  " + entry + ":", self.options[entry][0])

        selection = input("What would you like to do? ").upper()
        if selection in ("0", "B"): selection = "Q" #You can quit with 0 or B also

        if selection in self.options:
            action = self.options[selection][1]
            return action()
        else:
            print("Invalid Input. Please try again")

    def _choose(self):
        result = None
        while True:
            result = self._options_menu()
            if result is self.kill:
                break
            if self.drop_down is True:
                break
        return result

class LMenu(AMenu):
    """
    Load menu

    Need to pass a list of text strings and a function to pass the choice string to
    """
    def __init__(self, name="", files=None, function=None, drop_down=True):
        self.name = name
        self.files = {}
        self.function = function
        assert len(files) <= 34
        for idx, opt in enumerate(files):
            self.files[self.chars[idx]] = opt
        self.files["Q"] = "Back"
        self.files_list = list(self.files.keys())
        self.files_list.sort()
        self.drop_down = drop_down #If this is True, the menu auto quits after a selection
        self._choose()

    def _options_menu(self):
        print("\n- {} -".format(self.name))
        for entry in self.files_list:
            print("  " + entry + ":", self.files[entry])

        selection = input("What file would you like to load? ").upper()
        if selection in ("0", "B"): selection = "Q" #You can quit with 0 or B also

        if selection == "Q":
            return self.back()
        elif selection in self.files:
            return self.function(self.files[selection])
        else:
            print("Invalid Input. Please try again")


# __author__ = 'andrew.sielen'
#
# __version__ = 300
# # Basic menu system v3.0

class Menu(object):
    """
        Basic menu in the format:
        1: Item
        2: Item
        3: Item
        Q: Back/Quit

        Need to pass a list of option strings with functions attached
        drop_down=True means the menu wont open itself again when closed
    """

    STANDARD = 0
    LOAD = 1
    RETURN = 2
    KILL = 0

    def __init__(self, name=None, choices=None, function=None, drop_down=False, type=STANDARD, quit=False):
        """

        :param name: Menu intro text. Can also be a function call as long as it returns a string
        :param choices:
            Can be in two formats:
                1) Names with Functions
                    [("Choice1",Function1),("Choice2",Function2)]
                2) Names
                    ["Name1","Name2","Name3"]
        :param drop_down:
            False = Keep loading this menu until option back/quit is chosen
            True = load the menu once and then quit
        :param type:
            standard = choice format 1
            load = choice format 2
            return = choice format 2 - returns the choice instead of calling a function on that choice
        :param quit:
            True = have the last option be 'quit'
            False = have the last option be 'back'
        :return:
        """

        self.name = name
        self.type = type
        if function is None:
            self.function = self.return_string
        else:
            self.function = function

        # Make sure that the choices is in the right format for the type
        if type == self.STANDARD:
            # Should be in the format listed above, so each element should be a tuple of two elements
            assert len(choices[0]) == 2
        elif type == self.LOAD:
            # If the type isn't standard, we need a function to run
            assert function != None

        self.drop_down = drop_down

        self.choices = {}

        for idx, opt in enumerate(choices):
            if self.type != self.STANDARD:
                opt = (opt, self.function)  # convert the opt to a tuple if it isn't one
            self.choices[self.idx_to_sel(idx)] = opt

        # Create the choice list. - Could have just used a sorted dict.
        self.options_list = list(self.choices.keys())
        self.options_list.sort()

        # For any menu type, this is just a text string that triggers a return instead of an action
        if quit:
            self.choices["0"] = ("Quit", self.back)
        else:
            self.choices["0"] = ("Back", self.back)
        self.options_list.append("0")

        self._choose_loop()  # Run the menu

    def return_string(self, str):
        """
        For the type: return. Returns the string instead of working it with the function
        :return:
        """
        return str

    def back(self):
        return

    def idx_to_sel(self, idx):
        """
            Convert the index number to a string that can be used in the selection process
                Adds one to the string so it starts with 0. 0 is reserved for quit/back
        """
        return str(idx + 1)

    def _options_menu(self):
        menu_intro = ""

        if callable(self.name):
            # If a function was entered for the header, call it
            menu_intro = self.name()
        else:
            # else use the text string
            menu_intro = self.name

        print("\n{}".format(menu_intro))

        for entry in self.options_list:
            print("  " + entry + ":", self.choices[entry][0])

        selection = input("Which selection? ")

        if selection in self.choices:
            if selection == "0":
                return self.KILL

            action = self.choices[selection][1]
            if self.type == self.STANDARD:
                return action()
            else:
                return action(self.choices[selection][0])

        else:
            print("Invalid Input. Please try again")


    def _choose_loop(self):
        result = None
        while True:
            result = self._options_menu()
            if result is self.KILL:
                break
            if self.drop_down is True:
                break
        return result


class Load_Menu(Menu):
    """
    Alias for Load Menus
    """

    def __init__(self, name=None, choices=None, function=None):
        super(Load_Menu, self).__init__(name=name, choices=choices, function=function, drop_down=True, type=Menu.LOAD)