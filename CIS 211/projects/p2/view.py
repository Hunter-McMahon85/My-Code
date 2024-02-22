import curses


# Implement your View class(es). I recommend using an abstract base class View,
# and inheriting the specific View for balloons and arrows from it, e.g., in
# a ViewBalloonPop class

class ViewBalloonPop:
    def __init__(self, screen):
        """
        initiator function for the ViewBalloonPop class
        :param screen: the display object for the game
        """
        self.screen = screen
        self.key = screen.getch()


    def draw_person(self, y: int, x: int):
        """
        Draw a "person" centered at the y, x coordinates
        :param y: persons y coordinate/height
        :param x: persons x coordinate (horizontal)
        :return: void
        """
        self.screen.addstr(y, x, '😃')

    def draw_arrow(self, y: int, x: int):
        """
        Draws an arrow based on the y, x coordinates.
        :param y: arrows height/y coordinate
        :param x: arrows horizontal x coordinate
        :return: void
        """
        self.screen.addstr(y, x, '->')

    def draw_live_balloons(self, balloons: list):
        """
        draws the balloons onto the screen
        :param balloons: list of balloons coordinate tuples
        :return: void
        """
        for y_balloon, x_balloon in balloons:
            self.screen.addstr(y_balloon, x_balloon, '🎈')

    def clear_screen(self):
        """
        clears the display screen
        :return: void
        """
        # Clears the screen
        curses.cbreak()
        curses.curs_set(0)  # Makes the cursor invisible
        self.screen.keypad(True)
        self.screen.clear()
        self.screen.nodelay(True)  # allows input while arrow moving

    def display_ammo_count(self, total_ammo, ammo_fired):
        """
        displays the ammo counter
        :return: void
        """
        self.screen.addstr(0, 0, 'Arrows left: ' + str(total_ammo - ammo_fired))

    def draw_fired_arrows(self, arrows):
        """
        draws the fired arrows on the screen
        :param arrows: dictionary of existing arrows and their attributes
        :return: void
        """
        for arrow in arrows.values():
            self.draw_arrow(arrow[0], arrow[1])

    def screen_refresh(self):
        """
        refreshes the view
        :return: void
        """
        self.screen.refresh()  # refresh the screen (draw everything)
        curses.napms(100)  # wait 100 milliseconds
        self.screen.clear()  # clear the screen

    def display_win(self, dimensions):
        """
        displays win screen
        :return: void
        """
        self.screen.addstr(dimensions[0] // 2, dimensions[1] // 2 - 5, '😃 You win! 😃')
        self.screen.refresh()
        curses.napms(3000)

    def display_loss(self, dimensions):
        """
        displays loss screen
        :return: void
        """
        self.screen.addstr(dimensions[0] // 2, dimensions[1] // 2 - 6, '😞 You lose! 😞')
        self.screen.refresh()
        curses.napms(3000)  # pause for 3 seconds

    def capture_input(self):
        """
        captures input for the game
        :return: a string that is used to by the move_update function in the model
        """
        if self.key == curses.KEY_UP:
            return 'up'
        elif self.key == curses.KEY_DOWN:
            return 'down'
        elif self.key == 32:
            return 'fire'

