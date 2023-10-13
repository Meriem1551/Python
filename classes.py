from spaces.planet import Planet
from spaces.calc import planet_mass, planet_vol

from classes import Planet

# from functions import first
naboo = Planet("Naboo", 300000, 8, "Naboo System")
naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print(f"{naboo.name} has a mass of {naboo_mass} and a volume of {naboo_vol}")
