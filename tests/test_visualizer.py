def test_visualizer_draws_and_stops_after_finding_path(monkeypatch):
    monkeypatch.setenv('SDL_VIDEODRIVER', 'dummy')
    import pygame as pg
    import main
    from classes import Spot

    pg.display.init()
    screen = pg.display.set_mode((120, 80))
    Spot.all.clear()
    grid = [[Spot(x, y, screen) for x in range(3)] for y in range(3)]
    Spot.all.clear()
    for row in grid:
        for spot in row:
            spot.wall = False
            spot.add_neighbors(grid)
    start, end = grid[0][0], grid[-1][-1]
    monkeypatch.setattr(main, 'field_init', lambda: ([start], [], [], end, grid, screen))
    monkeypatch.setattr(main, 'wait_for_exit', lambda: None)
    try:
        main.main()
        assert end.g == 2
        assert screen.get_at((1, 1))[:3] == (0, 0, 255)
    finally:
        pg.quit()
