import random
from collections import deque

from classes import Spot
from functions import heuristic, search_step, find_path


def test_diagonal_distance():
    assert heuristic(Spot(0, 0, None), Spot(1, 1, None)) == 1


def test_search_matches_breadth_first_on_rectangular_grids():
    for seed in range(100):
        rng = random.Random(seed)
        grid = [[Spot(x, y, None) for x in range(9)] for y in range(5)]
        for row in grid:
            for spot in row:
                spot.wall = rng.random() < 0.3
                spot.add_neighbors(grid)
        start, end = grid[0][0], grid[-1][-1]
        start.wall = end.wall = False
        queue, distances = deque([start]), {start: 0}
        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if not neighbor.wall and neighbor not in distances:
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
        opened, closed = [start], []
        found = None
        while opened:
            current = search_step(opened, closed, end)
            if current is end:
                found = len(find_path(end)) - 1
                break
        assert found == distances.get(end)
