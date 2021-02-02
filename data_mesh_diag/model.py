from dataclasses import dataclass, field
from dataclasses_jsonschema import JsonSchemaMixin
from typing import List
import yaml

try:
    from yaml import CSafeLoader as YamlLoader
except ImportError:
    from yaml import SafeLoader as YamlLoader


@dataclass
class DataPort(JsonSchemaMixin):
    name: str


@dataclass
class DataProduct(JsonSchemaMixin):
    name: str
    input_ports: List[DataPort] = field(default_factory=lambda: [])
    output_ports: List[DataPort] = field(default_factory=lambda: [])


@dataclass
class DataDomain(JsonSchemaMixin):
    name: str
    data_products: List[DataProduct]


@dataclass
class DataMesh(JsonSchemaMixin):
    domains: List[DataDomain]


def get_data_mesh_from_file(filename: str) -> DataMesh:
    with open(filename, "rb") as handle:
        yaml_mesh_dict = yaml.load(handle.read().decode("utf-8"), Loader=YamlLoader)
        return DataMesh.from_dict(yaml_mesh_dict)