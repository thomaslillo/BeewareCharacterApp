"""
A simple character generator for new players to D and D 5e, using questions about themselves or their ideal in game personality to create a character.
"""
# widget toolkit
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT, Pack
import csv

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

        # import the questions and traits to display
        race_traits = {} # lookup for traits
        questions_list = []
        
        # utf-8 with a byte order mark
        with open('..\\data\\RaceTs.csv', mode='r', encoding='utf-8-sig') as traits_file:
            for line in csv.reader(traits_file):
                race = {line[0]: line[1:]}
                race_traits.update(race)
        
        with open('..\\data\\RaceQs.csv', mode='r', encoding='utf-8-sig') as questions_file:
            for line in csv.reader(questions_file):
                questions_list.append(line)
        
        # print to dev console to view the files       
        #print(race_traits)
        #print(race_list)
        #print(race_traits['Elf'][:-1])
        print(questions_list)
        
        
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
        
        """ the questions that go into the box
        """
        
        # the question box that will hold all the rows of questions
        questions_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        
        # label at the top with instructions
        instructions_label = toga.Label(
            'Player Name: ',
            style=Pack(padding=(5))
        )
        
        # options for each question choice
        opts_box = toga.Box(style=Pack(direction=ROW, padding=5))
        
        options = []
        
        for i in range(1,4):
            opt = toga.Button(
            'Trait '+str(i),
            style=Pack(padding=5)
            )
            options.append(opt)
        
        for opt in options:
            opts_box.add(opt) 
        
        # write to the questons box - instructions first then questions
        questions_box.add(instructions_label)
        questions_box.add(opts_box)

        """ adding things to the main box and adding the main box to the window
        """
        
        # add the things to the main box
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