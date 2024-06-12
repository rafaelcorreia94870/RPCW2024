#Make me code to open datasets/world-data-2023.csv and return the data as dictionaries with country and all the info of it.

import csv
import re
import json

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def treatCountryName(name):
    #if name contains Bosnia return Bosnia and Herzegovina
    name = name.replace(' ', '')
    name = name.replace(' and ', '&')
    if 'Bahama' in name:
        return 'The Bahamas'
    if 'Bolivia' in name:
        return 'Bolivia'
    if 'Bonaire' in name:
        return 'Bonaire'
    
    if 'Bosnia' in name:
        return 'Bosnia and Herzegovina'
    #if name contains Herzegovina return Bosnia and Herzegovina
    if 'Herzegovina' in name:
        return 'Bosnia and Herzegovina'
    if 'Wallis' in name:
        return 'Wallis and Futuna'
    if 'Futuna' in name:
        return 'Wallis and Futuna'
    if 'Congo' in name and not 'Dem' in name:
        return 'Republic of the Congo'
    if 'Sao' in name and 'Tome' in name:
        return 'São Tomé and Príncipe'
    if 'SanMarino' in name:
        return 'San Marino'
    if 'Saint' in name and 'Kitts' in name:
        return 'Saint Kitts and Nevis'
    if 'Papua' in name:
        return 'Papua New Guinea'
    if 'Marshall' in name:
        return 'Marshall Islands'
    if 'IsleofMan' in name:
        return 'Isle of Man'
    if 'Hong' in name and 'Kong' in name:
        return 'Hong Kong'
    if 'Guinea' in name and not 'Equatorial' in name and 'Bissau' in name:
        return 'Guinea-Bissau'
    if 'Guinea' in name and not 'Equatorial' in name and not 'Bissau' in name:
        return 'Guinea'
    if 'equatorial' in name:
        return 'Equatorial Guinea'
    if 'Salvador' in name:
        return 'El Salvador'
    if 'DominicanRepublic' in name:
        return 'Dominican Republic'
    if 'Dem' in name and 'Congo' in name:
        return 'Democratic Republic of the Congo'
    if 'Czech' in name:
        return 'Czech Republic'
    if 'Costa' in name and 'Rica' in name:
        return 'Costa Rica'
    if 'Cook' in name and 'Islands':
        return 'Cook Islands'
    if 'Central' in name and 'African' in name:
        return 'Central African Republic'
    if ('Cape' in name or 'Cabo' in name) and 'Verde' in name:
        return 'Cape Verde'
    if 'British' in name and 'Virgin' in name:
        return 'British Virgin Islands'
    if 'Antigua' in name:
        return 'Antigua and Barbuda'
    if 'Samoa' in name and 'American' in name:
        return 'American Samoa'
    if 'Venezuela' in name:
        return 'Venezuela'
    if 'Sint' in name and 'Maarten' in name:
        return 'Sint Maarten'
    if 'Micronesia' in name:
        return 'Micronesia'
    if ('Korea' in name and 'North' in name ) or ('Korea' in name and 'Democratic' in name):
        return 'North Korea'
    if 'Korea' in name and 'South' in name or ('Korea' in name and 'Republic' in name):
        return 'South Korea'
    if 'Iran' in name:
        return 'Iran'
    if 'Gambia' in name:
        return 'TheGambia'
    if 'United' in name and 'States' in name:
        return 'United States'
    if 'Malvinas' in name or 'Falkland' in name:
        return 'Falkland Islands'
    if 'Macao' in name:
        return 'Macao'
    if 'Brunei' in name:
        return 'Brunei'
    if name == "Laos" or ('Lao' in name and 'People' in name and 'Democratic' in name and 'Republic' in name):
        return 'Laos'
    if name == "Burma":
        return 'Myanmar'
    if "Ivory" in name and "Coast" in name or ("Coted" in name and "Ivoire" in name):
        return "Ivory Coast"
    if "Timor" in name :
        return "East Timor"
    if "Swaziland" in name:
        return "Eswatini"
    if "Holy" in name and "See" in name or ("Vatican" in name and "City" in name):
        return "Holy See"
    if "Macedonia" in name:
        return "North Macedonia"
    if "Moldova" in name:
        return "Moldova"
    if "Ireland" in name:
        return "Ireland"
    if "Russia" in name:
        return "Russia"
    if "Palestine" in name or "Palestinian" in name:
        return "Palestine"
    if "Syria" in name:
        return "Syria"
    if "Trinidad" in name:
        return "Trinidad and Tobago"
    if "Tanzania" in name:
        return "Tanzania"
    
        

    return name
