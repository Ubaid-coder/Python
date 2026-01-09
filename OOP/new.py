class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        
    def attack_enemy(self):
        print(f'{self.name} attacks with power {self.attack}')
        
        
warrior = Character('Thor',100,50)
mage = Character('Gandalf',80,70)
archer = Character('Archer',80,90)

warrior.attack_enemy()
mage.attack_enemy()
archer.attack_enemy()

"""
1- classes & objects
2- inheritance
3- encapsulation
4- abstraction
5- polymorphism

"""