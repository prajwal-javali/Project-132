import csv
import plotly.express as pe

rows = []

with open ("data.csv", "r") as f:
    a = csv.reader(f)
    for row in a:
        rows.append(row)


headers = rows[0]
planet_data_rows = rows[1:]

# print(headers)
# print(planet_data_rows[0])


headers[0] = "row_num" 


solar_system_planet_count = {}

for planet_data in planet_data_rows:
    if solar_system_planet_count.get(planet_data[11]) :
        solar_system_planet_count[planet_data[11]] += 1
    else:
        solar_system_planet_count[planet_data[11]] = 1

max_ss = max(solar_system_planet_count, key = solar_system_planet_count.get) 

print("The solar system " , max_ss , ", has maximun planets -" , solar_system_planet_count[max_ss]) 


temp_planet_data_rows = list(planet_data_rows)

for planet_data in temp_planet_data_rows:
    planet_mass = planet_data[3]
    if planet_mass.lower() == "unknown":
        planet_data_rows.remove(planet_data)
        continue
    else:
        planet_mass_value = planet_mass.split(" ")[0]
        planet_mass_ref = planet_mass.split(" ")[1]
        if planet_mass_ref == "Jupiters":
            planet_mass_value = float(planet_mass_value) * 317.8
        planet_data[3] = planet_mass_value

    planet_radius = planet_data[7]
    if planet_radius.lower() == "unknown":
        planet_data_rows.remove(planet_data)
        continue
    else:
        planet_radius_value = planet_radius.split(" ")[0]
        planet_radius_ref = planet_radius.split(" ")[2]
    if planet_radius_ref == "Jupiter":
        planet_radius_value = float(planet_radius_value) * 11.2
    planet_data[7] = planet_radius_value

print(len(planet_data_rows))


# 19.4 Jupiters

# 1.08 x Jupiter

# ---------------------------------------------------- c 132 ----------------------------------------------------------

hd_10180_planets = []
for planet_data in planet_data_rows:
  if max_ss == planet_data[11]:
    hd_10180_planets.append(planet_data)

print(len(hd_10180_planets))
print(hd_10180_planets)


hd_10180_planet_masses = []

hd_10180_planet_names = []

for p in hd_10180_planets:
    hd_10180_planet_masses.append(p[3])     
    hd_10180_planet_names.append(p[1])     


hd_10180_planet_masses.append(1)
hd_10180_planet_names.append(['earth'])     

fig = pe.bar(x=hd_10180_planet_names , y=hd_10180_planet_masses)
# fig.show()


# The Value of G (Gravitational Constant) is 6.674e-11

# Mass of Earth = 5.972e+24

# Radius of Earth = 6371000


temp_planet_data_rows = list(planet_data_rows)
for planet_data in temp_planet_data_rows:
  if planet_data[1].lower() == "hd 100546 b":
    planet_data_rows.remove(planet_data)

planet_masses = []

planet_radius = []

planet_names = []

for p in planet_data_rows:
    planet_masses.append(p[3])
    planet_radius.append(p[7])
    planet_names.append(p[1])

planet_gravity = []
for index, name in enumerate(planet_names):
    # g = G + MassofEarth/radius*radius
    gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radius[index])*float(planet_radius[index])*6371000*6371000) * 6.674e-11
    planet_gravity.append(gravity)

fig = pe.scatter(x=planet_radius, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
# fig.show()

low_gravity_planets = []

for index , gravity in enumerate(planet_gravity):
    if gravity < 100:
        low_gravity_planets.append(planet_data_rows[index])
    
print(len(low_gravity_planets))

planet_type_values = []
for planet_data in planet_data_rows:
  planet_type_values.append(planet_data[6])

print(list(set(planet_type_values)))
