#polymorphism with classes method overriding
class Bird():
    def sound(self):
        print('Birds make sounds')
        
class Crow(Bird):
    def sound(self):
        print('Crows say caw caw')
        
class Paroot(Bird):
    def sound(self):
        print('Parrot sounds, squawk')

bird1 = Crow()
bird2 = Paroot()

bird1.sound()
bird2.sound()