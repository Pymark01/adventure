#build grid
grid = []

for _ in range(5):
    row = []        # create a list called row
    for _ in range(5):
        row.append(".")
    grid.append(row)

#plyer position
player_x = 0
player_y = 0
grid[player_y][player_x] = "P"

# Place player
def print_grid():
    for row in grid:
        print(" ".join(row))
    print()  #empty line

# game loop
while True:
    print_grid()

    # ask player for a move
    command = input("Move (w/s/a/d), or q to quit: ").lower()

    if command == "q":
        print("goodbye!")
        break

    # clear old position
    grid[player_y][player_x] = "."

    #update position based on command
    if command == "w" and player_y> 0:
        player_y -= 1
    elif command == "s" and player_y < len(grid) -1:
        player_y += 1
    elif command == "a" and player_x > 0:
        player_x -= 1
    elif command == "d" and player_x < len(grid) -1:
        player_x += 1
    else:
        print("invalid move!")

    # place player in new position
    grid[player_y][player_x] = "P"

