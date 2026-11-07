from functions import *


def main():
    openSet, closedSet, path, end, grid, screen = field_init()

    flag = False
    #  Main loop
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        if len(openSet) > 0:
            current = search_step(openSet, closedSet, end)
            if current is end:
                print('Found')
                flag = True
                path = find_path(current)
        else:
            print('No path found')
            flag = True

        screen.fill((91, 97, 97))
        # [[grid[x][y].show((91, 97, 97)) for x in range(COLS)] for y in range(ROWS)]
        for i in Spot.all:
            i.show((0, 0, 0))

        for i in openSet:
            i.show((0, 255, 0))

        for i in closedSet:
            i.show((255, 0, 0))

        for i in path:
            i.show((0, 0, 255))

        pg.display.update()
        pg.display.flip()
        if flag:
            wait_for_exit()
            break


if __name__ == "__main__":
    main()
