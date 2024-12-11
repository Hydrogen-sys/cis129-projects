class Pet:
    def __init__(self, name, pet_type, age):
        self.name = name
        self.pet_type = pet_type
        self.age = age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_pet_type(self, pet_type):
        self.pet_type = pet_type

    def get_pet_type(self):
        return self.pet_type

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

# Main program
if __name__ == "__main__":
    name = input("Enter your pet's name: ")
    pet_type = input("Enter your pet's type (e.g., dog, cat): ")
    age = input("Enter your pet's age: ")

    my_pet = Pet(name, pet_type, age)

    print("\nPet Details:")
    print(f"Name: {my_pet.get_name()}")
    print(f"Type: {my_pet.get_pet_type()}")
    print(f"Age: {my_pet.get_age()}")
