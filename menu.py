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
