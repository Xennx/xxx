import time, random, pygame
enemyAtk = 0
enemyArm = 0
enemyDmg = 0
enemyDice = 0
heroDice = 0
act = 0
itype = 0
ichanse = 0
istat = 0
say = 0
move = 0

class Hero():
    def __init__(self, name, kind, place, home = 'Sea', battle = 'great', level = 1, exp = 0, atk = 1, arm = 4, hp = 3, usualhp = 3):
        self.name = name
        self.kind = kind
        self.home = home
        self.place = place
        self.level = level
        self.battle = battle
        self.exp = exp
        self.atk = atk
        self.arm = arm
        self.hp = hp
        self.usualhp = usualhp
        print('Write a name')
        self.name = input()
        print(self.name + ' created')
        
        print(self.name + ' stats: Atk = ' + str(self.atk) + ' Arm = ' + str(self.arm) + ' Hp = ' + str(self.hp) + ' Level = ' + str(self.level))

    def level_up(self):
        if self.battle == 'died':
            print('you died, restart the game')
        else:
            if self.exp >= 200 and self.level == 1:
                self.level = 2
                self.atk += 1
                self.arm += 2
                self.hp += 2
                self.usualhp += 2
                print(self.name + 'leveled up')
                print(self.name + ' stats: Atk = ' + str(self.atk) + ' Arm = ' + str(self.arm) + ' Hp = ' + str(self.hp) + ' Level = ' + str(self.level))
            elif self.exp >= 500 and self.level == 2:
                self.level = 3
                self.atk += 2
                self.arm += 3
                self.hp += 3
                self.usualhp += 3
                print(self.name + 'leveled up')
                print(self.name + ' stats: Atk = ' + str(self.atk) + ' Arm = ' + str(self.arm) + ' Hp = ' + str(self.hp) + ' Level = ' + str(self.level))
            elif self.exp >= 1000 and self.level == 3:
                self.level = 4
                self.atk += 3
                self.arm += 4
                self.hp += 4
                self.usualhp += 4
                print(self.name + 'leveled up')
                print(self.name + ' stats: Atk = ' + str(self.atk) + ' Arm = ' + str(self.arm) + ' Hp = ' + str(self.hp) + ' Level = ' + str(self.level))
            else:
                print(self.name + ' not enough exp')

    def gohome(self):
        if self.battle == 'died':
            print('you died, restart the game')
        else:
            print(self.name + ' go to ' + self.home)
            time.sleep(5)
            print(self.name + ' arrived to ' + self.home)
            self.exp += 5
            print(self.name + ' exp = ' + str(self.exp))
            
    def status(self):
        if self.battle == 'died':
            print('you died, restart the game')
        else:
            print(self.name + ' stats: Atk = ' + str(self.atk) + ' Arm = ' + str(self.arm) + ' Hp = ' + str(self.hp) + ' Level = ' + str(self.level))

    def go_place(self):
        if self.battle == 'died':
            print('you died, restart the game')
        else:
            self.place = input()
            print(self.name + ' go to ' + self.place)
            time.sleep(10)
            print(self.name + ' arrived to ' + self.place)
            if self.place == 'Healing Fountain':
                if self.hp < self.usualhp:
                    self.hp = self.usualhp
                    print(self.name + ' heal up')
                    print(self.name + ' stats: Atk = ' + str(self.atk) + ' Arm = ' + str(self.arm) + ' Hp = ' + str(self.hp) + ' Level = ' + str(self.level))
                else:
                    print('You didnt need healing')
            else:
                if self.level == 1:
                    chanse_enemy = random.randint(1, 2)
                    enemyAtk = random.randint(1, 2)
                    enemyArm = random.randint(3, 5)
                    enemyDmg = random.randint(1, 2)
                elif self.level == 2:
                    chanse_enemy = random.randint(1, 2)
                    enemyAtk = random.randint(1, 3)
                    enemyArm = random.randint(3, 6)
                    enemyDmg = random.randint(1, 3)
                elif self.level == 3:
                    chanse_enemy = random.randint(1, 2)
                    enemyAtk = random.randint(2, 4)
                    enemyArm = random.randint(4, 7)
                    enemyDmg = random.randint(2, 4)
                elif self.level == 4:
                    chanse_enemy = random.randint(1, 2)
                    enemyAtk = random.randint(2, 5)
                    enemyArm = random.randint(4, 8)
                    enemyDmg = random.randint(2, 5)
                    
                if chanse_enemy == 1:
                    print('Battle! ' + 'Attack = ' + str(enemyAtk) + ' Armor = ' + str(enemyArm) + ' Damage = ' + str(enemyDmg))
                    print(self.name + ' stats: Atk = ' + str(self.atk) + ' Arm = ' + str(self.arm) + ' Hp = ' + str(self.hp) + ' Level = ' + str(self.level))
                    self.battle = 'conlose'
                    while self.battle == 'conlose':
                        print('Write t if you want to throw or l if you want to run away')
                        act = input()
                        if act == 't':
                            print('Throwing your and enemy dice')
                            time.sleep(4)
                            heroDice = random.randint(1, 6)
                            enemyDice = random.randint(1, 6)
                            print('Your dice number is ' + str(heroDice))
                            print('Enemy dice number is ' + str(enemyDice))
                            if enemyDice + enemyAtk > self.arm:
                                self.hp -= enemyDmg 
                                print('Enemy damaged you. Your hp = ' + str(self.hp))
                                print(self.name + ' stats: Atk = ' + str(self.atk) + ' Arm = ' + str(self.arm) + ' Hp = ' + str(self.hp) + ' Level = ' + str(self.level))
                                if self.hp < 1:
                                    self.battle = 'died'
                                    print(self.name + ' died. Please restart the game')
                                elif self.hp > 0:
                                    self.battle = 'live'
                            
                            else:
                                print('Enemy not damaged you')
                                self.battle = 'live'
                            if heroDice + self.atk > enemyArm:
                            
                                print('You killed an enemy')
                                if self.battle == 'died':
                                    print(self.name + ' died. Please restart the game')
                                elif self.battle == 'live':
                                    self.battle = 'victory'
                                    self.exp += 50
                                    print(self.name + ' exp = ' + str(self.exp))
                                    print('if you have 200 exp and want to level up summon method "alan.level_up()"')
                                       
                                        

                            else:
                                print('You didnt killed an enemy')
                                if self.battle == 'died':
                                    print(self.name + ' died. Please restart the game')
                                else:
                                    self.battle = 'conlose'
                                    
                            if self.battle == 'victory':
                                if self.level == 1:
                                    ichanse = random.randint(1, 2)
                                    itype = random.randint(1, 3)
                                    istat = random.randint(1, 3)
                                elif self.level == 2:
                                    ichanse = random.randint(1, 2)
                                    itype = random.randint(1, 3)
                                    istat = random.randint(3, 5)
                                elif self.level == 3:
                                    ichanse = random.randint(1, 2)
                                    itype = random.randint(1, 3)
                                    istat = random.randint(4, 6)
                                if ichanse == 1:
                                    print('You have got an item! Do you want to equip it?')                            
                                    if itype == 1:
                                        print('Atk = ' + str(istat))
                                        say = input()
                                        if say == 'yes':
                                            self.atk = istat
                                            print('Equiped!')
                                        else:
                                            print('Nothing')
                                    if itype == 2:
                                        print('Arm = ' + str(istat))
                                        say = input()
                                        if say == 'yes':
                                            self.arm = istat
                                            print('Equiped!')
                                        else:
                                            print('Nothing')
                                    if itype == 3:
                                        print('hp = ' + str(istat))
                                        say = input()
                                        if say == 'yes':
                                            self.hp = istat
                                            self.usualhp = istat
                                            print('Equiped!')
                                        else:
                                            print('Nothing')
                                else:
                                    print(self.name + ' didnt find an item')
                        
                            
                                    
                        elif act == 'l':
                            self.battle = 'leave'
                            print ('you leaved the battle')
                            self.exp += 5
                            print(self.name + ' exp = ' + str(self.exp))
                        
                else:
                    print('No battle! ' + str(enemyAtk) + ' ' + str(enemyArm) + ' ' + str(enemyDmg))
                    self.exp += 10
                    print(self.name + ' exp = ' + str(self.exp))
                    
    def restart(self):
        self.place = 'Russia'
        self.level = 1
        self.exp = 0
        self.atk = 1
        self.arm = 4
        self.hp = 3
        self.usualhp = 3
        print(self.name + ' stats: Atk = ' + str(self.atk) + ' Arm = ' + str(self.arm) + ' Hp = ' + str(self.hp) + ' Level = ' + str(self.level) + ' Exp = ' + str(self.exp))
            
        
r = Fish('Alan', 'shark', 'Russia', 'Russia')

while move != 'quit':
    move = input('Your move is = ')
    if move == 'place':
        r.go_place()
    elif move == 'restart':
        r.restart()
    elif move == 'levelup':
        r.level_up()
    elif move == 'gohome':
        r.gohome()
    elif move == 'status':
        r.status()
    elif move == 'efrg':
        print('Welcome back!')
