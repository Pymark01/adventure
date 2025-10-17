#this is to build a monster-list made out of objects
from monster_dictionary import monsters_data
from monster_class_two import Monstertwo

monster_bank = []
for monster_dict in monsters_data:
    # Each dictionary has only one key-value pair
    monster_name = list(monster_dict.keys())[0]  # gets skeleton, 'zombie', etc..
    stats = monster_dict[monster_name]  #gets {"detection": 4, "hide": 2,....}

    new_monster = Monstertwo(
        monster_name,
        stats["detection"],
        stats["hide"],
        stats["attack"],
        stats["defense"],
        stats["health"],
    )
    monster_bank.append(new_monster)

    print(new_monster)

# build grid
grid = []

for _ in range(5):
    row = []
    for y in range(5):
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
