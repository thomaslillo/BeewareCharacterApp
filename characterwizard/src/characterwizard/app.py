"""
A simple character generator for new players to D and D 5e, using questions about themselves or their ideal in game personality to create a character.
"""
# widget toolkit
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT, Pack
import csv
from random import randint

from travertino.constants import CENTER

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
            Welcome to the D&D 5e character wizard! This is like a little personality text that will match you to a race and class that you can 
            enter into your D&D character sheet. In each section pick the trait that is most like you (or who you think you'd like to be in game).
            Unless otherwise chosen, names are randomly generated from the elven category!
            """,
            style=Pack(padding=(2))
        )
        
        # select a gender
        
        # create a box for the race questions
        name_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        
        # store the list of names in a list
        names = []
        
        # make this reading files into a function 
        #questions = read_csv('..\\data\\RaceQs.csv')
        with open('..\\data\\namelist.csv', mode='r', encoding='utf-8-sig') as raw_file:
            for line in csv.reader(raw_file):
                names.append(line)
        print(names)
        
        
        greek = toga.Button(
        "Greek Myth Names",
        on_press=self.GreekNames,
        style=Pack(padding=5)
        )
        
        elven = toga.Button(
        "Elven Myth Names",
        on_press=self.ElvenNames,
        style=Pack(padding=5)
        )
        
        name_box.add(greek)
        name_box.add(elven)
        
        """ write to the questons box - instructions first then questions then results boxes
        """
        questions_box.add(instructions_label)
        questions_box.add(name_box)
        """ adding things to the main box and adding the main box to the window
        """
        main_box.add(questions_box)
        
        # this is where we define a window to put the main box into
        self.main_window = toga.MainWindow(title=self.formal_name) 
        self.main_window.content = main_box # we add the main box to the window
        self.main_window.show() # show the main window    
    
    def GreekNames(self, widget):
        print('greek names!')
        # call the generate_names function with the greek subset of self.names
    
    def ElvenNames(self, widget):
        print('Elven names!')
        # call the generate_names function with the elven subset of self.names
        
    def generate_names(self, widget, names):
        # placeholder code
        print('predict!')
        
        # create a list of all the first letters of names from names list
        
        # create a probability table from the list of two letter pairings
        
        # randomly select 6 letters from the first letter list
        
        # randomly generate a expected length for all 6 names
        
        # return a list of 6 names between 5 and 12 characters long


# this main method creates the instance of our application - imported and invoked by __main__.py
def main():
    return CharacterWizard()