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

cortijo.display()
cortijo.display_missing()

stoneHouse = Building()
stoneHouse.name = 'stoneHouse'
stoneHouse.houseSize = 54 # m^2
stoneHouse.add_child('rooms', [
    Room('kitchen'),
    Room('living room'),
    Room('private bedroom')
])


ruin = Building()
ruin.name = 'ruin guest house'
ruin.houseSize = 38 # m^2
ruin.add_child('rooms', [
    Room('guest bedroom 1'),
    Room('guest bedroom 2')
])

# adding costs
stoneHouse.add_cost('restoration', 5000)
ruin.add_cost('restoration', 20000)

stoneHouse.display()
stoneHouse.display_missing()

ruin.display()
ruin.display_missing()

cortijo.add_child('structures', [stoneHouse, ruin])

cortijo.display()
cortijo.display_missing()

# understand the financials of the project
# find total costs

costs = Cost()
total_cost = costs.sum_costs(cortijo)
print(total_cost)
print('')
