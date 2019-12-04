class Animal:
    '''

    '''

    def __init__(self, legs, species, color):
        self._legs = legs
        self._species = species
        self._color = color

    def get_color(self):
        '''
        Returns the Animal's color
        '''
        return self._color

    def __repr__(self):
        '''
        Returns all of the Animal's data
        '''
        return f"{self._species}: {self._color}, {self._legs} legs"


class Dog(Animal):
    def __init__(self, color):
        super().__init__(4, "Dog", color)


class Bird(Animal):
    def __init__(self, color):
        super().__init__(2, "Bird", color)


class Fish(Animal):
    def __init__(self, color):
        super().__init__(0, "Fish", color)


print(Dog("brown"))
print(Bird("blue"))
print(Fish("orange"))
