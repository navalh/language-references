CURRENT_YEAR = 2014

class Animal(object):
    def __init__(self):
        self.is_alive = True  # It's alive!!

class Pet(Animal):
    def __init__(self, name, year_of_birth, owner=None):
        Animal.__init__(self)   # call the parent's constructor
        self.name = name
        self.age = CURRENT_YEAR - year_of_birth
        self.owner = owner

    def eat(self, thing):
        self.talk()
        if thing == "poison":
            self.lose_life()
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print("..")

class Cat(Pet):
    """
    >>> my_cat = Cat("Furball", 2011, "Me", lives=2)
    >>> my_cat.talk()
    Meow!
    >>> my_cat.name
    'Furball'
    >>> my_cat.lose_life()
    >>> my_cat.is_alive
    True
    >>> my_cat.eat("poison")
    Meow!
    Furball ate a poison!
    >>> my_cat.is_alive
    False
    >>> my_cat.lose_life()
    'Cat is dead x_x'
    """
    def __init__(self, name, year_of_birth, owner, lives=9):
        assert type(lives) == int and  lives > 0
        Pet.__init__(self, name, year_of_birth, owner)
        self.lives = lives

    def talk(self):
        """A cat says 'Meow!' when asked to talk."""
        print('Meow!')

    def lose_life(self):
        """A cat can only lose a life if it has at least one
        life. When there are zero lives left, the 'is_alive'
        variable becomes False.
        """
        if self.lives > 0:
            self.lives = self.lives - 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print("'Cat is dead x_x'") 

class NoisyCat(Cat):
    """
    >>> my_cat = NoisyCat("Noisy Kitty", 2011, "Me", lives=1)
    >>> my_cat.talk()
    Meow!
    Meow!
    >>> my_cat.name
    'Noisy Kitty'
    >>> my_cat.lose_life()
    >>> my_cat.lose_life()
    'Cat is dead x_x'
    """
    def __init__(self, name, year_of_birth, owner, lives=9):
        Cat.__init__(self, name, year_of_birth, owner, lives)

    def talk(self):
        """A NoisyCat will always repeat what he/she said
        twice."""
        Cat.talk(self)
        Cat.talk(self)
