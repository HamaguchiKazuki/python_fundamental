#6-1
class Thing:
    pass

print(Thing)

exsample = Thing()

print(exsample)

#6-2
class Thing2:
    letters = 'abc'

print(Thing2.letters)

#6-3
class Thing3:
    def __init__(self):
        self.letters = 'xyz'

something = Thing3()
print(something.letters)

#6-4
# class Element:
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#     def __str__(self):
#          return'name=%s, symbol=%s, number=%s' % (self.name, self.symbol, self.number)

#6-8 class

class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number

# element = Element('Hydrogen', 'H', 1)
# print(element.name, element.symbol, element.number)

#6-5
hydrogen_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
# hydrogen = Element(hydrogen_dict['name'], hydrogen_dict['symbol'], hydrogen_dict['number'])
# print(hydrogen.name, hydrogen.symbol, hydrogen.number)

#6-6
hydrogen = Element(**hydrogen_dict)
# hydrogen.dump()

#6-7
print(hydrogen)

#6-8
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)

#6-9

class Bear:
    def eats(self):
        return 'berries'


class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'


bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()

print(bear.eats(), rabbit.eats(), octothorpe.eats())

#6-10

class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
       return ''' I have many attachments:
                  My laser, to %s
                  My claw, to %s
                  My smartphone, to %s''' % (
           self.laser.does(),
           self.claw.does(),
           self.smartphone.does()
       )

robot = Robot()
print( robot.does() )

