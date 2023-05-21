from ressources_finance import Cost
class CortijoObject(object):
    """
    A base class for objects in the Cortijo project.

    Attributes
    ----------
    _name : str
        The name of the object, accessed through the name property.
    _children : dict
        A dictionary storing the child objects associated with the object, accessed through the getter method get_children.

    Methods
    -------
    add_child(child_type, child):
        Adds a child of the specified type to the object's _children dictionary, if it is not already present.
    remove_child(child_type, child):
        Removes a child of the specified type from the object's _children dictionary.
    get_children():
        Returns a list of all child objects associated with the object.
    display():
        Prints all attributes of the object, with special handling for list, GeoPoint, and dict attributes.
    display_missing():
        Returns a string with the names of attributes that are None or empty dictionaries or lists.
    """
    VALID_CHILD_TYPES = ["not defined!"]
    def __init__(self):
        self._name = ''  # We use underscore to indicate this should be accessed via getter/setter
        self._children = {}
        self._cost = Cost()  # initialize cost dictionary

    # Create getter and setter functions
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def add_child(self, child_type, child=None):
        """
        Adds a child of the specified type.

        Parameters
        ----------
        child_type : str
            The type of child object(s) to be added. This is used as the key in the _children dictionary.
        child : object or list of objects, optional
            The child object(s) to be added. This can be a single object or a list of objects.
            If no child is provided, this method simply ensures that the _children dictionary has an entry for the specified child_type.

        Notes
        -----
        If the child_type does not exist yet in the _children dictionary, this method initializes it with an empty list.
        If a child (or list of children) is provided, it appends (or extends) the child object(s) to the list for the specified child_type in the _children dictionary.
        """
        if child_type not in self.VALID_CHILD_TYPES:
            raise ValueError(f"{child_type} is not a valid child type")

        # If the child type does not exist yet, initialize it with an empty list
        if child_type not in self._children:
            self._children[child_type] = []

        # If a child is provided, add the child to the appropriate list
        if child is not None:
            # Check if the child is a list of objects
            if isinstance(child, list):
                # Extend the list for this child_type with the new list of children
                self._children[child_type].extend(child)
            else:
                # Append the single child object to the list for this child_type
                self._children[child_type].append(child)


    def get_children(self):
        all_children = []
        for child_type in self._children:
            all_children.extend(self._children[child_type])
        return all_children

    def add_cost(self, cost_type, amount):
        self._cost.add_cost(cost_type, amount)

    # Display functions
    def display(self):
        """
        Prints all attributes of the object, with special handling for list, GeoPoint, dict attributes,
        children attributes, and Cost attributes.
        """
        # Iterate over all attributes of the object
        for attr, value in self.__dict__.items():
            # Remove leading underscore if it exists from attribute's name for cleaner output
            attr = attr[1:] if attr.startswith('_') else attr

            # Case 1: If attribute is a list, print each item in the list
            if isinstance(value, list):
                print(f"{attr}:")
                for i, item in enumerate(value):
                    # If item has a 'name' attribute, print the name, otherwise print the item itself
                    if hasattr(item, 'name'):
                        print(f"    {item.name}")
                    else:
                        print(f"    {item}")
            # Case 2: If attribute is a GeoPoint object, print the name of the GeoPoint
            elif isinstance(value, GeoPoint):
                print(f"{attr}: {value.name}")

            # Case 3: If attribute is a Cost object, iterate over its costs dictionary to print the costs
            elif isinstance(value, Cost):
                print(f"{attr}:")
                for cost_type, amount in value.costs.items():
                    print(f"    {cost_type}: {amount}€")

            # Case 4: If attribute is the 'children' dictionary, print the type of child objects
            #         and the names of each child object under that type
            elif isinstance(value, dict) and attr == "children":
                print(f"{attr}:")
                for child_type, children in value.items():
                    print(f"    {child_type}:")
                    for child in children:
                        if hasattr(child, 'name'):
                            print(f"        {child.name}")

            # Case 5: If attribute is any other dictionary, print each key-value pair in the dict
            elif isinstance(value, dict):
                print(f"{attr}:")
                for key, val in value.items():
                    print(f"    {key}: {val}")

            # Case 6: If attribute is none of the above types, simply print the attribute's name and value
            else:
                print(f"{attr}: {value}")
        print('\n')

    def display_missing(self):
        """
            Returns a string with the names of attributes that are None, empty dictionaries, or empty lists.

            If the attribute is the 'children' dict, it will also check if the list of child objects under
            each type is empty. If it is, it will add the type of those child objects to the list of missing attributes.

            If all attributes are set (i.e., not None, not empty dictionaries, and not empty lists, and there
            are child objects for all types in the 'children' attribute), returns a string indicating this.

            Returns
            -------
            str
                A string indicating which attributes are not set, or that all values are set.
            """
        missing_attributes = []

        for attr, value in self.__dict__.items():
            attr = attr[1:] if attr.startswith('_') else attr  # Remove leading underscore if it exists

            # Check for None or empty values
            if value is None or value == {} or value == []:
                missing_attributes.append(attr)

            # Check for empty child lists
            if attr == "children":
                for child_type, children in value.items():
                    if not children:
                        missing_attributes.append(child_type)

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
