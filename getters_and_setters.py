class Person:
    def __init__(self, name):
        self.name = name  # This will trigger the setter

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name - adds '.Junior'
    @name.setter
    def name(self, new_name):
        self._name = new_name + ".Junior"

# Create a Person object
person1 = Person("Tanishq")

# Accessing name
print(f"The new name of the user is: {person1.name}")
