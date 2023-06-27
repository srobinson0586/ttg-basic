class Infinity:
    """ A class to represent infinity.

    This allows us to perform arithmetic and comparisons with infinity
    during graph operations. You can represent edges that don't exist
    with an edge with infinite length. """
    ### This lets us print it out as the unicode infinity sign.
    def __str__(self):
        return chr(0x221e)
    def __repr__(self):
        return self.__str__()

    ### These functions allow all comparisons.
    def __lt__(self, n):
        return False
    def __eq__(self, n):
        rtn = False
        if isinstance(n, Infinity):
            return True
        return rtn
    def __gt__(self, n):
        return not (self < n or self == n)
    def __le__(self, n):
        return self < n or self == n
    def __ge__(self, n):
        return self > n or self == n

    ### These functions allow addition to integers.
    def __add__(self, n):
        return self
    def __radd__(self, n):
        return self + n
