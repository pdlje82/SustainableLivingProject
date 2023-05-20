Cortijo Cost Management System

This repository contains a Python-based cost management system for a property, referred to as "Cortijo". This system models the property and its associated entities as objects and utilizes object-oriented programming (OOP) principles to manage and calculate costs associated with the property. The system can also visualize the structure of the property and its entities as a graph using NetworkX and PyGraphviz libraries.
Classes

    Cortijo: Represents the property. It has attributes such as name and children to store the associated entities.

    CortijoChild and CortijoGrandChild: These classes represent the different entities associated with the property. They also have name and children attributes.

    Cost: Represents the different types of costs associated with each entity in the system. It can add, remove, modify and calculate total costs.

    Graph: Represents the property and its entities as a directed graph. It can draw the graph, which can then be saved as a PNG file or rendered to an in-memory image.

Usage

Here is a basic example of using these classes:

from estates import Cortijo
from structures import Building
from zones import Room
from helper import GeoPoint

from grapher import Graph
from ressources_finance import Cost
from storage import create_file, save_object, load_object

# set project dir and name
project_dir = 'data/'
filename = 'LosCigarrones_v1'
full_path = create_file(project_dir, filename)

cortijo = Cortijo()
cortijo.name = 'Los Cigarrones, Orgiva'
cortijo.landSize = 1900        # m^2
cortijo.location = GeoPoint(
    36.886978,                 # latitude
    -3.379498,                 # longitude
    400)                       # elevation
# adding costs
cortijo.add_cost('purchase', 75000)     # €
# display the properties of the Corijo
cortijo.display()
cortijo.display_missing()

# define the house
stoneHouse = Building()
stoneHouse.name = 'stoneHouse'
stoneHouse.houseSize = 54 # m^2
stoneHouse.add_child('rooms', [
    Room('kitchen'),
    Room('living room'),
    Room('private bedroom')
])
# adding costs
stoneHouse.add_cost('restoration', 5000)
# display the properties of the house
stoneHouse.display()
stoneHouse.display_missing()

# add the house to the Cortijo
cortijo.add_child('structures', [stoneHouse]

# draw a graph of all objects
graph_cortijo = Graph(cortijo)])
graph_cortijo.draw_graph(full_path, save=1)
# save project
save_object(cortijo, "data.pkl", full_path)

This example creates a property with one house, assigns some costs to the property and the house, calculates the total costs, and creates a graph of the property.

Installation

This project depends on the following Python libraries:

    NetworkX
    PyGraphviz
    IPython
    PIL

Please note that the project is currently in its initial stage and is subject to changes in its structure and functionality. Please ensure to check for updates frequently.
