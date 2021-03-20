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
        
        
        """ creating things to go into the main box
        """
        self.name_input = toga.TextInput(style=Pack(flex=1))
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(self.name_input)
        
        # button that calls a function when pressed
        button = toga.Button(
            'Start Character Quiz',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )
        
        """ the logic and creation of the questions box
        """
        # the question box that will hold all the rows of questions
        questions_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        
        # dict to tally points into each run of the app
        # give humans a starting advantage to make more of them per party - in line with lore
        races_points = {"Dragonborn":0, "Dwarf":0, "Elf":0, "Gnome":0, "Half-Elf":0, "Hafling":0, "Half-Orc":0, "Human":3, "Tiefling":0}
        
        # import the questions and traits to display - stored externally for easy modifications
        race_traits = {} # lookup for traits
        questions = []
        
        # make this reading files into a function 
        #questions = read_csv('..\\data\\RaceQs.csv')
        
        # utf-8 with a byte order mark
        with open('..\\data\\RaceTs.csv', mode='r', encoding='utf-8-sig') as traits_file:
            for line in csv.reader(traits_file):
                race = {line[0]: line[1:]}
                race_traits.update(race)
        
        with open('..\\data\\RaceQs.csv', mode='r', encoding='utf-8-sig') as raw_file:
            for line in csv.reader(raw_file):
                questions.append(line)
        
        # print to dev console to view the files - REMOVE IN PROD
        #print(race_traits)
        #print(race_list)
        #print(race_traits['Elf'][:-1])
        print(race_traits)
        print("\n")
        print(questions)
        
        # label at the top with instructions
        instructions_label = toga.Label(
            """
            Welcome to the D&D 5e character wizard! This is like a little personality text that will match you to a race and class that you can 
            enter into your D&D character sheet. In each section pick the trait that is most like you (or who you think you'd like to be in game).
            """,
            style=Pack(padding=(2))
        )
        
        # create a box for the race questions
        race_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        
        # THE QUESTION ROW CREATION LOOP
        
        # loop through each of the 36 pre determined race comparison questions
        for i in questions:
            # selecting random traits for each combination of races
            trait_1 = race_traits[i[1]][randint(0,3)]
            trait_2 = race_traits[i[2]][randint(0,3)]

            # initial selected display value - updated by buttons
            init_val = "results"
        
            # labels of traits and question number
            RQnum = toga.Label(i[0]+". ", style=Pack(padding=(2)))
            Trait1 = toga.Label(trait_1, style=Pack(padding=(2)))
            Trait2 = toga.Label(trait_2, style=Pack(padding=(2)))
            # the buttons
            t1_very = toga.Button('Very',
                style=Pack(padding=5))
            t2_very = toga.Button('Very',
                style=Pack(padding=5))
            t1_kinda = toga.Button('Kinda',
                style=Pack(padding=5))
            t2_kinda = toga.Button('Kinda',
                style=Pack(padding=5))
            # updated label at end to display values from buttons
            chosen = toga.Label(" | Selected: "+init_val, style=Pack(padding=(2)))
        
            one_row = []
        
            one_row.append(RQnum)
            one_row.append(Trait1)
            one_row.append(t1_very)
            one_row.append(t1_kinda)
            one_row.append(t2_kinda)
            one_row.append(t2_very)
            one_row.append(Trait2)
            one_row.append(chosen)

            question_box = toga.Box(style=Pack(direction=ROW, padding=5))
            
            # add the row
            for i in one_row:
                question_box.add(i)
            
            race_box.add(question_box)
        
        """ write to the questons box - instructions first then questions then results boxes
        """
        questions_box.add(instructions_label)
        questions_box.add(race_box)

        """ adding things to the main box and adding the main box to the window
        """
        main_box.add(name_box)
        main_box.add(button)
        main_box.add(questions_box)
        
        # this is where we define a window to put the main box into
        self.main_window = toga.MainWindow(title=self.formal_name) 
        self.main_window.content = main_box # we add the main box to the window
        self.main_window.show() # show the main window    
    
    def say_hello(self, widget):
        self.main_window.info_dialog(
            'Hello',
            'Welcome {}'.format(self.name_input.value)   
        )


# this main method creates the instance of our application - imported and invoked by __main__.py
def main():
    return CharacterWizard()