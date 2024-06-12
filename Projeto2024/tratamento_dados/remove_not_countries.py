import json

# Function to remove specified countries from the JSON data
def remove_countries_from_json(json_data, countries_to_remove):
    new_json_data = {}
    for country in countries_to_remove:
        del json_data[country]
    for country in json_data:
        new_json_data[country.replace(" ","")] = json_data[country]
    return new_json_data

# List of countries to be removed
countries_to_remove = ["American Samoa", "Anguilla", "Aruba", "Bermuda", "Bonaire",
                       "British Virgin Islands", "CaymanIslands", "ChannelIslands",
                       "Cook Islands", "Falkland Islands", "FaroeIslands", "FrenchGuiana",
                       "FrenchPolynesia","GazaStrip", "Gibraltar", "Greenland", "Guadeloupe",
                       "Guam", "Guernsey", "Hong Kong", "Isle of Man", "Jersey", "Macau", "Macao",
                       "Martinique", "Mayotte", "Montserrat", "NetherlandsAntilles", "NewCaledonia",
                       "Niue", "N.MarianaIslands","NorthernMarianaIslands", "PuertoRico", "Reunion",
                       "SaintHelena", "SaintPierreandMiquelon", "Sint Maarten", "StPierre&Miquelon",
                       "Taiwan", "Tokelau", "Turks&CaicosIs", "TurksandCaicosIslands",
                       "VirginIslands","Wallis and Futuna", "WestBank", "WesternSahara",
                       "S\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd"]

# Load the JSON data from the file
with open('datasets/countries.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)

# Remove the specified countries
updated_data = remove_countries_from_json(data, countries_to_remove)

# Save the updated JSON data back to the file
with open('datasets/final_countries.json', 'w', encoding='UTF-8') as file:
    json.dump(updated_data, file, indent=4)

print(updated_data.keys())
print("Countries removed successfully.")
