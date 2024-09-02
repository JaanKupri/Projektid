# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}


# test function by updating damages
def recorded_damages(damages):
  i = 0
  for damage in damages:
    if "M" in damage:
      damage = float(damage[:-1])
      damage = damage * conversion["M"]
      damages[i] = damage
    elif "B" in damage:
      damage = float(damage[:-1])
      damage = damage * conversion["B"]
      damages[i] = damage
    i += 1
recorded_damages(damages)


# 2 
# Create a Table
hurricanes = {}

# Create and view the hurricanes dictionary
for index in range(0, len(names)):
  hurricane = {"Name": names[index],
 "Month": months[index],
 "Year": years[index],
 "Max Sustained Wind": max_sustained_winds[index],
 "Areas Affected": areas_affected[index],
 "Damage": damages[index],
 "Deaths": deaths[index]}
  hurricanes[names[index]] = hurricane
  

#print(hurricanes)
# 3
# Organizing by Year
hurricanes_by_year = {}
for hurricane in hurricanes.values():
  current_cane = hurricane
  current_year = hurricane["Year"]
  if current_year not in hurricanes_by_year:
    hurricanes_by_year[current_year] = [current_cane]
  else:
    hurricanes_by_year[current_year].append(current_cane)




# create a new dictionary of hurricanes with year and key


# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in


# 5 
# Calculating Maximum Hurricane Count

max_count = 0
max_count_hurricane = ""

affected_area_count = {}
for hurricane in hurricanes.values():
  areas = hurricane["Areas Affected"]
  for area in areas:
    if area not in affected_area_count:
      affected_area_count[area] = 1
    else:
      affected_area_count[area] += 1

l = list(affected_area_count)
#print(l[0])
# find most frequently affected area and the number of hurricanes involved in


# 6
# Calculating the Deadliest Hurricane
max_deaths = 0
max_deaths_hurricane = ""

for hurricane in hurricanes.values():
  deaths = hurricane["Deaths"]
  if deaths > max_deaths:
    max_deaths = deaths
    max_deaths_hurricane = hurricane["Name"]

#print(max_deaths_hurricane + ": " + str(max_deaths))
# find highest mortality hurricane and the number of deaths

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
for hurricane in hurricanes.values():
  deaths = hurricane["Deaths"]
  i = -1
  for rating in mortality_scale.values():
    i += 1
    if deaths > 10000:
      hurricanes_by_mortality[5] = hurricane
    if deaths <= rating and hurricane not in hurricanes_by_mortality.values():
      hurricanes_by_mortality[i].append(hurricane)

#print(hurricanes_by_mortality)

# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage
max_damage = 0
max_damage_hurricane = ""
for hurricane in hurricanes.values():
  damage = hurricane["Damage"]
  try:
    float(damage)
    if damage > max_damage:
      max_damage = damage
      max_damage_hurricane = hurricane["Name"]
  except ValueError:
      continue

print(max_damage_hurricane + ": " + str(max_damage))
# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
# categorize hurricanes in new dictionary with damage severity as key
for hurricane in hurricanes.values():
  damage = hurricane["Damage"]
  i = -1
  for rating in damage_scale.values():
    i += 1
    if damage == "Damages not recorded":
      continue
    elif damage > 50000000000:
      hurricanes_by_damage[5] = hurricane
    elif damage <= rating and hurricane not in hurricanes_by_damage.values():
      hurricanes_by_damage[i].append(hurricane)

print(hurricanes_by_damage)
