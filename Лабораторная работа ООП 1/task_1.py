import doctest

class Tomcat:
    """
    A class representing a tomcat.
    
    Example:
    >>> cat = Tomcat("Semen", 2, "black")
    >>> print(cat.meow_age())
    'meow meow'
    >>> print(cat.mrr())
    'Semen: mrr'
    """
    def __init__(self, name: str, age: int, color: str):
        self.name = None
        self.age = None
        self.color = None
        self.init_name(name)
        self.init_age(age)
        self.init_color(color)

    def init_name(self, name: str) -> None:
        """Initialize the name of the tomcat."""
        if not isinstance(name, str):
            raise TypeError
        self.name = name

    def init_age(self, age: int) -> None:
        """Initialize the age of the tomcat."""
        if not isinstance(age, int):
            raise TypeError
        if age < 0 or age > 40:
            raise ValueError
        self.age = age

    def init_color(self, color: str) -> None:
        """Initialize the color of the tomcat."""
        if not isinstance(color, str):
            raise TypeError
        self.color = color

    def meow_age(self) -> str:
        """Return a string of meows based on the tomcat's age."""
        return 'meow ' * self.age

    def mrr(self) -> str:
        """Return a string containing the tomcat's name and 'mrr'."""
        return f'{self.name}: mrr'

class Pussycat:
    """
    A class representing a pussycat.
    
    Example:
    >>> cat = Pussycat("Kisa", 0, "white")
    >>> print(cat.meow())
    '0 meow'
    >>> print(cat.create_kitty("Mi", Tomcat("Semen", 2, "black")))
    <__main__.Kitty object at 0x00000141733C01C0>
    >>> print(cat.meow())
    '1 meow'
    """
    def __init__(self, name: str, kids: int, color: str):
        self.name = None
        self.kids = None
        self.color = None
        self.init_name(name)
        self.init_kids(kids)
        self.init_color(color)

    def init_name(self, name: str) -> None:
        """Initialize the name of the pussycat."""
        if not isinstance(name, str):
            raise TypeError
        self.name = name

    def init_kids(self, kids: int) -> None:
        """Initialize the number of kids of the pussycat."""
        if not isinstance(kids, int):
            raise TypeError
        if kids < 0:
            raise ValueError
        self.kids = kids

    def init_color(self, color: str) -> None:
        """Initialize the color of the pussycat."""
        if not isinstance(color, str):
            raise TypeError
        self.color = color

    def create_kitty(self, name: str, daddy: Tomcat) -> 'Kitty':
        """Create a kitten with the given name and father (tomcat)."""
        self.kids += 1
        return Kitty(name, self, daddy)

    def meow(self) -> str:
        """Return the number of kids followed by 'meow'."""
        return str(self.kids) + " meow"

class Kitty:
    """
    A class representing a kitten.
    
    Example:
    >>> kitten = Kitty("Mi", Pussycat("Kisa", 0, "white"), Tomcat("Semen", 2, "black"))
    >>> print(kitten.meow())
    'Mi: meow'
    >>> print(kitten.get_parents())
    'Kisa and Semen'
    """
    def __init__(self, name: str, mammy: Pussycat, daddy: Tomcat):
        self.name = None
        self.mammy = None
        self.daddy = None
        self.init_name(name)
        self.init_mammy(mammy)
        self.init_daddy(daddy)

    def init_name(self, name: str) -> None:
        """Initialize the name of the kitten."""
        if not isinstance(name, str):
            raise TypeError
        self.name = name

    def init_mammy(self, mammy: Pussycat) -> None:
        """Initialize the mother (pussycat) of the kitten."""
        if not isinstance(mammy, Pussycat):
            raise TypeError
        self.mammy = mammy

    def init_daddy(self, daddy: Tomcat) -> None:
        """Initialize the father (tomcat) of the kitten."""
        if not isinstance(daddy, Tomcat):
            raise TypeError
        self.daddy = daddy

    def meow(self) -> str:
        """Return the name of the kitten followed by 'meow'."""
        return self.name + ": meow"

    def get_parents(self) -> str:
        """Return a string containing the names of the mother and father."""
        res = self.mammy.name + " and " + self.daddy.name
        return res

if __name__ == "__main__":
    doctest.testmod()
