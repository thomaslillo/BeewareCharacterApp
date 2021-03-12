"""
A simple character generator for new players to D and D 5e, using questions about themselves or their ideal in game personality to create a character.
"""
# widget toolkit
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

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
        main_box = toga.Box()

        # this is where we define a window to put the main box into
        self.main_window = toga.MainWindow(title=self.formal_name) 
        self.main_window.content = main_box # we add the main box to the window
        self.main_window.show() # show the main window

# this main method creates the instance of our application - imported and invoked by __main__.py
def main():
    return CharacterWizard()