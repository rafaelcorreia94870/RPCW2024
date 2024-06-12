import re
import csv
import json

# open not_country.csv file and create a list of countries
with open('../preprocess/not_country.csv', 'r') as f:
    reader = csv.reader(f)
    not_country = reader.__next__()
    # print(not_country)


def replace_spaces_with_underscore(svg_content):
    # Regular expression pattern to match class attribute values
    pattern = r'className="([^"]*)"'

    # Function to replace spaces with underscores in class attribute values
    def replace_spaces(match):
        country_name = match.group(1)
        if country_name in not_country:
            return f'className= "not-country {country_name}"'
        else:
            country_name = country_name.replace(' ', '_')
            return f'className={{getCountryClassName("{country_name}")}}\nonMouseOver={{handleMouseOver}}\nonMouseLeave={{handleMouseLeave}}'

    # Perform the replacement using regular expressions
    modified_svg_content = re.sub(pattern, replace_spaces, svg_content)

    return modified_svg_content


def get_name_list():
    name_list = []
    with open('datasets/countriesInfo.json', 'r', encoding='utf-8') as f:
        content = json.load(f)
        for country in content:
            names = content[country]["nome"]
            for name in names:
                name_list.append(name)
    return name_list

def check_names(svg, namelist):
    names_not_in_list = set()
    svg_names = re.findall(r'className="([^"]*)"', svg)
    for name in svg_names:
        if name not in namelist and name not in not_country:
            names_not_in_list.add(name)
    return names_not_in_list
    
def name_treatment(names_not_in_list):
    #Republic of Congo -> Congo
    #Dem. Rep. Korea -> North Korea
    #Palestine -> Palestine
    #Côte d'Ivoire -> IvoryCoast
    #São Tomé and Principe -> S\u00e3oTom\u00e9andPr\u00edncipe
    #Lao PDR -> Laos
    #for each of these comments, add the name to the countriesInfo.json file, knowing that the comments here are formatted as name_to_add -> name_in_json_file

    with open('datasets/countriesInfo.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Modify the JSON data based on the provided names
    for name in names_not_in_list:
        if name == "Republic of Congo":
            data["RepublicoftheCongo"]["nome"].append("Republic of Congo")
        elif name == "Dem. Rep. Korea":
            data["NorthKorea"]["nome"].append("Dem. Rep. Korea")
        elif name == "Palestine":
            data["Palestine"]["nome"].append("Palestine")
        elif name == "Côte d'Ivoire":
            data["IvoryCoast"]["nome"].append("Côte d'Ivoire")
        elif name == "São Tomé and Principe":
            data["SãoToméandPríncipe"]["nome"].append("São Tomé and Principe")
        elif name == "Lao PDR":
            data["Laos"]["nome"].append("Lao PDR")
        else:
            print("Name not treated:", name)
    
    # Save the changes back to the JSON file
    with open('datasets/countriesInfo.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    
def main():
    # Input SVG file name
    input_svg_file = '../preprocess/map.svg'
    # Output SVG file name
    output_svg_file = '../preprocess/output.svg'

    # Read the content of the input SVG file
    with open(input_svg_file, 'r', encoding='utf-8') as f:
        svg_content = f.read()

    # Modify the SVG content
    modified_svg_content = replace_spaces_with_underscore(svg_content)

    namelist = get_name_list()
    
    names_not_in_list = check_names(svg_content, namelist)
    print(names_not_in_list)

    name_treatment(names_not_in_list)


    # Write the modified SVG content to the output file
    with open(output_svg_file, 'w') as f:
        f.write(modified_svg_content)

    print("SVG classes with spaces replaced by underscores. Output saved to", output_svg_file)


if __name__ == "__main__":
    main()
