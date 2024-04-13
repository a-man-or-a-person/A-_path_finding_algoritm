from functions import *

openSet, closedSet, path, end, grid, screen = field_init()

flag = False
#  Main loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    if len(openSet) > 0:
        winner = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[winner].f:
                winner = i

        current = openSet[winner]

        if openSet[winner] == end:
            print('Found')
            flag = True
            # Find the path
            path = find_path(current)

        openSet.remove(current)
        closedSet.append(current)

        for neighbor in current.neighbors:
            if not (neighbor in closedSet) and not neighbor.wall:
                tempG = current.g + 1
                if neighbor in openSet:
                    if tempG < neighbor.g:
                        neighbor.g = tempG
                else:
                    neighbor.g = tempG
                    openSet.append(neighbor)
                    neighbor.previous = current
            neighbor.h = heuristic(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h
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
