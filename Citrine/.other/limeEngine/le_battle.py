from le_colors import colored

class Entity():
    def __init__(self):
        pass
    def skill(self):
        pass
    def attack(self):
        pass

class Player(Entity):
    def __init__(self, name = "Player"):
        self.name = name
        self.color = 'green'
        self.health = 10
        self.damage = 2
        self.level = 1
        self.skill = 0
        self.skill_treshhold = 5
        self.initiative = 5
        self.stats = self.updateStats()

    def setSkill(self):
        _skill = '['
        for i in range(self.skill_treshhold):
            if i < self.skill:
                _skill += '■'
            else:
                _skill += ' '
        _skill += ']'
        return str(_skill)

    def updateStats(self):
        return (" [" + colored("H:%i " % self.health, 'red') + colored("D:%i " % self.damage, 'blue') + colored("S:%s " % self.setSkill(), 'yellow') + "] ")

    def levelUp(self, num = 1):
        self.level += num
        self.health += num * 2
        self.damage += num

class Wolf(Entity):
    def __init__(self):
        self.name = "Wolf"
        self.color = 'bright_black'
        self.health = 5
        self.damage = 1
        self.skill = 0
        self.skill_treshhold = 3
        self.initiative = 2
        self.stats = self.updateStats()

    def setSkill(self):
        _skill = '['
        for i in range(self.skill_treshhold):
            if i < self.skill:
                _skill += '■'
            else:
                _skill += ' '
        _skill += ']'
        return str(_skill)

    def updateStats(self):
        return (" [" + colored("H:%i " % self.health, 'red') + colored("D:%i " % self.damage, 'blue') + colored("S:%s " % self.setSkill(), 'yellow') + "] ")

    def useSkill(self):
        self.skill_name = "Pack Power"
        self.skill_description = "Wolf is using skill!\nWolf is summonning 1 Wolf!"
        #summon()
        print(self.skill_description)

    def attack(self):
        if self.skill == self.skill_treshhold:
            self.useSkill()
        else: print()


def attack(entity1, entity2):
    print("\n\n" + colored(entity1.name, entity1.color) + " is " + entity1.stats + "\n" + colored(entity1.name, entity1.color) + " deal " + str(entity1.damage) + " damage to " + colored(entity2.name, entity2.color) + "!")
    entity2.health -= entity1.damage
    print(colored(entity2.name, entity2.color) + " health is down to " + str(entity2.health) + ".")
    if entity2.health <= 0:
        print("\n" + colored(entity2.name, entity2.color) + " is defeated! Congratulations!")
        return True
    else:
        return False

def battle(player, enemy):
    '''
    player = ''
    for entity in entity_list:
        if isinstance(entity, Player):
            player = entity
    entity_list.remove(player)
    '''

    turn = 0
    _exit = False
    while not _exit:
        turn += 1
        if turn % 2 != 0:
            _exit = attack(player, enemy)
        else:
            _exit = attack(enemy, player)
    print(colored("\nBattle is finished!\n", 'yellow'))


battle(Player(), Wolf())
