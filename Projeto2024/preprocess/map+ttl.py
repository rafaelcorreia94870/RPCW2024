import json

# List of country names from the first list
countries1 = [
    "Afghanistan", "Albania", "Algeria", "American Samoa", "Angola", "Anguilla", "Antigua and Barbuda",
    "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
    "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia",
    "Bosnia and Herzegovina", "Botswana", "Brazil", "British Virgin Islands", "Brunei Darussalam",
    "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Canary Islands (Spain)",
    "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Colombia",
    "Comoros", "Costa Rica", "Croatia", "Cuba", "Curaçao", "Cyprus", "Czech Republic", "Côte d'Ivoire",
    "Dem. Rep. Korea", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica",
    "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
    "Ethiopia", "Faeroe Islands", "Falkland Islands", "Federated States of Micronesia", "Fiji", "Finland",
    "France", "French Guiana", "French Polynesia", "Gabon", "Georgia", "Germany", "Ghana", "Greece",
    "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
    "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kosovo", "Kuwait", "Kyrgyzstan",
    "Lao PDR", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Lithuania", "Luxembourg",
    "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
    "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Moldova", "Mongolia", "Montenegro",
    "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
    "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Northern Mariana Islands", "Norway",
    "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar", "Republic of Congo", "Republic of Korea",
    "Reunion", "Romania", "Russian Federation", "Rwanda", "Saba (Netherlands)", "Saint Kitts and Nevis",
    "Saint Lucia", "Saint Vincent and the Grenadines", "Saint-Barthélemy", "Saint-Martin", "Samoa",
    "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Sint Maarten", "Slovakia",
    "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka",
    "St. Eustatius (Netherlands)", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria",
    "São Tomé and Principe", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "The Gambia", "Timor-Leste",
    "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands",
    "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States",
    "United States Virgin Islands", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam",
    "Western Sahara", "Yemen", "Zambia", "Zimbabwe"
]

# List of country names from the second list
countries2 = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua & Barbuda", "Antigua and Barbuda",
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahamas, The", "Bahrain",
    "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bolivia (Plurinational State of)",
    "Bosnia & Herzegovina", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Brunei Darussalam",
    "Bulgaria", "Burkina Faso", "Burma", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Cape Verde",
    "Central African Rep.", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo",
    "Congo, Dem. Rep.", "Congo, Repub. of the", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus",
    "Czech Republic", "Czechia", "Democratic People's Republic of Korea", "Democratic Republic of the Congo", "Denmark",
    "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
    "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Federated States of Micronesia", "Fiji", "Finland", "France", "Gabon",
    "Gambia", "Gambia, The", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
    "Guyana", "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iran (Islamic Republic of)",
    "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati",
    "Korea, North", "Korea, South", "Kuwait", "Kyrgyzstan", "Lao People's Democratic Republic", "Laos", "Latvia", "Lebanon",
    "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malawi", "Malaysia",
    "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia (Federated States of)",
    "Micronesia, Fed. St.", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia",
    "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway",
    "Oman", "Pakistan", "Palau", "Palestinian National Authority", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines",
    "Poland", "Portugal", "Qatar", "Republic of Ireland", "Republic of Korea", "Republic of Moldova", "Republic of the Congo",
    "Romania", "Russia", "Russian Federation", "Rwanda", "Saint Kitts & Nevis", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome & Principe", "Sao Tome and Principe", "Saudi Arabia",
    "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
    "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "State of Palestine", "Sudan", "Suriname", "Swaziland",
    "Sweden", "Switzerland", "Syria", "Syrian Arab Republic", "Tajikistan", "Tanzania", "Thailand", "The Bahamas", "The Gambia",
    "The former Yugoslav Republic of Macedonia", "Timor-Leste", "Togo", "Tonga", "Trinidad & Tobago", "Trinidad and Tobago",
    "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United Republic of Tanzania",
    "United States", "United States Virgin Islands", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City",
    "Venezuela", "Venezuela (Bolivarian Republic of)", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

# Create a mapping dictionary
mapping = {}

for country1 in countries1:
    # Find the best match in countries2
    best_match = None
    for country2 in countries2:
        if country1.lower().strip() == country2.lower().strip():
            best_match = country2
            break
    mapping[country1] = best_match

# Write the mapping to a JSON file
with open('country_mapping.json', 'w') as f:
    json.dump(mapping, f, indent=4)

print("Country mapping written to country_mapping.json")
