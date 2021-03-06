# -*- coding:utf-8 -*-
from sys import exit
from random import randint


class Scene(object):
    """docstring for Scene"""

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):
    """docstring for Engine"""

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.net_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):

    quips = [
        "You died, You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Sure a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(Death.quips) - 1)]
        exit(1)


death = Death()
death.enter()
