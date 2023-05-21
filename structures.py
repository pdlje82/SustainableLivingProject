from helper import CortijoObject
import zones


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
            The number of rooms in the Building, updated whenever the rooms property is set.

        Methods
        -------
        no methods other than the ones inherited from CortijoObject
        """
    VALID_CHILD_TYPES = ["rooms"]
    def __init__(self):
        super().__init__()
        self._houseSize = None

    # Create getter and setter functions
    @property
    def houseSize(self):
        return self._houseSize

    @houseSize.setter
    def houseSize(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('houseSize must be a int or float')
        self._houseSize = value




