from helper import CortijoObject

class Building(CortijoObject):
    """
        A subclass of CortijoObject that represents a specific Building.

        Attributes
        ----------
        _buildingCost : dict
            The cost of constructing the Building, accessed through the buildingCost property.
        _houseSize : int or float
            The size of the house in square meters, accessed through the houseSize property.
        _rooms : list
            The rooms in the Building, accessed through the rooms property.
        _noOfRooms : int
            The number of rooms in the Building, updated whenever the rooms property is set.

        Methods
        -------
        no methods other than the ones inherited from CortijoObject
        """
    def __init__(self):
        super().__init__()
        self._buildingCost = {}
        self._houseSize = None
        self._rooms = []
        self._noOfRooms = None

    # Create getter and setter functions
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must be a string')
        self._name = value

    @property
    def buildingCost(self):
        return self._buildingCost

    @buildingCost.setter
    def buildingCost(self, value):
        # assuming b_type can be of any type
        if not isinstance(value, dict):
            raise ValueError('buildingCost must be a of type dict, i.e. {restoration: 1000}')
        self._buildingCost = value

    @property
    def houseSize(self):
        return self._houseSize

    @houseSize.setter
    def houseSize(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('houseSize must be a int or float')
        self._houseSize = value

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        if not isinstance(value, list):
            raise ValueError('rooms must be a list')
        self._rooms = value
        self._noOfRooms = len(value)


