#!/usr/bin/env python3


import xml.etree.ElementTree as ET

# Load SVG
tree = ET.parse('./svg.svg')
root = tree.getroot()

# SVGs usually use this namespace
SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace('', SVG_NS)

# Print all elements with an id
for elem in root.iter():
    id_val = elem.attrib.get('id')
    if id_val:
        print(f"Found element with id: {id_val}")
