from sys import exit


class Scene(object):

    # enter the scene
    def enter(self):
        pass


# main game
class Engine(object):

    # create engine for our game given the object scene_map
    def __init__(self, scene_map):
        self.scene_map = scene_map
        self.next_room = None

    # start the game
    def play(self):
        
        print("(engine runs opening scene)")
        self.scene_map.opening_scene()
        print("(after opening scene the engine runs the start scene)")

        for i in range(6):
            self.scene_map.next_scene(a_game.next_room)
            print("(we changed a_game.next_room atrribute into ", self.next_room, ")")
            
            self.scene_map.next_scene(a_game.next_room)
        
class Map(object):

    # tell which scene is the start one
    def __init__(self, start_scene):
        self.start_scene = start_scene
        #self.current_scene = start_scene

    def next_scene(self, scene_name):
        print(">>>", scene_name)
        self.scene_name = scene_name
        print(">>>", self.scene_name)
        print("(here is a next scene module)")
        print("(we have a string", scene_name, "and want to run this room enter module) ")
        print("(we create an object for this room)")
        
        if scene_name == 'central_corridor':
            central_corridor = CentralCorridor()
            print("(we run the module central_corridor.enter()")
            central_corridor.enter()
        elif scene_name == 'the_bridge':
            the_bridge = TheBridge()
            print("(we run the module the_bridge.enter()")
            the_bridge.enter()

    def opening_scene(self):
        print("(here is the opening scene desription)")
        a_game.next_room = self.start_scene


class CentralCorridor(Scene):

    def enter(self):
        print("(we print the central corridor description)")
        print("(we let user decide which is the next room to enter)")
        a_game.next_room = input("\n> ") # just type the name of the room
        print("(now we have to return the name of next room to the engine so it can run it from map object")


class TheBridge(Scene):

    def enter(self):
        print("(we print the bridge description)")
        print("(we let user decide which is the next room to enter)")
        print("(now we have to return the name of next room to the engine so it can run it from map object")
        a_game.next_room = input("\n> ") # just type the name of the room


# central_corridor is a start_scene
a_map = Map('central_corridor')
# a_map is a scene_map
a_game = Engine(a_map)
# start a game
a_game.play()


class Death(Scene):

    def enter(self):
        pass


class LaserWeaponArmory(Scene):

    def enter(self):
        pass





class EscapePod(Scene):

    def enter(self):
        pass