from monster_class import Monsters

skeleton =Monsters("skeleton", 6,2,14)
zombie = Monsters("zombie", 10,0,20)

skeleton_alive = True
zombie_alive = True

while skeleton_alive and zombie_alive:
    print("The fight continues...")

    # skeleton attacks first
    damage = skeleton.damage()
    zombie.health -= damage
    print(f"Skeleton attacks Zombie for {damage} damage. Zombie health: {zombie.health}")
    if skeleton.health > zombie.health:
        zombie.health -= skeleton.attack   # call the attack method
        if zombie.health <= 0:
            zombie_alive = False
            print("zombie is dead!")
            break

    # Zombie attacks back
    damage = zombie.damage()
    skeleton.health -= damage
    print(f"Zombie attacks Skeleton for {damage} damage. Skeleton health: {skeleton.health}")
    if skeleton.health <= 0:
        skeleton_alive = False
        print("Skeleton perished!")
        break