import xml.etree.ElementTree as ET

def extract_country_names(svg_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()
    
    # Namespace for SVG files
    namespace = {'svg': 'http://www.w3.org/2000/svg'}
    
    # Extract all paths and their classNames
    country_names = set()
    for path in root.findall('.//svg:path', namespace):
        class_name = path.get('className')
        if class_name:
            country_names.add(class_name)
    
    return country_names

# Path to your SVG file
svg_file = 'map.svg'

# Extract and print country names
country_names = extract_country_names(svg_file)
for country in sorted(country_names):
    print(country)

