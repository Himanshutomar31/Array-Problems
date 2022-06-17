# Define a class, which have a class parameter and have a same instance parameter.

class Car:
    def __init__(self, name) -> None:
        self.name = name

    def print_name(self):
        print(self.name)


c = Car("BMW")
print(c.print_name())
