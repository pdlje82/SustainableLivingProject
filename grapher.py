import os
import networkx as nx
from networkx.drawing.nx_agraph import to_agraph
from IPython.display import Image
from PIL import Image
import io



class Graph:
    """
    A class to represent a Cortijo and its associated entities (children and grandchildren) as a directed graph.

    Attributes
    ----------
    G : nx.DiGraph
        A directed graph from the NetworkX library to store the nodes and edges.
    cortijo : CortijoObject
        The Cortijo object to be represented in the graph.

    Methods
    -------
    draw_graph(project_dir: str, save: int = 0) -> Image
        Creates the nodes and edges in the graph based on the Cortijo's children and grandchildren.
        If the 'save' argument is 1, it saves the graph as a .png image file in the specified project directory.
        If 'save' is 0 (default), it renders the graph to an in-memory image and returns it.

    """
    def __init__(self, cortijo):
        self.G = nx.DiGraph()  # initialize a directed graph
        super().__init__()
        self.cortijo = cortijo  # the cortijo object to represent in the graph

    def draw_graph(self, full_path, save=0, include=[]):
        # This function will add all the attributes from the "include" list to the label of each node.
        def get_node_label(node):
            label = [node.name]
            for attribute in include:
                if hasattr(node, attribute):
                    attr_value = getattr(node, attribute)
                    label.append(f"{attribute}: {attr_value}")
            return '\n'.join(label)

        self.G.add_node(self.cortijo.name)  # add cortijo as a node to the graph

        # loop over all types of children in the cortijo
        for child_type, children in self.cortijo._children.items():
            child_type_node = f"{child_type}\n-{self.cortijo.name}"  # create a label for the child type
            self.G.add_node(child_type_node)  # add the child type as a node
            self.G.add_edge(self.cortijo.name, child_type_node)  # draw an edge from cortijo to the child type

            # loop over all children of a particular type
            for child in children:
                self.G.add_node(child.name)  # add the child as a node
                self.G.add_edge(child_type_node, child.name)  # draw an edge from the child type to the child

                # loop over all types of subchildren in the child
                for subchild_type, subchildren in child._children.items():
                    subchild_type_node = f"{subchild_type}\n- {child.name}"  # create a label for the subchild type
                    self.G.add_node(subchild_type_node)  # add the subchild type as a node
                    self.G.add_edge(child.name, subchild_type_node)  # draw an edge from child to the subchild type

                    # loop over all subchildren of a particular type
                    for subchild in subchildren:
                        self.G.add_node(subchild.name)  # add the subchild as a node
                        self.G.add_edge(subchild_type_node,
                                        subchild.name)  # draw an edge from the subchild type to the subchild

        # Convert to a pygraphviz graph
        A = to_agraph(self.G)
        A.node_attr['shape'] = 'rectangle'  # set the shape of all nodes to rectangle

        # Use the 'dot' layout engine to draw a top-down graph
        A.layout('dot')

        if save == 1:
            # save the graph to a PNG file
            graph_path = os.path.join(full_path, 'graph.png')
            A.draw(graph_path)
            return Image.open(graph_path)
        else:
            # Render the graph to an in-memory byte buffer
            output_buffer = io.BytesIO()
            A.draw(output_buffer, format='png')

            # Create a PIL.Image object from the data
            image_data = output_buffer.getvalue()
            image = Image.open(io.BytesIO(image_data))
            return image  # return the image

