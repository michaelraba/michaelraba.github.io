import xml.etree.ElementTree as ET


def list_svg_layers(svg_path):
    tree = ET.parse(svg_path)
    root = tree.getroot()

    def recurse_layers(element, path="root", depth=0):
        for child in element:
            if child.tag.endswith("g"):
                layer_id = child.attrib.get("id", "(no id)")
                new_path = f"{path}/{layer_id}"
                print("  " * depth + f"→ {layer_id}")
                recurse_layers(child, new_path, depth + 1)

    recurse_layers(root)


list_svg_layers("./svg.svg")