def open_csv_world_data_2023(data):
    file = 'datasets/world-data-2023.csv'
    #Country -> nome
    #Density -> densidade_populacional
    #Abreviation -> NOT USED (abreviacao)
    #Agricultural Land( %) -> NOT USED (terra_agricola)
    #Land Area(Km2) -> area
    #Birth Rate -> taxa de natalidade
    #Calling Code -> NOT USED (codigo_telefonico)
    #Capital/Major City -> capital
    #Co2-Emissions -> NOT USED (emissoes_co2)
    #CPI -> NOT USED (indice_percepcao_corrupcao)
    #CPI Change (%) -> NOT USED (mudanca_indice_percepcao_corrupcao)
    #Currency-Code -> NOT USED (codigo_moeda)
    #Fertility Rate -> NOT USED (taxa_fertilidade)
    #Forested Area (%) -> NOT USED (area_florestada)
    #Gasoline Price -> NOT USED (preco_gasolina)
    #GDP -> gdp
    #Gross primary education enrollment (%) -> NOT USED (matriculas_ensino_primario)
    #Gross tertiary education enrollment (%) -> NOT USED (matriculas_ensino_terciario)
    #Infant mortality -> mortalidade_infantil
    #Largest city -> NOT USED (maior_cidade)
    #Life expectancy -> espetativa_de_vida
    #Maternal mortality ratio -> NOT USED (taxa_mortalidade_materna)
    #Minimum wage -> NOT USED (salario_minimo)
    #Official language -> NOT USED (lingua_oficial)
    #Out of pocket health expenditure -> NOT USED (despesas_saude_bolso)
    #Physicians per thousand -> NOT USED (medicos_por_mil)
    #Population -> populacao
    #Population: Labor force participation (%) -> NOT USED (participacao_forca_trabalho)
    #Tax revenue (%) -> NOT USED (receita_imposto)
    #Total tax rate -> NOT USED (taxa_imposto)
    #Unemployment rate -> NOT USED (taxa_desemprego)
    #Urban_population -> NOT USED (populacao_urbana)
    #Latitude -> latitude
    #Longitude -> longitude
    with open(file, 'r', encoding='UTF-8') as f:
        # return the data as one dictionary with the country as key and all the info as values
        reader = csv.DictReader(f)
        for row in reader:
            original_name = row['Country'].strip()
            row['Country']= treatCountryName(row['Country'])
            if row['Country'] not in data:
                data[row['Country']] = {}
            old_data = data[row['Country']]
            if old_data == {}:
                data[row['Country']]['nome'] = []
                old_data = { 
                    'area': '', 
                    'capital': '', 
                    'densidade populacional': '', 
                    'espetativa de vida' : '', 
                    'exportacoes': '', 
                    'gdp': '', 
                    'hemisferio': '', 
                    'importacoes': '', 
                    'lado em que conduz': '', 
                    'latitude': '', 
                    'literacia': '', 
                    'longitude': '', 
                    'migracao liquida': '', 
                    'moeda': '', 
                    'mortalidade infantil': '', 
                    'populacao': '', 
                    'taxa de mortalidade': '', 
                    'taxa de natalidade': '', 
                    'telefones por 1000': '', 
                    'costa' : '', 
                    'temperatura media': '', 
                    'racio sexos': '', 
                    'taxa desemprego': '', 
                    'taxa fertilidade': '', 
                    'medicos por mil': '', 
                    'receita imposto': '', 
                    'emissoes co2' : '', 
                    }
                
            
            if original_name not in data[row['Country']]['nome']:
                data[row['Country']]['nome'].append(original_name)
            if old_data['area'] == '':
                data[row['Country']]['area'] = row['Land Area(Km2)']

            if old_data['capital'] == '':
                data[row['Country']]['capital'] = row['Capital/Major City']

            if old_data['densidade populacional'] == '':
                data[row['Country']]['densidade populacional'] = row['Density\n(P/Km2)']

            if old_data['espetativa de vida'] == '':
                data[row['Country']]['espetativa de vida'] = row['Life expectancy']

            if old_data['exportacoes'] == '':
                data[row['Country']]['exportacoes'] = ''

            if old_data['gdp'] == '':
                data[row['Country']]['gdp'] = row['GDP']

            if old_data['hemisferio'] == '':
                row_info = row['Latitude']
                if is_float(row_info):
                    if float(row['Latitude']) > 0:
                        data[row['Country']]['hemisferio'] = 'Norte'
                    else:
                        data[row['Country']]['hemisferio'] = 'Sul'
                else:
                    data[row['Country']]['hemisferio'] = ''

            if old_data['importacoes'] == '':
                data[row['Country']]['importacoes'] = ''

            if old_data['lado em que conduz'] == '':
                data[row['Country']]['lado em que conduz'] = ''

            if old_data['latitude'] == '':
                data[row['Country']]['latitude'] = row['Latitude']

            if old_data['literacia'] == '':
                data[row['Country']]['literacia'] = ''

            if old_data['longitude'] == '':
                data[row['Country']]['longitude'] = row['Longitude']

            if old_data['migracao liquida'] == '':
                data[row['Country']]['migracao liquida'] = ''

            if old_data['moeda'] == '':
                data[row['Country']]['moeda'] = row['Currency-Code']

            if old_data['mortalidade infantil'] == '':
                data[row['Country']]['mortalidade infantil'] = row['Infant mortality']

            if old_data['populacao'] == '':
                data[row['Country']]['populacao'] = row['Population']

            if old_data['taxa de mortalidade'] == '':
                data[row['Country']]['taxa de mortalidade'] = ''

            if old_data['taxa de natalidade'] == '':
                data[row['Country']]['taxa de natalidade'] = row['Birth Rate']

            if old_data['telefones por 1000'] == '':
                data[row['Country']]['telefones por 1000'] = ''

            if old_data['costa'] == '':
                data[row['Country']]['costa'] = ''

            if old_data['temperatura media'] == '':
                data[row['Country']]['temperatura media'] = ''

            if old_data['racio sexos'] == '':
                data[row['Country']]['racio sexos'] = ''

            if old_data['taxa desemprego'] == '':
                data[row['Country']]['taxa desemprego'] = ''

            if old_data['taxa fertilidade'] == '':
                data[row['Country']]['taxa fertilidade'] = ''

            if old_data['medicos por mil'] == '':
                data[row['Country']]['medicos por mil'] = ''

            if old_data['receita imposto'] == '':
                data[row['Country']]['receita imposto'] = row['Tax revenue (%)']

            if old_data['emissoes co2'] == '':
                data[row['Country']]['emissoes co2'] = ''      
                      
    return data

