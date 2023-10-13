from classes import Planet

# from functions import first
naboo = Planet("Naboo", 300000, 8, "Naboo System")
print(f"Name: {naboo.name}")
print(f"Radius is: {naboo.radius}")
print(f"Gravity is: {naboo.gravity}")
print(f"System is: {naboo.system}")
print(Planet.spin("a very high speed"))
# We can import functions as well
