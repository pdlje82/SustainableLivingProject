from helper import CortijoObject
class RainWaterSystem(CortijoObject):
    VALID_CHILD_TYPES = {'Catchment area': 'This is the surface that directly receives the rainfall and provides '
                                            'water to the system. In most residential settings, this is the roof of '
                                            'your home. Make sure your catchment area is clean and free of any debris.',
                         'Gutters and Downspouts': 'These guide the rainwater from the catchment area to the storage '
                                                   'tanks. They need to be large enough to handle the volume of '
                                                   'water you are expecting.',
                         'Storage Tanks': 'The heart of any rainwater harvesting system, these tanks store your '
                                          'harvested water. They can be above ground or below ground, and made from a '
                                          'variety of materials such as polyethylene, metal, or concrete. Consider your '
                                          'storage capacity needs and the space available when choosing your tank(s).',
                         'Delivery and Pumping System': 'A pump is necessary if you want to use the stored water inside '
                                                        'your home or if your landscape irrigation system requires it. '
                                                        'The size of the pump needed depends on the amount of water to '
                                                        'be delivered and the delivery pressure required.',
                         'Water Purification System': 'If you are planning to use the harvested water for potable uses, '
                                                      'you will need a purification system. This can include sediment '
                                                      'filters, carbon filters, UV sterilizers, and potentially other'
                                                      'treatments depending on the quality of the rainwater and your'
                                                      'local regulations.',
                         'Water Organization Module(WOM)': 'This is an unique feature to Earthships.It is a modular '
                                                           'system that filters and directs water throughout the '
                                                           'Earthship.It typically includes a ceramic filter and a '
                                                           'carbon filter to purify the water for drinking.From the WOM,'
                                                           ' water is directed to fixtures and appliances.',
                         'Overflow and Drainage': 'An overflow system is necessary to divert excess water once the '
                                                  'storage tank is full. Good design of this system can also help to '
                                                  'manage any excess water in a way that minimizes erosion or other '
                                                  'water damage.',
                         'Maintenance': 'Regular maintenance is key to keeping the system working effectively. This can '
                                        'include cleaning gutters, inspecting and cleaning screens and filters, '
                                        'inspecting and servicing the pump, and occasionally cleaning the inside of the '
                                        'storage tank.'}
    def __init__(self):
        super().__init__()

    def valid_components(self):
        CortijoObject.print_valid_child_types()

class WasteWaterSystem(CortijoObject):
    VALID_CHILD_TYPES = {'Greywater and Blackwater Treatment': 'Earthships often include a system for treating '
                                                               'greywater (from sinks and showers) and blackwater (from '
                                                               'toilets). Greywater is typically filtered and used to '
                                                               'irrigate indoor and outdoor plantings. Blackwater is '
                                                               'treated in a contained system and can also be used for '
                                                               'non-edible plantings.'}
    def __init__(self):
        super().__init__()


class PhotovoltaicSystem(CortijoObject):
    VALID_CHILD_TYPES = ['Water', 'PV']
    def __init__(self):
        super().__init__()

