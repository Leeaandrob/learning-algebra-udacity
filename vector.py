# coding: utf-8
from array import array


class Vector(object):
    def __init__(self, coordinates):
        self.coordinates = array('d', coordinates)

    def __iter__(self):
        return (i for i in (self.coordinates))

    def __eq__(self, vector):
        return tuple(self.coordinates) == tuple(vector)

    def __repr__(self):
        return "Vector - {0}".format(str([i for i in self.coordinates]))

    def __str__(self):
        return str(tuple(self))

    def __get__(self):
        return self.coordinates

    def __getitem__(self, position):
        return self.coordinates[position]

    def __add__(self, other):
        return list(map(lambda x, y: round(x+y, 3), self.coordinates, other))

    def __sub__(self, other):
        return list(map(lambda x, y: round(x-y, 3), self.coordinates, other))

    def __mul__(self, scalar):
        return Vector([round(scalar * x, 3) for x in self.coordinates])
