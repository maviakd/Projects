class Sample:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        print(f"Squaring both numbers {self.x**2} {self.y**2}")

    def add(self):
        print(f"Adding both numbers {self.x + self.y}")

    def run(self):
        Sample.square(self)
        Sample.add(self)


dog = Sample(2, 3)
dog.run()


class AnotherSample(Sample):
    def __init__(self, x, y):
        Sample.__init__(self, x, y)


cat = AnotherSample(1, 2)
cat.run()

class Dog():
        def __init__(self, name):
                self.name = name

        def speak(self):
            return self.name + "says woof"


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says meow"

niko = Dog("niko")
felix = Cat("felix")
for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")

b = (Book(1, 2, 3))
print(b)
print(len(b))
# del b will delete B