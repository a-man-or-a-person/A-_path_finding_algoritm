from random import randint
import pygame as pg
from constants import ROWS, COLS, cube_width, cube_height


class Spot:
    all = []

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.f = 0  # sum of g and h
        self.g = 0  # Distance traveled
        self.h = 0  # Distance to the target
        self.neighbors = []
        self.previous = None
        self.wall = False

        if randint(0, 10) <= 4:
            self.wall = True
            Spot.all.append(self)  # make a set

    def __repr__(self):
        return f'Spot({self.f}, {self.g}, {self.h} ---- {self.x, self.y})'

    def is_wall(self):
        return self.wall

    def show(self, color):
        rectangle = pg.Rect(self.x * cube_width, self.y * cube_height, cube_width - cube_width / 100,
                            cube_height - cube_height / 100)
        pg.draw.rect(self.screen, color, rectangle, 0)

    def add_neighbors(self, grid):
        if self.x > 0:
            self.neighbors.append(grid[self.y][self.x - 1])
        if self.x < COLS - 1:
            self.neighbors.append(grid[self.y][self.x + 1])
        if self.y > 0:
            self.neighbors.append(grid[self.y - 1][self.x])
        if self.y < ROWS - 1:
            self.neighbors.append(grid[self.y + 1][self.x])
        if self.x > 0 and self.y > 0:
            self.neighbors.append(grid[self.y - 1][self.x - 1])
        if self.x < COLS - 1 and self.y > 0:
            self.neighbors.append(grid[self.y - 1][self.x + 1])
        if self.x > 0 and self.y < ROWS - 1:
            self.neighbors.append(grid[self.y + 1][self.x - 1])
        if self.x < COLS - 1 and self.y < ROWS - 1:
            self.neighbors.append(grid[self.y + 1][self.x + 1])
