from random import randint


def roll_die(die_used):
    return randint(1, die_used)


class Player:
    # these attributes are the skills and the things the player has
    def __init__(self, Id, detection_skill, hide_skill, attack_die, defend_skill, health):
        #attributes that are skills
        self.detect = detection_skill
        self.hide = hide_skill
        self.damage_roll = roll_die(attack_die)
        self.block_damage = defend_skill
        self.health = health

    def detect(self):
        if self.detect >= monster.hide




player_one = Player("player_one",5, 3, 8,6,25)
player_two = Player("player_two",7,5,6,4,15)