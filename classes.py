class Planet:
    shape = "round"  # shared property that didn't change

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f"{self.name} is orbiting in the {self.system}"

    @classmethod
    def commons(cls):
        return f"All planets are {cls.shape} because of gravity"

    @staticmethod
    def spin(speed):
        return f"All planets spins and spins at {speed}"


# hoth = Planet("Hoth", 2000000, 5.5, "Hoth System")
# print(f"Name is: {hoth.name}")
# print(f"Radius is: {hoth.radius}")
# print(f"Gravity is: {hoth.gravity}")
# print(f"System is: {hoth.system}")

# print(hoth.orbit())

# init func passing custom values
naboo = Planet("Naboo", 300000, 8, "Naboo System")
print(f"Name: {naboo.name}")
print(f"Radius is: {naboo.radius}")
print(f"Gravity is: {naboo.gravity}")
print(f"System is: {naboo.system}")
print(naboo.orbit())
# we can do instance.classmethod but not classname.instancemethod
print(Planet.commons())
# same for static methods
print(Planet.spin("a very high speed"))
