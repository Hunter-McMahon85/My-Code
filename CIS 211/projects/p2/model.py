# Implement your Model class here
import random


class Model:
    def __init__(self, targets: int, ammo: int, screen):
        """
        initializes the model object for the games behind the scenes functions
        :param targets: (int) number of targets in the game
        :param ammo: (int) number of shots you have to pop the targets
        :param screen: the display object
        """
        self.dimensions = screen.getmaxyx()
        self.balloons = [(random.randint(1, self.dimensions[0] - 2),
                          random.randint(10, self.dimensions[1] - 2)) for i in range(targets)]
        self.arrows = {}
        self.arrow_id = 0
        self.total_arrows = ammo
        self.y = self.dimensions[0] // 2  # halfway down the screen

    def move_update(self, direction: str):
        """
        changes y to move the person based on user input
        :param direction: direction moved , can either be up, down, or space
        :return: void
        """
        if direction == 'up':  # up arrow
            self.y = max(2, self.y - 1)  # only go up to the second line of the screen
        elif direction == 'down':  # down arrow
            self.y = min(self.dimensions[0] - 1, self.y + 1)  # only go down to the last line of the screen
        elif direction == 'fire':  # 32 is the ASCII code for the spacebar
            # "Shoot" an arrow (add it to the dictionary)
            if self.arrow_id < self.total_arrows:
                self.arrows[self.arrow_id] = (self.y, 3)
                self.arrow_id += 1

    def is_hit(self):
        """
        checks to see if a balloons been hit
        :return: void
        """
        for y_arrow, x_arrow in self.arrows.values():
            if (y_arrow, x_arrow) in self.balloons:
                self.balloons.remove((y_arrow, x_arrow))  # Pop the balloon

    def check_game_over(self) -> str:
        """
        checks to see if the game is over
        :return: Boolean, True if game over, False if not
        """
        # Check if game over (no balloons left!)
        if len(self.balloons) == 0:
            return 'win'
        # Check if game over (no arrows!)
        if len(self.arrows) == 0 and self.arrow_id >= self.total_arrows:
            return 'loss'
        else:
            return 'game on'

    def move_arrows(self):
        """
        moves the arrows across the screen by updating coordinates
        :return: void
        """
        for item in list(self.arrows):
            pos = self.arrows[item]
            if pos[1] >= self.dimensions[1] - 3:
                # Arrow reached right end of screen
                del self.arrows[item]
            else:
                self.arrows[item] = (pos[0], pos[1] + 1)
