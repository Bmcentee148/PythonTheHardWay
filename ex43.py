# Class Definitions
class Map(object) :
    
    def __init__(self, start_scene) :
        pass

    def next_scene(self) :
        pass

    def opening_scene(self) :
        pass

class Engine(object) :
    
    def __init__(self, scene_map) :
        pass

    def play(self) :
        pass

class Scene(object) :
    
    def enter(self) :
        pass

class Death(Scene) :
    pass

class Central_Corridor(Scene) :
    pass

class Armory(Scene) :
    pass

class Bridge(Scene) :
    pass

class Escape_Pod(Scene) :
    pass

#Script
game_map = Map('Central_Corridor') # create map of game scenes
game = Engine(game_map) # create game engine using map of scenes
game.play() # run the game
