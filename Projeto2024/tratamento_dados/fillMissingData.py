import json


data = json.loads(open('datasets/final_countries2.json', encoding='UTF-8').read())



# capital 
data["Palestine"]["capital"] = "Jerusalem"


# espetativa de vida 
data["Andorra"]["espetativa de vida"] = 83.5
data["Monaco"]["espetativa de vida"] = 89.5
data["HolySee"]["espetativa de vida"] = 84.16
data["Tuvalu"]["espetativa de vida"] = 67.7


# exportacoes  e importacoes - baseado em - https://oec.world/
data["IvoryCoast"]["exportacoes"] = 17500
data["IvoryCoast"]["importacoes"] = 18300
data["HolySee"]["exportacoes"] = 0
data["HolySee"]["importacoes"] = 0
data["Liechtenstein"]["exportacoes"] = 0
data["Liechtenstein"]["importacoes"] = 0
data["Monaco"]["exportacoes"] = 0
data["Monaco"]["importacoes"] = 0
data["Nauru"]["exportacoes"] = 198
data["Nauru"]["importacoes"] = 74.8
data["SanMarino"]["exportacoes"] = 204
data["SanMarino"]["importacoes"] = 437


# gdp 
data["HolySee"]["gdp"] = 0  # não divulgado

# hemisferio 
data["SãoToméandPríncipe"]["hemisferio"] = "Norte"

# lado em que conduz      
data["Georgia"]["lado em que conduz"] = "right"
data["HolySee"]["lado em que conduz"] = "right"
data["Ireland"]["lado em que conduz"] = "left"
data["Micronesia"]["lado em que conduz"] = "right"
data["Palestine"]["lado em que conduz"] = "right"
data["Vanuatu"]["lado em que conduz"] = "right"


# literacia 
data["Cyprus"]["literacia"] = 99.1
data["HolySee"]["literacia"] = 100
data["DemocraticRepublicoftheCongo"]["literacia"] = 77
data["Montenegro"]["literacia"] = 98.7
data["Palestine"]["literacia"] = 96.3
data["SouthSudan"]["literacia"] = 34.5
data["EastTimor"]["literacia"] = 68.1

############################################################################################################
#VERIFICAR ESTA PARTE
############################################################################################################
# MIGRACAO LIQUIDA
data["DemocraticRepublicoftheCongo"]["migracao liquida"] = -0.20
data["HolySee"]["migracao liquida"] = 0.0
data["Montenegro"]["migracao liquida"] = 0.1
data["Palestine"]["migracao liquida"] = -1.2
data["SouthSudan"]["migracao liquida"] = -4.3

# MOEDA
data["Netherlands"]["moeda"] = "Euro"
data["Palestine"]["moeda"] = "Israeli new shekel, Jordanian dinar"

# MORTALIDADE INFANTIL
data["HolySee"]["mortalidade infantil"] = 0

# TAXA DE MORTALIDADE
data["Andorra"]["taxa de mortalidade"] = 6.9
data["DemocraticRepublicoftheCongo"]["taxa de mortalidade"] = 14.3
data["HolySee"]["taxa de mortalidade"] = 10.4
data["Liechtenstein"]["taxa de mortalidade"] = 7.3
data["Monaco"]["taxa de mortalidade"] = 10.2
data["Montenegro"]["taxa de mortalidade"] = 9.6
data["Nauru"]["taxa de mortalidade"] = 7.5
data["Palestine"]["taxa de mortalidade"] = 3.9
data["SanMarino"]["taxa de mortalidade"] = 8.7
data["SouthSudan"]["taxa de mortalidade"] = 14.9
data["Tuvalu"]["taxa de mortalidade"] = 9.0

# TAXA DE NATALIDADE
data["HolySee"]["taxa de natalidade"] = 0
data["Nauru"]["taxa de natalidade"] = 24.9
data["Palestine"]["taxa de natalidade"] = 30.3

# TELEFONES POR 1000
data["HolySee"]["telefones por 1000"] = 0

# COSTA
data["Benin"]["costa"] = 121
data["CentralAfricanRepublic"]["costa"] = 0
data["DemocraticRepublicoftheCongo"]["costa"] = 37
data["HolySee"]["costa"] = 0
data["Montenegro"]["costa"] = 293.5
data["Palestine"]["costa"] = 40
data["SouthSudan"]["costa"] = 0

# RACIO SEXOS
data["IvoryCoast"]["racio sexos"] = 98.2

# TAXA DESEMPREGO
data["Andorra"]["taxa desemprego"] = 3.7
data["AntiguaandBarbuda"]["taxa desemprego"] = 11.0
data["IvoryCoast"]["taxa desemprego"] = 2.9
data["Dominica"]["taxa desemprego"] = 23.0
data["Grenada"]["taxa desemprego"] = 15.0
data["HolySee"]["taxa desemprego"] = 0
data["Kiribati"]["taxa desemprego"] = 30.6
data["Micronesia"]["taxa desemprego"] = 16.2
data["Monaco"]["taxa desemprego"] = 2.0
data["Palau"]["taxa desemprego"] = 1.7
data["SaintKittsandNevis"]["taxa desemprego"] = 4.5
data["SouthSudan"]["taxa desemprego"] = 12.0
data["Tuvalu"]["taxa desemprego"] = 6.0

# TAXA FERTILIDADE
data["IvoryCoast"]["taxa fertilidade"] = 4.7
data["Dominica"]["taxa fertilidade"] = 2.1
data["HolySee"]["taxa fertilidade"] = 0
data["Monaco"]["taxa fertilidade"] = 1.5
data["SaintKittsandNevis"]["taxa fertilidade"] = 2.2
data["SanMarino"]["taxa fertilidade"] = 1.4

# EMISSOES CO2
data["AntiguaandBarbuda"]["emissoes co2"] = 2.0
data["IvoryCoast"]["emissoes co2"] = 0.4
data["HolySee"]["emissoes co2"] = 0
data["Monaco"]["emissoes co2"] = 4.2
data["Palau"]["emissoes co2"] = 15.8
data["SanMarino"]["emissoes co2"] = 1.8
data["Tuvalu"]["emissoes co2"] = 0.1



f = open("datasets/countriesInfo.json","w", encoding='UTF-8')
json.dump(data,f,indent=4)
