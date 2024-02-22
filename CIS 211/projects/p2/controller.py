# Implement your Controller class here

class Controller:
    def __init__(self, view, model):
        """

        :param view:
        :param model:
        """
        self.view = view
        self.model = model

    def game_loop(self):
        """
        the function handling the game loop
        :return: void
        """
        self.view.clear_screen()

        while True:
            self.view.draw_live_balloons(self.model.balloons)

            self.model.move_update(self.view.capture_input())

            self.view.display_ammo_count(self.model.total_arrows, self.model.arrow_id)

            self.view.draw_person(self.model.y, 2)

            self.view.draw_fired_arrows(self.model.arrows)

            self.view.screen_refresh()

            self.model.is_hit()

            game_status = self.model.check_game_over()

            if game_status == 'win':
                self.view.display_win(self.model.dimensions)
                break
            elif game_status == 'loss':
                self.view.display_loss(self.model.dimensions)
                break

            self.model.move_arrows()
