import sys

from .graph import generate_diagram
from .model import get_data_mesh_from_file


def main():
    yaml_file = sys.argv[1]
    print(f"Generating diagram from {yaml_file}...")
    data_mesh = get_data_mesh_from_file(yaml_file)
    output_filename = generate_diagram(data_mesh)
    print(f"Diagram written to {output_filename}")


if __name__ == "__main__":
    main()
