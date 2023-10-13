class Planet:
    def __init__(self):
        self.name = "Hoth"
        self.radius = 2000000
        self.gravity = 5.5
        self.system = "Horh System"

    def orbit(self):
        return f"{self.name} is orbiting in the {self.system}"


hoth = Planet()
print(f"Name is: {hoth.name}")
print(f"Radius is: {hoth.radius}")
print(f"Gravity is: {hoth.gravity}")
print(f"System is: {hoth.system}")

print(hoth.orbit())
