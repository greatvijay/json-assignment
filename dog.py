class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name} has a {self.coat_color} coat color.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, hunting_skill):
        super().__init__(name, age, coat_color)
        self.hunting_skill = hunting_skill

    def skill_level(self):
        print(f"{self.name} has a hunting skill level of {self.hunting_skill}.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def show_weight(self):
        print(f"{self.name} weighs {self.weight} pounds.")


# Creating objects and implementing functionalities
dog1 = Dog("Buddy", 3, "brown")
dog1.description()
dog1.get_info()

dog2 = JackRussellTerrier("Romeo", 2, "white", "high")
dog2.description()
dog2.get_info()
dog2.skill_level()

dog3 = Bulldog("Rocky", 5, "black", 60)
dog3.description()
dog3.get_info()
dog3.show_weight()
