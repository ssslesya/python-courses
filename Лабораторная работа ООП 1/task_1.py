import doctest


class Tomcat:
    # """
    #     >>> cat = Tomcat("Semen", 2, "black")
    #     >>> print(cat.meow_age())
    #     meow meow
    #     >>> print(cat.mrr())
    #     Semen: mrr
    # """

    def __init__(self, name, age, color):
        self.name = None
        self.init_name(name)

        self.age = None
        self.init_age(age)

        self.color = None
        self.init_color(color)

    def init_name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.name = name

    def init_age(self, age):
        if not isinstance(age, (int, float)):
            raise TypeError
        if age < 0 or age > 40:
            raise ValueError
        self.age = age

    def init_color(self, color):
        if not isinstance(color, str):
            raise TypeError
        self.color = color

    def meow_age(self):
        return self.age * "meow "

    def mrr(self):
        return self.name + ": mrr"


class Pussycat:
    # """
    #     >>> cat = Pussycat("Kisa", 0, "white")
    #     >>> print(cat.meow())
    #     0 meow
    #     >>> print(cat.create_kitty("Mi", Tomcat("Semen", 2, "black")))
    #     <__main__.Kitty object at 0x00000141733C01C0>
    #     >>> print(cat.meow())
    #     1 meow
    # """
    def __init__(self, name, kids, color):
        self.name = None
        self.init_name(name)

        self.kids = None
        self.init_kids(kids)

        self.color = None
        self.init_color(color)

    def init_name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.name = name

    def init_kids(self, kids):
        if not isinstance(kids, (int, float)):
            raise TypeError
        if kids < 0:
            raise ValueError
        self.kids = kids

    def init_color(self, color):
        if not isinstance(color, str):
            raise TypeError
        self.color = color

    def create_kitty(self, name: str, daddy: Tomcat):
        self.kids += 1
        return Kitty(name, self, daddy)

    def meow(self):
        res = str(self.kids) + " meow"
        return res


class Kitty:
    # """
    #     >>> kitten = Kitty("Mi", Pussycat("Kisa", 0, "white"), Tomcat("Semen", 2, "black"))
    #     >>> print(kitten.meow())
    #     Mi: meow
    #     >>> print(kitten.get_parents())
    #     Kisa and Semen
    # """
    def __init__(self, name, mammy, daddy):
        self.name = None
        self.init_name(name)

        self.mammy = None
        self.init_mammy(mammy)

        self.daddy = None
        self.init_daddy(daddy)

    def init_name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.name = name

    def init_mammy(self, mammy):
        if not isinstance(mammy, Pussycat):
            raise TypeError
        self.mammy = mammy

    def init_daddy(self, daddy):
        if not isinstance(daddy, Tomcat):
            raise TypeError
        self.daddy = daddy

    def meow(self):
        return self.name + ": meow"

    def get_parents(self):
        res = self.mammy.name + " and " + self.daddy.name
        return res


if __name__ == "__main__":
    doctest.testmod()
