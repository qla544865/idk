import pygame
import numpy as np
import math
from math import sqrt


WIDTH_SCREEN = 800*2
HEIGHT_SCREEN = 450*2

origin = (WIDTH_SCREEN // 2, HEIGHT_SCREEN // 2)

def convert(x, y):
    return (origin[0] + x, origin[1] - y)

class Vector:
    def __init__(self, x1:int,y1:int, x2:int,y2:int):
        self.root = np.array([x1,y1])
        self.end_point = np.array([x2,y2])
        self.direction =  np.array([x2-x1,y2-y1])
        magnitude = np.linalg.norm(self.direction)

        self.direction = self.direction / magnitude

        self.acc_size = sqrt((x1-x2)**2 + (y1-y2)**2)
        self.size = round(self.acc_size)

    def update_point(self, x1:int,y1:int, x2:int,y2:int):
        self.root = np.array([x1,y1])
        self.end_point = np.array([x2,y2])
        self.direction =  np.array([x2-x1,y2-y1])
        magnitude = np.linalg.norm(self.direction)

        self.direction = self.direction / magnitude

        self.size = sqrt((x1-x2)**2 + (y1-y2)**2)
    
    def update_size(self, size):
        self.size = size
        self.end_point = np.array([ self.root[0] + self.direction[0] * self.size, self.root[1] + self.direction[1]*self.size ])


    def update_direction(self,x,y):
        self.direction =  np.array([x,y])
        magnitude = np.linalg.norm(self.direction)

        self.direction = self.direction / magnitude
        self.end_point = np.array([ self.root[0] + self.direction[0] * self.size, self.root[1] + self.direction[1]*self.size ])

    def move_root_point(self, x,y):
        self.root = np.array([x,y])
        self.end_point = np.array([ self.root[0] + self.direction[0] * self.size, self.root[1] + self.direction[1]*self.size ])

    def draw(self, screen:pygame.Surface, color):

        if self.size <= 0:
            return

        x1 = round(self.root[0])
        y1 = round(self.root[1])

        x2 = round(self.end_point[0])
        y2 = round(self.end_point[1])

        x1,y1 = convert(x1,y1)
        x2,y2 = convert(x2,y2)

        pygame.draw.line(screen, color, (x1,y1), (x2,y2), 3)
        pygame.draw.circle(screen, color, (x1,y1), 5)

        end_pos = (x2,y2)
        head_size=8

        dx = x2 - x1
        dy = y2 - y1
        angle = math.atan2(dy, dx)

        arrowhead_points = [
            end_pos,
            (
                end_pos[0] - head_size * math.cos(angle - math.pi / 6),
                end_pos[1] - head_size * math.sin(angle - math.pi / 6)
            ),
            (
                end_pos[0] - head_size * math.cos(angle + math.pi / 6),
                end_pos[1] - head_size * math.sin(angle + math.pi / 6)
            )
        ]

        pygame.draw.polygon(screen, color, arrowhead_points)

    def copy(self):
        return Vector(self.root[0], self.root[1], self.end_point[0], self.end_point[1])



def add_vec(vec1:Vector, vec2:Vector):
    new_vec1 = vec1.copy()
    new_vec2 = vec2.copy()

    new_vec2.move_root_point(new_vec1.end_point[0], new_vec1.end_point[1])

    new_vec = Vector(new_vec1.root[0],new_vec1.root[1], new_vec2.end_point[0],new_vec2.end_point[1])

    del new_vec1
    del new_vec2

    return new_vec

