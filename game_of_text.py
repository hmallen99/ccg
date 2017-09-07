class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data=newdata

    def setNext(self,newnext):
        self.next=newnext

class UnorderedList:
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head==None

    def enqueue(self,item):
        if self.head==None:
            self.head=Node(item)
        else:
            current=self.head
            while current.getNext() != None:
                current=current.getNext()
            current.setNext(Node(item))

class Player:
    def __init__(self,health,attack,mana,armor):
        self.health=health
        self.attack=attack
        self.mana=mana
        self.armor=armor

    def is_alive(self):
        if self.health > 0:
            return 1
        else:
            return 0

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def get_armor(self):
        return self.armor

    def set_attack(self,attack):
        self.attack=attack

    def set_armor(self,armor):
        self.armor = armor

    def set_mana(self,mana):
        self.mana = mana

    def set_health(self,health):
        self.health = health

class Minion:
    def __init__(self):
        self.minion_health = 0
        self.mana_cost = 0
        self.attack_ability = 0
        self.minion_attack = 0

    def get_mana_cost(self):
        return self.mana_cost

    def get_minion_health(self):
        return self.minion_health

    def get_minion_attack(self):
        return self.minion_attack

    def set_minion_attack(self, minion_attack):
        self.minion_attack = minion_attack

    def set_minion_health(self, minion_health):
        self.minion_health = minion_health

class FootSoldier(Minion):
    def __init__(self):
        Minion.__init__(self)
        self.minion_health = 400
        self.mana_cost = 2
        self.attack_ability = 1
        self.minion_attack = 100

class brienne(Player):
    def __init__(self, health, attack, mana, armor):
        Player.__init__(self, health, attack, mana,armor)
        self.name="Brienne"

    def special_move(self):
        self.armor=self.armor+100
        self.attack=self.attack+25

class arya(Player):
    def __init__(self, health, attack, mana, armor):
        Player.__init__(self, health, attack, mana,armor)
        self.name="Arya"

    """bleed effect: have a function detecting if special is used, do function"""
    def special_move(self):
        self.attack=self.attack*2


class jon(Player):
    def __init__(self, health, attack, mana, armor):
        Player.__init__(self, health, attack, mana,armor)
        self.name="Jon"

    def special_move(self):
        self.armor=self.armor+50
        self.attack=self.attack+25

class jaime(Player):
    def __init__(self, health, attack, mana, armor):
        Player.__init__(self, health, attack, mana,armor)
        self.name="Jaime"

    def special_move(self):
        self.armor=self.armor+75
        self.attack=self.attack+50

class daenerys(Player):
    def __init__(self, health, attack, mana, armor):
        Player.__init__(self, health, attack, mana,armor)
        self.name="Daenerys"

    def special_move(self):
        self.armor=self.armor-25
        self.attack=self.attack+100

class game:
    def __init__(self):
        self.execute()
        """choose players
           1. Brienne of Tarth
           2. Jon Snow
           3. Daenerys Targaryen
           4. Jaime Lannister
           5. Arya Stark"""

    def execute(self):
        choose_player1 = int(input("player 1 choose"))
        choose_player2 = int(input("player 2 choose"))
        if choose_player1 == 1:
            self.player1 = brienne(3000,150,0,0)
            print("Player 1 is Brienne")
        elif choose_player1 == 2:
            self.player1 = jon(2750,200,0,0)
            print("Player 1 is Jon")
        elif choose_player1 == 3:
            self.player1 = daenerys(2000,200,0,0)
            print("Player 1 is Daenerys")
        elif choose_player1 == 4:
            self.player1 = jaime(2750,250,0,0)
            print("Player 1 is Jaime")
        elif choose_player1 == 5:
            self.player1= arya(1750,200,0,0)
            print("Player 1 is Arya")
        else:
            print("Character not found")

        if choose_player2 == 1:
            self.player2 = brienne(3000,150,0,0)
            print("Player 2 is Brienne")
        elif choose_player2 == 2:
            self.player2 = jon(2750,200,0,0)
            print("Player 2 is Jon")
        elif choose_player2 == 3:
            self.player2 = daenerys(2000,200,0,0)
            print("Player 2 is Daenerys")
        elif choose_player2 == 4:
            self.player2 = jaime(2750,250,0,0)
            print("Player 2 is Jaime")
        elif choose_player2 == 5:
            self.player2= arya(1750,200,0,0)
            print("Player 2 is Arya")
        else:
            print("Character not found")
        turn = 0
        while self.player1.is_alive() and self.player2.is_alive():
            print("turn")
            if turn == 0:
                self.player_action(self.player1,self.player2)
                print(self.player1.get_health(), " ", self.player2.get_health())
                turn = turn + 1
            elif turn == 1:
                self.player_action(self.player2,self.player1)
                print(self.player1.get_health(), " ", self.player2.get_health())
                turn = turn - 1
        print("Game Over")

    def player_action(self,player_x,player_y):
        print("1. Draw")
        print("2. Attack")
        print("3. Special Move")
        player_move=int(input("What is your move?"))
        if player_move == 1:
            print("draw")
        elif player_move == 2:
            print("attack")
            if player_y.get_armor() > 0:
                temp_attack =  player_x.get_attack() - player_y.get_armor()
                if temp_attack < 0:
                    player_y.set_armor(-temp_attack)
                else:
                    player_y.set_armor(0)
                    player_y.set_health(player_y.get_health()-temp_attack)
            else:
                player_y.set_health(player_y.get_health()-player_x.get_attack())
        elif player_move == 3:
            temp=player_x.get_attack()
            player_x.special_move()
            player_y.set_health(player_y.get_health()-player_x.get_attack())
            player_x.set_attack(temp)

henry = game()
