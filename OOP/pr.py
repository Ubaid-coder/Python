warrior_name = 'Thor'
warrior_health = 100
warrior_attack = 50

mage_name = 'Gandalf'
mage_health = 80
mage_attack = 70


def attack_warrior():
    print(f'Warrior attacks with power: ', warrior_attack)

def attack_mage():
    print(f'Mage attacks with power: ', mage_attack)
    
    
attack_warrior()
attack_mage()

print(hex(id(mage_attack)))