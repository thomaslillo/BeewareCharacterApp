"""
A simple character generator for new players to D and D 5e, using questions about themselves or their ideal in game personality to create a character.
"""
# widget toolkit
import toga
from toga.style import Pack
from toga.style.pack import ALIGNMENT_CHOICES, COLUMN, ROW, RIGHT, CENTER, Pack
import csv
import random
import sys
from functools import partial

from travertino.constants import CENTER

class Mdict:
    def __init__(self):
        self.d = {}
    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError(key)
    def add_key(self, prefix, suffix):
        if prefix in self.d:
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]
    def get_suffix(self,prefix):
        l = self[prefix]
        return random.choice(l)

# each toga app has a single toga.app instance, representing the entity that is the application
class CharacterWizard(toga.App):

    # the startup method for the app
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        # the main box is defined - toga apps are comprised of boxes or widgets with styles applied, all within the main box
        main_box = toga.Box(style=Pack(direction=COLUMN)) # creating the main box with a style
        # COLUMN box - that is, it is a box that will consume all the available width, and will expand its height as content is added, but it will try to be as short as possible.
        
        """ the logic and creation of the questions box
        """
        # the question box that will hold all the rows of questions
        questions_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        
        # label at the top with instructions
        instructions_label = toga.Label(
            """
            Welcome to the D&D 5e character name wizard! This is like a little tool that will help you select a brand new name for any character, 
            whether it be an NPC or player, by the theme of the game. These names are created using a Markov Chain from lists of existing names 
            from that theme! This ensures that they are new to you and your fellow players! Press a button below to generate a name.
            """,
            style=Pack(padding=(2))
        )

        # store the list of names in a list
        self.names = []
        
        # make this reading files into a function 
        #questions = read_csv('..\\data\\RaceQs.csv')
        with open('..\\data\\namelist.csv', mode='r', encoding='utf-8-sig') as raw_file:
            for line in csv.reader(raw_file):
                self.names.append(line)
        
        # clean up the blanks in the lists of names
        for category in self.names:
            while '' in category:
                category.remove('')
    
        # the buttons that display a name based on its category
        # ADD BUTTONS HERE WHEN YOU ADD A LIST
        
        button_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        
        # loop through all the lists and create a button for each
        for category in self.names:
            # create the button names
            button = toga.Button(category[1],on_press= partial(self.CreateNames,index=int(category[0])), style=Pack(padding=5))
            # add the button tot he box
            button_box.add(button)
        
        # display the name to the screen (this will be updated with the new names)
        output = toga.Box(style=Pack(direction=ROW,  padding=5))
        output.add(toga.Label('Randomly Generated Name', style=Pack(text_align=RIGHT)))
        self.display_name = toga.TextInput(readonly=True)
        output.add(self.display_name)
        
        """ write to the questons box - instructions first then questions then results boxes
        """
        questions_box.add(instructions_label)
        questions_box.add(button_box)
        questions_box.add(output)
        """ adding things to the main box and adding the main box to the window
        """
        main_box.add(questions_box)
        
        # this is where we define a window to put the main box into
        self.main_window = toga.MainWindow(title=self.formal_name) 
        self.main_window.content = main_box # we add the main box to the window
        self.main_window.show() # show the main window    
        
    # the display name button widgets
    def CreateNames(self, widget, index):
        # call the generate_names function with the elven subset of self.names
        self.clean_names = self.names[index]
        # set the list to be everything except first two columns
        self.selected_list = self.clean_names[2:]
        name = self.build_dict()
        #print(name)
        self.display_name.value = name
        
    def build_dict(self, chainlen = 2):
        """
        Building the dictionary
        https://towardsdatascience.com/generating-startup-names-with-markov-chains-2a33030a4ac0 <- how I learned to do this
        """
        
        if chainlen > 10 or chainlen < 1:
            print("Chain length must be between 1 and 10, inclusive")
            sys.exit(0)

        self.mcd = Mdict()
        oldnames = []
        self.chainlen = chainlen

        # use the selected list of names
        for l in self.selected_list:
            l = l.strip()
            oldnames.append(l)
            s = " " * chainlen + l
            for n in range(0,len(l)):
                self.mcd.add_key(s[n:n+chainlen], s[n+chainlen])
            self.mcd.add_key(s[len(l):len(l)+chainlen], "\n")
        
        return self.New()
        
    def New(self):
        """
        New name from the Markov chain
        """
        prefix = " " * self.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > 9:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.capitalize()


# this main method creates the instance of our application - imported and invoked by __main__.py
def main():
    return CharacterWizard()