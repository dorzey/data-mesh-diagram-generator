from graphviz import Digraph
from .model import DataPort, DataProduct, DataDomain, DataMesh


def add_domain(g, domain: DataDomain):
    with g.subgraph(name=f"cluster_{domain.name}") as h:
        h.attr(label=domain.name)
        for data_product in domain.data_products:
            add_data_product(h, data_product)


def add_data_product(h, data_product: DataProduct):
    h.node(data_product.name, shape="hexagon")
    for idp in data_product.input_ports:
        add_input_port(h, data_product, idp)
    for odp in data_product.output_ports:
        add_output_port(h, data_product, odp)


def add_output_port(h, data_product: DataProduct, odp: DataPort):
    h.node(odp.name, shape="doublecircle")
    h.edge(data_product.name, odp.name)


def add_input_port(h, data_product: DataProduct, idp: DataPort):
    h.node(idp.name, shape="doublecircle")
    h.edge(idp.name, data_product.name)


def generate_diagram(data_mesh: DataMesh, output_filename="data_mesh") -> str:
    g = Digraph("G", format="png")

    for domain in data_mesh.domains:
        add_domain(g, domain)

    g.render(filename=output_filename, format="png", cleanup=True)
    return output_filename + ".png"