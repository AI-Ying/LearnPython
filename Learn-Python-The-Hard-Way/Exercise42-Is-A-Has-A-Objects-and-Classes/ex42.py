# -*- coding: utf-8 -*-

## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    print "I am a Animal"

## ??
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name
        print "I am a Dog, my name is %s" % self.name

## ??
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name
        print "I am a Cat, my name is %s" % self.name

##??
class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name
        print "I am a person, my name is %s" % self.name

        ## Person has-a pet of some kind
        self.pet = None
        print "I have a pet who is %s" % self.pet

## ??
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary
        print "I am Employee, my name is %s and my salary are %s" %(self.name, self.salary)

## ??
class Fish(object):
    print "I a Fish"
## ??
class Salmon(Fish):
    print "I am a kind of Fish:Salmon "

## ??
class Halibut(Fish):
    print "I am a kind of Fish:Halibut "

## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
