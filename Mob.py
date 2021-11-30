import pygame
from Object import Object 
from pygame.math import Vector2
from Effect import Boom
import math

class Mob(Object):
    def __init__(self, img_path, size, velocity, missile):
        super().__init__(img_path, size, velocity)
        self.missile = missile
        self.is_targeted = False
        self.direction = Vector2(1,1)
        self.rad = 1

    def move(self, boundary, game):
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]): #update when screen resized
            self.on_resize(game)

        self.x += self.direction.y
        self.y += self.direction.x
        self.rad+=0.08*self.velocity #속도에 적절한 값을 곱하여, 각도 변경
        self.direction.from_polar((self.velocity*4,math.sin(self.rad)*90)) #속도에 비례한 길이를 갖고, 방향 sin함수를 따르는 벡터를 다음 방향으로 지정

        if self.y >= boundary[1] - self.sy:
            game.mobList.remove(self)

    def destroy(self, game):
        boom = Boom(game.animation.animations["destroy_effect"])
        mob_location = {"x":self.x+(self.sx/2), "y":self.y+(self.sy/2)}
        boom.set_XY((mob_location["x"] - boom.sx/2, mob_location["y"]- boom.sy/2))
        game.effect_list.append(boom)
        if self in game.mobList:
            game.mobList.remove(self)
                        

        