from classes import Monsters

from random import randint
def roll_die(die_used):
    return randint(1, die_used)
    print(roll_die(6))




skeleton = Monsters("Skeleton", 4, 1, 10)
zombie = Monsters("Zombie", 2, 2, 10)

#print(f"skeleton : {skeleton.attack}")
#print(f"zombie : {zombie.attack}")

#skeleton.health_check()
#zombie.health_check()

damage = roll_die(6)
#skeleton.take_damage(damage)
zombie.take_damage(damage)