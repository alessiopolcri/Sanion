import xml.etree.ElementTree as ET

def load_strings(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    strings = {}
    for string in root.findall('string'):
        name = string.get('name')
        value = string.text
        strings[name] = value
    return strings

STRINGS = load_strings('data/xml/strings.xml')