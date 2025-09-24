from abc import ABC , abstractclassmethod
from os import name


class Animal(ABC) :
    count = 0
    def __init__(self):
        Animal.count += 1
        