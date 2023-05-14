# from Buildings import Building
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
    _buildings : list of Building
        A list of buildings located in the Cortijo, accessed through the buildings property.

    Methods
    -------
    add_building(building: Building):
        Adds a Building object to the list of buildings in the Cortijo.
    """
    def __init__(self):
        super().__init__()
        self._purchaseCost = None  # in €
        self._landSize = None  # in sqm
        self._location = None  # latitude DD, longitude DD
        self._buildings = []  # list to store Building objects

    # Create getter and setter functions
    @property
    def purchaseCost(self):
        return self._purchaseCost

    @purchaseCost.setter
    def purchaseCost(self, value):
        self._purchaseCost = value

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

    # add and remove objects to and from the cortijo
    def add_building(self, building):
        """
        Adds a Building object to the list of buildings in the Cortijo.

        Parameters
        ----------
        building : Building
            The building to be added to the Cortijo.

        Raises
        ------
        TypeError
            If the building is not an instance of Building.
        """
        if isinstance(building, Building):
            self._buildings.append(building)
        else:
            raise TypeError("Expected a Building object.")
