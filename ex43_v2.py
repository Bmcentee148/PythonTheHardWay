# Import Statements
from sys import exit
from random import randint

# Class Definitions

class Engine(object) :

    def __init__(self, scene_map) :
        self.scene_map = scene_map

    def play(self) :
        #begin the game
        curr_scene = self.scene_map.opening_scene()

        while True :
            next_scene_name = curr_scene.enter()
            curr_scene = self.scene_map.next_scene(next_scene_name)

# Serves as a base class for our scenes 
class Scene(object) :

    #Abstract method to be implemented by child classes
    def enter() :
       print "Not implemented here. Use subclass."
       exit(1)


class Death(Scene):
    explanations = [
        'This is the end of the line. You\'re dead',
        'Too bad you couln\'t stay alive',
        'Booo you are dead'
    ]
    def enter(self) :
        print Death.explanations[randint(0, len(Death.explanations) - 1 )]
        exit(1)

class Central_Corridor(Scene) :
    def enter(self) :
        pass

class Laser_Weapon_Armory(Scene):
    def enter(self) :
        pass

class Bridge(Scene):
    def enter(self) :
        pass

class Escape_Pod(Scene):
    def enter(self) :
        pass

class Map(object) :

    scenes = {
        'death' : Death(),
        'corridor' : Central_Corridor(),
        'armory' : Laser_Weapon_Armory(),
        'bridge' : Bridge(),
        'escape' : Escape_Pod()
    }
    
    def __init__(self, opening_scene) :
        self.opening_scene = opening_scene

    def next_scene(self, scene_name) :
        return Map.scenes.get(scene_name)

    def opening_scene(self) :
        return Map.scenes.get(self.opening_scene)

death_test = Death()
death_test.enter()