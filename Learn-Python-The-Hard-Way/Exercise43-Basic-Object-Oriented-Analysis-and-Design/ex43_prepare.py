# -*- coding: utf-8 -*-

'''
The process is as follows:
    1. write or draw about the problem.
    2. Extract key concepts from #1 and research them.
    3. Create a class hierarchy and object map for the concepts.
    4. Code the classes and a test to run them.
    5. Repeat and refine
'''

# The Analysis of a Simple Game Engine

# 1. Write or Draw about the Problem
'''
Aliens have invaded a space ship and our hero has to go though a maze of rooms
defeating them so he can escape into an escape pod to the planet below.The game
will be more like a Zork or Adventure type game with text outputs and funny
ways to die. The game will involve an engine that runs a map full of rooms or
scenes. Each room will print its own description when the player enters it and
then tell the engine what room to run next out of the map.
'''

# 2. Extract key concepts from #1 and research them.

# Alines
## Player
# Space Ship
## Maze
# Room
# Scene
## Gothon
# Escape Pod
# The Planet
# Map
## Engine
## Death
## Gentral Corridor
## Laser Weapon Armory
## The Bridge


# 3. Create a class hierarchy and object map for the concepts.

'''
* Map
* Engine
* Scene
  * Death
  * Central Corridor
  * Laser Weapon Armory
  * The Bridge
  * Escape Pod
'''

# add verbs
'''
* Map
  - next_scene
  - opening_scene
* Engine
  - play
* Scene
  - enter
  * Death
  * Central Corridor
  * Laser Weapon Armory
  * The Bridge
  * Escape Pod
'''

# 4. Code the classes and a test to run them.
class Scene(object):
    def enter(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):
    def enter(self):
        pass

class CentralCorridor(Scene):
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapedPod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def open_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()















