class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.attack = 0
        self.original_attack = 0
        self.magic_attack = 0
        self.defense = 0
        self.original_defense = 0
        self.armor = 0
        self.luck = 0
        self.backpack = {}
        self.location = "Room of Altar"
        self.game_over = False



class spider:
    def __init__(self):
        self.name = 'Giant Spider'
        self.hp = 170
        self.mp = 0
        self.status_effects = {'poisonous':-5}
        self.location = 'c2'
        self.attack = 5
        self.original_attack = 5
        self.defense = 5
        self.original_defense = 5
        self.armor = 0
        self.backpack = {"fragment": '2HS'}      


class goblin:
    def __init__(self):
        self.name = 'Angry Goblin'
        self.hp = 330
        self.mp = 0
        self.status_effects = {'stun':0}
        self.location = 'a4'
        self.attack = 15
        self.defense = 15
        self.armor = 1


class witch:
    def __init__(self):
        self.name = 'Evil Witch'
        self.hp = 440
        self.mp = 80
        self.status_effects = {'curse': -15}
        self.location = 'a4'
        self.attack = 5
        self.magic_attack = 15
        self.defense = 20
        self.armor = 2


class boss:
    def __init__(self):
        self.name = 'Clan traitor'
        self.hp = 700
        self.mp = 80
        self.status_effects = {'icy touch': -15}
        self.location = 'c3'
        self.attack = 15
        self.magic_attack = 20
        self.defense = 25
        self.armor = 5


