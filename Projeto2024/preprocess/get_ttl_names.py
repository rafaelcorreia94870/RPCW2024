import json

def extract_country_names(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Extract country names from the JSON data
    country_names = {binding['country_name']['value'] for binding in data['results']['bindings']}
    
    return country_names

# Path to your JSON file
json_file = 'query-result.srj'

# Extract and print country names
country_names = extract_country_names(json_file)
for country in sorted(country_names):
    print(country)