def open_csv_contry_profile_variables(data):
    file = 'datasets/country_profile_variables.csv'
    #country -> nome
    #Region -> NOT USED (regiao)
    #Surface area (km2) -> area
    #Population in thousands (2017) -> populacao
    #Population density (per km2, 2017) -> densidade_populacional
    #Sex ratio (m per 100 f, 2017) -> NOT USED (racio sexos), a usar agr
    #GDP: Gross domestic product (million current US$) -> gdp
    #GDP growth rate (annual %, const. 2005 prices) -> NOT USED (crescimento_gdp)
    #GDP per capita (current US$) -> NOT USED (gdp_per_capita)
    #Economy: Agriculture (% of GVA) -> NOT USED (agricultura)
    #Economy: Industry (% of GVA) -> NOT USED (industria)
    #Economy: Services and other activity (% of GVA) -> NOT USED (servicos)
    #Employment: Agriculture (% of employed) -> NOT USED (emprego_agricultura)
    #Employment: Industry (% of employed) -> NOT USED (emprego_industria)
    #Employment: Services (% of employed) -> NOT USED (emprego_servicos)
    #Unemployment (% of labour force) -> NOT USED (taxa_desemprego)
    #Labour force participation (female/male pop. %) -> NOT USED (participacao_forca_trabalho)
    #Agricultural production index (2004-2006=100) -> NOT USED (indice_producao_agricola)
    #Food production index (2004-2006=100) -> NOT USED (indice_producao_alimentar)
    #International trade: Exports (million US$) -> exportacoes
    #International trade: Imports (million US$) -> importacoes
    #International trade: Balance (million US$) -> NOT USED (balanco_comercial)
    #Balance of payments, current account (million US$) -> NOT USED (balanco_pagamentos)
    #Population growth rate (average annual %) -> NOT USED (crescimento_populacional)
    #Urban population (% of total population) -> NOT USED (populacao_urbana)
    #Urban population growth rate (average annual %) -> NOT USED (crescimento_populacao_urbana)
    #Fertility rate, total (live births per woman) -> NOT USED (taxa_fertilidade)
    #Life expectancy at birth (females/males, years) -> espetativa_de_vida (necessita tratar)
    #Population age distribution (0-14 / 60+ years, %) -> NOT USED (distribuicao_etaria)
    #International migrant stock (000/% of total pop.) -> NOT USED (migracao_internacional)
    #Refugees and others of concern to UNHCR (in thousands) -> NOT USED (refugiados)
    #Infant mortality rate (per 1000 live births -> mortalidade_infantil
    #Health: Total expenditure (% of GDP) -> NOT USED (despesas_saude)
    #Health: Physicians (per 1000 pop.) -> NOT USED (medicos_por_mil)
    #Education: Government expenditure (% of GDP) -> NOT USED (despesas_educacao)
    #Education: Primary gross enrol. ratio (f/m per 100 pop.) -> NOT USED (matriculas_ensino_primario)
    #Education: Secondary gross enrol. ratio (f/m per 100 pop.) -> NOT USED (matriculas_ensino_secundario)
    #Education: Tertiary gross enrol. ratio (f/m per 100 pop.) -> NOT USED (matriculas_ensino_terciario)
    #Seats held by women in national parliaments % -> NOT USED (mulheres_parlamento)
    #Mobile-cellular subscriptions (per 100 inhabitants) -> NOT USED (telemovel_por_100)
    #Mobile-cellular subscriptions (per 100 inhabitants) -> NOT USED (telemovel_por_100)
    #Individuals using the Internet (per 100 inhabitants) -> NOT USED (internet_por_100)
    #Threatened species (number) -> NOT USED (especies_ameacadas)
    #Forested area (% of land area) -> NOT USED (area_florestada)
    #CO2 emission estimates (million tons/tons per capita) -> NOT USED (emissoes_co2)
    #Energy production, primary (Petajoules) -> NOT USED (producao_energia)
    #Energy supply per capita (Gigajoules) -> NOT USED (energia_por_capita)
    #Pop. using improved drinking water (urban/rural, %) -> NOT USED (agua_potavel)
    #Pop. using improved sanitation facilities (urban/rural, %) -> NOT USED (saneamento)
    #Net Official Development Assist. received (% of GNI) -> NOT USED (ajuda_desenvolvimento)
    with open(file, 'r', encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            original_name = row['country'].strip()
            row['country'] = treatCountryName(row['country'])
            if row['country'] not in data:
                data[row['country']] = {}
            old_data = data[row['country']]
            if old_data == {}:
                data[row['country']]['nome'] = []
                old_data = {
                    'area': '', 
                    'capital': '', 
                    'densidade populacional': '', 
                    'espetativa de vida' : '', 
                    'exportacoes': '', 
                    'gdp': '', 
                    'hemisferio': '', 
                    'importacoes': '', 
                    'lado em que conduz': '', 
                    'latitude': '', 
                    'literacia': '', 
                    'longitude': '', 
                    'migracao liquida': '', 
                    'moeda': '', 
                    'mortalidade infantil': '', 
                    'populacao': '', 
                    'taxa de mortalidade': '', 
                    'taxa de natalidade': '', 
                    'telefones por 1000': '', 
                    'costa' : '', 
                    'temperatura media': '', 
                    'racio sexos': '', 
                    'taxa desemprego': '', 
                    'taxa fertilidade': '', 
                    'medicos por mil': '', 
                    'receita imposto': '', 
                    'emissoes co2' : '', 
                }
        
            if original_name not in data[row['country']]['nome']:
                data[row['country']]['nome'].append(original_name)
            
            if old_data['area'] == '':
                data[row['country']]['area'] = row['Surface area (km2)']

            if old_data['capital'] == '':
                data[row['country']]['capital'] = ''
            
            if old_data['densidade populacional'] == '':
                data[row['country']]['densidade populacional'] = row['Population density (per km2, 2017)']

            if old_data['espetativa de vida'] == '':
                row_info = row['Life expectancy at birth (females/males, years)']
                row_info = row_info.split('/')
                if (len(row_info) == 2 and is_float(row_info[0]) and is_float(row_info[1])):
                    data_add = (float(row_info[0]) + float(row_info[1])) / 2
                    data[row['country']]['espetativa de vida'] = data_add

            if old_data['exportacoes'] == '':
                data[row['country']]['exportacoes'] = row['International trade: Exports (million US$)']
            
            if old_data['gdp'] == '':
                data[row['country']]['gdp'] = row['GDP: Gross domestic product (million current US$)']
            
            if old_data['hemisferio'] == '':
                data[row['country']]['hemisferio'] = ''
            
            if old_data['importacoes'] == '':
                data[row['country']]['importacoes'] = row['International trade: Imports (million US$)']

            if old_data['lado em que conduz'] == '':
                data[row['country']]['lado em que conduz'] = ''

            if old_data['latitude'] == '':
                data[row['country']]['latitude'] = ''

            if old_data['literacia'] == '':
                data[row['country']]['literacia'] = ''

            if old_data['longitude'] == '':
                data[row['country']]['longitude'] = ''

            if old_data['migracao liquida'] == '':
                data[row['country']]['migracao liquida'] = ''
            
            if old_data['moeda'] == '':
                data[row['country']]['moeda'] = ''

            if old_data['mortalidade infantil'] == '':
                data[row['country']]['mortalidade infantil'] = row['Infant mortality rate (per 1000 live births']

            if old_data['populacao'] == '':
                data[row['country']]['populacao'] = row['Population in thousands (2017)']
            
            if old_data['taxa de mortalidade'] == '':
                data[row['country']]['taxa de mortalidade'] = ''

            if old_data['taxa de natalidade'] == '':
                data[row['country']]['taxa de natalidade'] = ''

            if old_data['telefones por 1000'] == '':
                #check if this is possible float(row['Mobile-cellular subscriptions (per 100 inhabitants)'])
                if is_float(row['Mobile-cellular subscriptions (per 100 inhabitants)']):
                    data[row['country']]['telefones por 1000'] = float(row['Mobile-cellular subscriptions (per 100 inhabitants)'])*10.0
                else:
                    data[row['country']]['telefones por 1000'] = ''

            if old_data['costa'] == '':
                data[row['country']]['costa'] = ''

            if old_data['temperatura media'] == '':
                data[row['country']]['temperatura media'] = ''

            if old_data['racio sexos'] == '':
                data[row['country']]['racio sexos'] = row['Sex ratio (m per 100 f, 2017)']

            if old_data['taxa desemprego'] == '':
                if is_float(row['Unemployment (% of labour force)']):
                    data[row['country']]['taxa desemprego'] = row['Unemployment (% of labour force)']
                else:
                    data[row['country']]['taxa desemprego'] = ''

            if old_data['taxa fertilidade'] == '':
                if is_float(row['Fertility rate, total (live births per woman)']):
                    data[row['country']]['taxa fertilidade'] = row['Fertility rate, total (live births per woman)' ]
                else:
                    data[row['country']]['taxa fertilidade'] = ''

            if old_data['medicos por mil'] == '':
                if is_float(row['Health: Physicians (per 1000 pop.)']):
                    data[row['country']]['medicos por mil'] = row['Health: Physicians (per 1000 pop.)']
                else:
                    data[row['country']]['medicos por mil'] = ''

            if old_data['receita imposto'] == '':
                data[row['country']]['receita imposto'] = ''

            if old_data['emissoes co2'] == '':
                data[row['country']]['emissoes co2'] = row['CO2 emission estimates (million tons/tons per capita)']


    return data

#kiva country code no info

def open_csv_countries_of_the_world(data):
    file = 'datasets/countries of the world.csv'
    #Country -> nome
    #Region -> NOT USED (regiao)
    #Population -> populacao
    #Area (sq. mi.) -> area (converter para km2)
    #Pop. Density (per sq. mi.) -> densidade_populacional (converter para km2)
    #Coastline (coast/area ratio) -> tem_costa (converter para boolean, ou NOT USED (costa_area))
    #Net migration -> migracao_liquida
    #Infant mortality (per 1000 births) -> mortalidade_infantil
    #GDP ($ per capita) -> gdp
    #Literacy (%) -> literacia
    #Phones (per 1000) -> telefones_por_1000
    #Arable (%) -> NOT USED (araveis)
    #Crops (%) -> NOT USED (culturas)
    #Other (%) -> NOT USED (outros)
    #Climate -> NOT USED (clima)
    #Birthrate -> taxa_natalidade
    #Deathrate -> taxa_de_mortalidade
    #Agriculture -> NOT USED (agricultura)
    #Industry -> NOT USED (industria)
    #Service -> NOT USED (servicos)  
    with open(file, 'r', encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            original_name = row['Country'].strip()
            row['Country'] = treatCountryName(row['Country'])
            if row['Country'] not in data:
                data[row['Country']] = {}
            old_data = data[row['Country']]
            if old_data == {}:
                data[row['Country']]['nome'] = []
                old_data = { 
                    'area': '', 
                    'capital': '', 
                    'densidade populacional': '', 
                    'espetativa de vida' : '', 
                    'exportacoes': '', 
                    'gdp': '', 
                    'hemisferio': '', 
                    'importacoes': '', 
                    'lado em que conduz': '', 
                    'latitude': '', 
                    'literacia': '', 
                    'longitude': '', 
                    'migracao liquida': '', 
                    'moeda': '', 
                    'mortalidade infantil': '', 
                    'populacao': '', 
                    'taxa de mortalidade': '', 
                    'taxa de natalidade': '', 
                    'telefones por 1000': '', 
                    'costa' : '', 
                    'temperatura media': '', 
                    'racio sexos': '', 
                    'taxa desemprego': '', 
                    'taxa fertilidade': '', 
                    'medicos por mil': '', 
                    'receita imposto': '', 
                    'emissoes co2' : '', 
                }
            

            if original_name not in data[row['Country']]['nome']:
                data[row['Country']]['nome'].append(original_name)
            
            if old_data['populacao'] == '':
                data[row['Country']]['populacao'] = row['Population']

            if old_data['area'] == '':
                data[row['Country']]['area'] = float(row['Area (sq. mi.)']) * 2.58999

            if old_data['densidade populacional'] == '':
                if is_float(row['Pop. Density (per sq. mi.)']):
                    data[row['Country']]['densidade populacional'] = float(row['Pop. Density (per sq. mi.)']) * (1/2.58999)
                else:
                    data[row['Country']]['densidade populacional'] = ''

            if old_data['costa'] == '':
                if is_float(row['Coastline (coast/area ratio)']):
                    realcostline = float(row['Coastline (coast/area ratio)']) * float(row['Area (sq. mi.)']) * 2.58999
                    data[row['Country']]['costa'] = realcostline
                else:
                    data[row['Country']]['costa'] = ''

            if old_data['migracao liquida'] == '':
                data[row['Country']]['migracao liquida'] = row['Net migration']

            if old_data['mortalidade infantil'] == '':
                data[row['Country']]['mortalidade infantil'] = row['Infant mortality (per 1000 births)']

            if old_data['gdp'] == '':
                data[row['Country']]['gdp'] = row['GDP ($ per capita)']

            if old_data['literacia'] == '':
                data[row['Country']]['literacia'] = row['Literacy (%)']

            if old_data['telefones por 1000'] == '':
                data[row['Country']]['telefones por 1000'] = row['Phones (per 1000)']

            if old_data['taxa de natalidade'] == '':
                data[row['Country']]['taxa de natalidade'] = row['Birthrate']

            if old_data['taxa de mortalidade'] == '':
                data[row['Country']]['taxa de mortalidade'] = row['Deathrate']


    return data

            

def clean_datasets():
    with open('datasets/world-data-2023.csv', 'r+', encoding='UTF-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            line.replace('#', '')
            f.write(line)
        f.truncate()

    with open('datasets/country_profile_variables.csv', 'r+', encoding='UTF-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            line = line.replace('-99', '')
            line = line.replace('Viet Nam', 'Vietnam')
            f.write(line)
        f.truncate()

    with open('datasets/countries of the world.csv', 'r+', encoding='UTF-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            line = re.sub(r'(\d+),(\d+)', r'\1.\2', line)  # Assign the result of re.sub() back to line
            f.write(line)
        f.truncate()



def read_all_csv():
    data = {}
    clean_datasets()
    data = open_csv_world_data_2023(data)
    data = open_csv_contry_profile_variables(data)
    data = open_csv_countries_of_the_world(data)
    return data
    
def main():
    data = read_all_csv()
    with open('datasets/countries.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    


if __name__ == '__main__':
    main()