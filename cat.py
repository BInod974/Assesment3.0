class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.hungry = True
        self.age_next_year = age + 1

    # Method 1: feed
    def feed(self):
        food = input(f"What will {self.name} eat?: ")
        self.hungry = False
        print(f"\nYay! {self.name} enjoyed the {food}!")

    # Method 2: sleep
    def sleep(self):
        print(f"{self.name} is now sleeping.")

    # Method 3: play
    def play(self, tired):
        if tired:
            print(f"{self.name} is too tired to play. Let them rest.")
        else:
            print(f"{self.name} is having fun playing!")

# Creating pet objects
pet_1 = Pet("Buddy", "dog", 3)
pet_2 = Pet("Mittens", "cat", 2)

# Using methods
pet_1.feed()
pet_2.sleep()
pet_2.play(tired=False)

print(pet_1.species)  # Output: dog
print(f"{pet_1.name}'s age next year: {pet_1.age_next_year}")

