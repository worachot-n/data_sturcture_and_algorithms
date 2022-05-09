from operator import getitem
from idna import valid_contextj


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0]*d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]
    
    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val 

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):                     # relies on len method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))                      # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other                        # rely on existing eq definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'      # adapt list representation

if __name__ in '__main__':
    vector = Vector(3)
    print(len(vector))
    print(getitem(vector, 0))
    print(vector.__setitem__(2, 1))
    print(vector.__add__([2, 2, 2]))
    print(vector.__eq__([0, 0, 1]))
    print(vector.__ne__([0, 0, 0]))
    print(str(vector))
