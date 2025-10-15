
# build grid
grid = []

for _ in range(5):
    row =[]
    for y in range (5):
        row.append(".")
    grid.append(row)

#player position
player_x = 0  #column
player_y = 0  #row

#place player
grid[player_y][player_x] = "P"
for row in grid:
    print(row)

print("Move right")

# move the player right

grid[player_y][player_x] = "."  # clear the old spot
player_x += 1
grid[player_y][player_x] = "P"

# print updated grid
for row in grid:
    print(row)
