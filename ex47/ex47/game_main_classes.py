from os import system
import platform


class Room(object):

    time = 1

    def __init__(self, name):
        self.name = name
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

    # clear IDLE window
    def clear(self):

        # for Windows
        if platform.system() == "Windows":
            system('cls')

        # for Mac and Linux
        else:
            system('clear')


class Engine(object):

    # # download a scenerio and scenes
    # def download(self, scenerio):

    #     self.scenerio = scenerio

    def __init__(self, game_intro):

        self.game_intro = game_intro

    # play a game
    def play(self):

        next_game = self.game_intro

        while True:
            next_game = next_game.run()