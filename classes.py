
from random import randint

def roll_die(die_used):
    return randint(1, die_used)
    print(roll_die(6))

class Monsters:
    # these are the attribute that the monster class has
    def __init__(self, monster_id, attack_die, monster_defence, monster_health):
        self.id = monster_id
        self.attack = attack_die
        self.defence = monster_defence
        self.health = monster_health
        self.total = 0

    # these are the methods that the monster class can do
    def count(self):
        self.total += 1

    def health_check(self):
        if self.health > 0:
            print(f"{self.id} is still coming towards you")
        else:
            print(f"{self.id} is permanently dead")

    def take_damage(self, damage_taken):
        self.health -= damage_taken + self.defence
        print(f"{self.id} takes {damage_taken} damage! Remaining health : {self.health}")
        if 0 >= self.health:
            print(f"{self.id} is dead")

    def damage(self):
        damage_roll = roll_die(self.attack)
        return damage_roll


skeleton = Monsters("skeleton", 4,2,6)
zombie = Monsters("zombie", 8,1,10)
#print(f"skeleton damage = ",skeleton.damage())
#print(f"zombie damage = ",zombie.damage())