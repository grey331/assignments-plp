# activity 1
# Superhero Class
class Superhero:
    def __init__(self, name, superpower, strength):
        self.name = name
        self.superpower = superpower
        self.strength = strength
    
    def display_info(self):
        print(f"Superhero: {self.name}")
        print(f"Superpower: {self.superpower}")
        print(f"Strength: {self.strength}")
    
    def perform_action(self):
        print(f"{self.name} is saving the day!")

# Inheritance: FlyingSuperhero subclass
class FlyingSuperhero(Superhero):
    def __init__(self, name, superpower, strength, flying_speed):
        super().__init__(name, superpower, strength)
        self.flying_speed = flying_speed
    
    def perform_action(self):
        print(f"{self.name} is flying at {self.flying_speed} km/h!")
    
    def display_info(self):
        super().display_info()
        print(f"Flying Speed: {self.flying_speed} km/h")
        
        
        # activity 2
# Polymorphism: Animal Classes

# Base Animal Class
class Animal:
    def move(self):
        pass  # This will be overridden by subclasses

# Lion Class
class Lion(Animal):
    def move(self):
        print("The lion is running fast")

# Bird Class
class Bird(Animal):
    def move(self):
        print("The bird is flying high ")

# Fish Class
class Fish(Animal):
    def move(self):
        print("The fish is swimming really fast")

# Main execution
if __name__ == "__main__":
    # Creating objects of Superheroes
    hero = Superhero("Iron Man", "Technology", 80)
    flying_hero = FlyingSuperhero("Superman", "Flight", 100, 800)

    # Display info and perform action for Superheroes
    hero.display_info()
    hero.perform_action()
    print()

    flying_hero.display_info()
    flying_hero.perform_action()
    print()

    # Polymorphism in Animals: Creating objects and calling move method
    lion = Lion()
    bird = Bird()
    fish = Fish()

    animals = [lion, bird, fish]

    for animal in animals:
        animal.move()  # Polymorphism in action
