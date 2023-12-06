# These two lines add type-union support and create a real-number type.
from typing import Union
RealType = Union[int, float]

class Bag:
    """
    Implements the Bag of Holding

    Attributes:
    bagweight -- the empty (tare) weight of the bag, must be a real number
    names -- list of item names
    weights -- list of item weights
    """

    def __init__(self, bagweight=0):
        """Creates an empty Bag. Its weight can be specified.

        Arguments:
        bagweight -- the empty weight of the bag (default 0)

        >>> Bag(1.022).bagweight
        1.022
        >>> Bag(0).bagweight
        0
        >>> Bag().bagweight
        0
        """
        self.bagweight = bagweight
        self.names = []
        self.weights = []

    def add(self, itemname: str, itemweight: RealType) -> None:
        """ Adds a new item to the Bag. The function will do nothing if there
            is already another item with the same name (case-sensitive) in the
            bag.

            Returns nothing.

            >>> b = Bag()
            >>> b.count()
            0
            >>> b.add("stick", 1)
            >>> b.count()
            1
            >>> b.add("stick", 2)
            >>> b.count()
            1
            >>> b.add("sTick", 1.1)
            >>> b.count()
            2
        """
        if itemname not in self.names:
            self.names.append(itemname)
            self.weights.append(itemweight)


    def remove(self, itemname: str) -> tuple[str, RealType]:
        """ Removes the item identified by itemname from the Bag and
            returns the name and weight of the removed item as two variables.

            >>> b = Bag()
            >>> b.add("stone", 10)
            >>> b.remove("stone")
            ('stone', 10)
        """
        if itemname in self.names:
            index = self.names.index(itemname)
            self.names.pop(index)
            return itemname, self.weights.pop(index)

    def weight(self) -> RealType:
        """ Returns the total (gross) weight.
            This includes the bag itself and all the items inside.

            >>> b = Bag(20)
            >>> b.add("potion", 2)
            >>> b.weight()
            22
            >>> b.add("sauce", 0)
            >>> b.add("jerky", 10.9)
            >>> b.weight()
            32.9
        """
        return self.bagweight + sum(self.weights)

    def items(self) -> list[str]:
        """ Returns the list of all item names in the Bag.
            The sorting (order) is not enforced.

            >>> b = Bag()
            >>> b.add("potion", 3)
            >>> b.add("egg", 0.2)
            >>> b.add("cheese", 15)
            >>> sorted(b.items())
            ['cheese', 'egg', 'potion']
        """
        return self.names

    def dump(self) -> list[tuple[str, RealType]]:
        """ Completely empties the Bag and returns all items as a list of tuples
            [(itemname, itemweight), ...]. The item ordering is not enforced.

            >>> b = Bag()
            >>> b.add("potion", 2)
            >>> b.dump()
            [('potion', 2)]
        """
        dump_list = []
        for item in self.names:
            dump_list.append(self.remove(item))
        return dump_list

    def count(self) -> int:
        """ Returns the number (int) of items inside the bag.

            >>> b = Bag()
            >>> b.count()
            0
            >>> b.add("carrot", 1)
            >>> b.count()
            1
            >>> b.add("cake", 4)
            >>> b.count()
            2
        """
        return len(self.names)

    def addmany(self, itemlist: list[tuple[str, RealType]]):
        """ Similar to add, but many items at a time. The itemlist variable is a
            list of tuples [(itemname, itemweight), ...].

            >>> b = Bag()
            >>> b.addmany([("a", 1), ("b", 2)])
            >>> b.count()
            2
        """
        for item in itemlist:
            self.add(item[0], item[1])

    def removemany(self, namelist: list[str]) -> list[tuple[str, RealType]]:
        """ Similar to remove, but the argument is a list of names
            [itemname, ...]. The returned items are put into a list.

            >>> b = Bag()
            >>> b.addmany([("a", 1), ("b", 2)])
            >>> b.count()
            2
            >>> sorted(b.removemany(["b", "a"]))
            [('a', 1), ('b', 2)]
        """
        remove_list = []
        for item in namelist:
            remove_list.append(self.remove(item))
        return remove_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # Use the following line INSTEAD if you want to print all tests anyway.
    # doctest.testmod(verbose = True)
