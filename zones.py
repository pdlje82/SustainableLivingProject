from helper import CortijoObject

class Room(CortijoObject):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._roomSize = None

    # Create getter and setter functions
    @property
    def roomSize(self):
        return self._roomSize

    @roomSize.setter
    def roomSize(self, value):
        self._roomSize = value

