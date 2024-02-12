class Pet:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is a pet."

    def __repr__(self) -> str:
        return f"Pet(name={self.name}, age={self.age})"


class Dog(Pet):

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self) -> str:
        return "Woof!"

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"


class Cat(Pet):

    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color

    def murr(self) -> str:
        return "Murr..."

    def __str__(self) -> str:
        return f"{self.name} is a {self.color} cat."

    def __repr__(self) -> str:
        return f"Cat(name={self.name}, age={self.age}, color={self.color})"


if __name__ == "__main__":
    # Usage:
    dog = Dog("Buddy", 3, "Golden Retriever")
    print(dog)
    print(dog.make_sound())
    print(repr(dog))

    cat = Cat("Whiskers", 5, "Tabby")
    print(cat)
    print(cat.murr())
    print(repr(cat))
    pass
