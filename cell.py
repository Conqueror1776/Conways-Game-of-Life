class Cell:
    def __init__(self):
        self.set_dead()

    def set_dead(self):
        self.alive = False

    def set_alive(self):
        self.alive = True

    def get_print(self):
        return 'X' if self.alive else ' '
