class Animal():
    """
    A Class representing the Object Animal
    :param name: the Animal's name
    :type name: str
    :param hunger: the Animal's hunger level
    :type hunger: int
    """
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        Get the name of the animal
        :rtype: str
        """
        return self._name
    
    def is_hungry(self):
        """
        Check if the animal is hungry
        :rtype: bool
        """
        return self._hunger > 0
    
    def feed(self):
        """
        Feed the animal (Reduce hunger by 1)
        """
        self._hunger -= 1

    def talk(self):
        """
        Make the animal talk
        """
        pass

    def special_method(self):
        """
        Make the animal do its special ability
        """
        pass


class Dog(Animal):
    """
    Class to represent object from type Dog, inheriting from Class Animal
    :param name: the Dog's name
    :type name: str
    :param hunger: the Dog's hunger level
    :type hunger: int
    """
    
    def talk(self):
        print('woof woof')

    def fetch_stick(self):
        print('There you go, sir!')

    def special_method(self):
        self.fetch_stick()


class Cat(Animal):
    """
    Class to represent object from type Cat, inheriting from Class Animal
    :param name: the Cat's name
    :type name: str
    :param hunger: the Cat's hunger level
    :type hunger: int
    """
    
    def talk(self):
        print('meow')

    def chase_laser(self):
        print('Meeeeow')

    def special_method(self):
        self.chase_laser()
        

class Skunk(Animal):
    """
    Class to represent object from type Skunk, inheriting from Class Animal
    :param name: the Skunk's name
    :type name: str
    :param hunger: the Skunk's hunger level
    :type hunger: int
    :param stink_count: the Stink count of the Skunk
    :type stink_count: int
    """

    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        print('tsssss')

    def stink(self):
        print('Dear lord!')

    def special_method(self):
        self.stink()
        

class Unicorn(Animal):
    """
    Class to represent object from type Unicorn, inheriting from Class Animal
    :param name: the Unicorn's name
    :type name: str
    :param hunger: the Unicorn's hunger level
    :type hunger: int
    """

    def talk(self):
        print('Good day, darling')

    def sing(self):
        print('I\'m not your toy...')

    def special_method(self):
        self.sing()
        

class Dragon(Animal):
    """
    Class to represent object from type Dragon, inheriting from Class Animal
    :param name: the Dragon's name
    :type name: str
    :param hunger: the Dragon's hunger level
    :type hunger: int
    :param color: the Color of the Dragon
    :type color: str
    """

    def __init__(self, name, hunger=0, color='Green'):
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        print('Raaaawr')

    def breath_fire(self):
        print('$@#$#@$')

    def special_method(self):
        self.breath_fire()


def main():
    zoo_lst = [
        Dog('Brownie', 10),
        Cat('Zelda', 3),
        Skunk('Stinky', 0),
        Unicorn('Keith', 7),
        Dragon('Lizzy', 1450),

        Dog('Doggo', 80),
        Cat('Kitty', 80),
        Skunk('Stinky Jr.', 80),
        Unicorn('Clair', 80),
        Dragon('McFly', 80)
    ]

    for animal in zoo_lst:
        if animal.is_hungry():
            print(type(animal).__name__, animal.get_name())
        while animal.is_hungry():
            animal.feed()
        
        animal.talk()
        animal.special_method()

    print('Zoo name:', Animal.zoo_name)


if __name__ == '__main__':
    main()