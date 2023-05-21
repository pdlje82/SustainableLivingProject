from estates import Cortijo
from structures import Building
from systems import RainWaterSystem, WasteWaterSystem
from zones import Room
from helper import GeoPoint

from grapher import Graph
from ressources_finance import Cost
from storage import create_file, save_object, load_object

# set project dir and name
project_dir = 'data/'
filename = 'LosCigarrones_v1'
full_path = create_file(project_dir, filename)

# create a Cortijo
cortijo = Cortijo()
cortijo.name = 'Los Cigarrones, Orgiva'
cortijo.landSize = 1900        # m^2
cortijo.location = GeoPoint(
    36.886978,                 # latitude
    -3.379498,                 # longitude
    400)                       # elevation

# adding costs
cortijo.add_cost('fixed', 'purchase', 75000)     # €

cortijo.display()
cortijo.display_missing()

# create a stoneHouse
stoneHouse = Building()
stoneHouse.name = 'stoneHouse'
stoneHouse.houseSize = 54 # m^2
stoneHouse.add_child('rooms', [
    Room('kitchen'),
    Room('living room'),
    Room('private bedroom')
])

# create a ruin
ruin = Building()
ruin.name = 'ruin guest house'
ruin.houseSize = 38 # m^2
ruin.add_child('rooms', [
    Room('guest bedroom 1'),
    Room('guest bedroom 2')
])

# adding costs
stoneHouse.add_cost( 'fixed', 'restoration', 5000)
ruin.add_cost('fixed', 'restoration', 20000)

stoneHouse.display()
stoneHouse.display_missing()
ruin.display()
ruin.display_missing()

# add the stone house and the ruin to the Cortijo
cortijo.add_child('structures', [stoneHouse, ruin])

cortijo.display()
cortijo.display_missing()

# understand the financials of the project
# find total costs

# show the network
graph_cortijo = Graph(cortijo)
graph_cortijo.draw_graph(full_path, save=0)

# add a rainwater system
rainWaterSystem = RainWaterSystem()
rainWaterSystem.name = 'rainwater system'
rainWaterSystem.print_valid_child_types()
rainWaterSystem.add_cost('fixed', 'purchase', 13000)

# add a wastewater system
wasteWaterSystem = WasteWaterSystem()
wasteWaterSystem.name = 'wastewater system'
wasteWaterSystem.print_valid_child_types()
rainWaterSystem.add_cost('fixed', 'purchase', 8000)

# add the water systems to the cortijo
cortijo.add_child('systems', [rainWaterSystem, wasteWaterSystem])

# show the new network
graph_cortijo = Graph(cortijo)
graph_cortijo.draw_graph(full_path, save=0)

costs = Cost()
fixed, running = costs.sum_costs(cortijo)
costs.plot_costs(fixed)