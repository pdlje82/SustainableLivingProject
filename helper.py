class CortijoObject(object):
    """
    A base class for objects in the Cortijo project.

    Attributes
    ----------
    _name : str
        The name of the object, accessed through the name property.

    Methods
    -------
    display():
        Prints all attributes of the object, with special handling for list, GeoPoint, and dict attributes.
    display_missing():
        Returns a string with the names of attributes that are None or empty dictionaries.
    """
    def __init__(self):
        self._name = ''  # We use underscore to indicate this should be accessed via getter/setter

    # Create getter and setter functions
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Display functions
    def display(self):
        """
        Prints all attributes of the object, with special handling for list, GeoPoint, and dict attributes.

        If the attribute is a list, each item in the list is printed. If the attribute is a GeoPoint, the name
        of the GeoPoint is printed. If the attribute is a dict, each key-value pair in the dict is printed.
        """
        for attr, value in self.__dict__.items():
            attr = attr[1:] if attr.startswith('_') else attr  # Remove leading underscore if it exists
            if isinstance(value, list):
                print(f"{attr}:")
                for i, item in enumerate(value):
                    if hasattr(item, 'name'):
                        print(f"    {item.name}")
                    else:
                        print(f"    {item}")
            elif isinstance(value, GeoPoint):  # Handle GeoPoint objects
                print(f"{attr}: {value.name}")
            elif isinstance(value, dict):
                print(f"{attr}:")
                for key, val in value.items():
                    print(f"    {key}: {val}")
            else:
                print(f"{attr}: {value}")

    def display_missing(self):
        """
        Returns a string with the names of attributes that are None or empty dictionaries.

        If all attributes are set (i.e., not None and not empty dictionaries), returns a string indicating this.

        Returns
        -------
        str
            A string indicating which attributes are not set, or that all values are set.
        """
        missing_attributes = [attr for attr, value in self.__dict__.items() if value is None or value == {}]
        if missing_attributes:
            return "These values are not set: " + ", ".join(missing_attributes)
        else:
            return "All values are set."


class GeoPoint:
    """
    A class to represent a geographical point.

    Attributes
    ----------
    latitude : float
        The latitude of the point in decimal degrees.
    longitude : float
        The longitude of the point in decimal degrees.
    elevation : float, optional
        The elevation of the point in meters (default is None).

    Methods
    -------
    to_string():
        Returns a string representation of the point.
    """
    def __init__(self, latitude, longitude, elevation=None):
        self._name = ''
        if not (-90 <= latitude <= 90):
            raise ValueError("Invalid latitude value")
        if not (-180 <= longitude <= 180):
            raise ValueError("Invalid longitude value")
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation
        self.to_string()

    @property
    def name(self):
        """str: The name of the GeoPoint, which is a string representation of the point."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def to_string(self):
        if self.elevation is not None:
            self.name = f"{self.latitude},{self.longitude},{self.elevation}"
            return self.name
        else:
            self.name = f"{self.latitude},{self.longitude}"
            return self.name
