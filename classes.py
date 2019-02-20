class spider:
    def __init__(self):
        self.name = 'Giant Spider'
        self.hp = 30
        self.mp = 0
        self.status_effects = {'poisonous':player.hp -= 5}
        self.location = 'c2'
        self.attack = 5
        self.defense = 5
        self.armor = 0
        

class goblin:
    def __init__(self):
        self.name = 'Angry Goblin'
        self.hp = 70
        self.mp = 0
        self.status_effects = {'stun':}
        self.location = 'a4'
        self.attack = 15
        self.defense = 15
        self.armor = 1


class witch:
    def __init__(self):
        self.name = 'Evil Witch'
        self.hp = 140
        self.mp = 80
        self.status_effects = {'curse':player.hp -= 15}
        self.location = 'a4'
        self.attack = 5
        self.magic_attack = 15
        self.defense = 20
        self.armor = 2


