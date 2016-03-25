# Import Statements
from sys import exit
from random import randint

# Class Definitions

class Engine(object) :
    
    def __init__(self, scene_map) :
        self.scene_map = scene_map

    def play(self) :
        current_scene = self.scene_map.opening_scene()
        
        while True :
            print "\n--------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

# Serves as Base Class for class that is-a Scene
class Scene(object) :
    
    # Abstract method that will be implemented in all subclasses
    def enter(self) :
        print "This is not implemented. Subclass and implement enter()."
        exit(1)

class Death(Scene) :
    
    def enter(self) :
        pass

class Central_Corridor(Scene) :
    
    def enter(self) :
        pass

class Armory(Scene) :
    
    def enter(self) :
        pass

class Bridge(Scene) :
    
    def enter(self) :
        pass

class Escape_Pod(Scene) :
    
    def enter(self) :
        pass

class Map(object) :
    
    scenes = {
        'death' : Death() ,
        'central_corridor' : Central_Corridor(),
        'laser_weapon_armory' : Armory(),
        'escape_pod' : Escape_Pod(),
        'bridge' : Bridge()
    }

    def __init__(self, start_scene) :
        self.start_scene = start_scene

    def next_scene(self, scene_name) :
        return Map.scenes.get(scene_name)

    def opening_scene(self) :
        return self.next_scene(self.start_scene)
#Script
game_map = Map('Central_Corridor') # create map of game scenes
game = Engine(game_map) # create game engine using map of scenes
game.play() # run the game
