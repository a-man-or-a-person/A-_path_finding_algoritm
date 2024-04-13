import sys
import pygame as pg
import math as m
from constants import display_width, display_height, COLS, ROWS
from classes import Spot


def wait_for_exit():
    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                waiting = False


def heuristic(start_point, end_point):
    return m.sqrt((end_point.x - start_point.x) ** 2 + (end_point.y - start_point.y) ** 2)


def set_start_and_end_points(grid, x1=0, y1=0, x2=COLS - 1, y2=ROWS - 1):
    start, end = grid[y1][x1], grid[y2][x2]
    if start in Spot.all:
        Spot.all.remove(start)
        start.wall = False
    if end in Spot.all:
        Spot.all.remove(end)
        end.wall = False

    return start, end


def field_init():
    '''
    Creates a grid of spots

    :return:
    openSet, closedSet, path, end, grid, screen
    '''
    pg.init()
    screen = pg.display.set_mode((display_width, display_height))
    background_color = (100, 100, 100)

    openSet = []
    closedSet = []
    path = []

    # Creating a grid
    grid = [[Spot(x, y, screen) for x in range(COLS)] for y in range(ROWS)]
    [[grid[x][y].add_neighbors(grid) for x in range(COLS)] for y in range(ROWS)]
    # if input('Do you want to set cords: Yes - type anything, No - press enter'):
    #     start, end = set_start_and_end_points(grid, int(input('Start x')), int(input('Start y')), int(input('End x')),
    #                                       int(input('End y')))
    # else:
    #     start, end = set_start_and_end_points(grid)
    start, end = set_start_and_end_points(grid)
    openSet.append(start)

    return openSet, closedSet, path, end, grid, screen


def find_path(current_block):
    path = []
    local = current_block
    while local:
        path.append(local)
        local = local.previous
    return path
