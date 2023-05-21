# from Buildings import Building
import structures
from helper import CortijoObject, GeoPoint


class Cortijo(CortijoObject):
    """
    A subclass of CortijoObject that represents a specific Cortijo.

    Attributes
    ----------
    _purchaseCost : int or float
        The cost of purchasing the Cortijo in euros, accessed through the purchaseCost property.
    _landSize : int or float
        The size of the land in square meters, accessed through the landSize property.
    _location : GeoPoint
        The geographical coordinates of the Cortijo, accessed through the location property.
    _children : dict of list
        A dictionary containing lists of child objects belonging to the Cortijo, accessed through the children property.
        Currently, the only key-value pair in the dictionary is 'buildings': [], where the value is a list of Building objects.

    Methods
    -------
    """
    VALID_CHILD_TYPES = ['structures', 'systems']
    def __init__(self):
        super().__init__()
        self._landSize = None  # in sqm
        self._location = None  # latitude DD, longitude DD

    # Create getter and setter functions
    @property
    def landSize(self):
        return self._landSize

    @landSize.setter
    def landSize(self, value):
        self._landSize = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if isinstance(value, GeoPoint):
            self._location = value
        else:
            raise TypeError("Expected a GeoPoint instance")
