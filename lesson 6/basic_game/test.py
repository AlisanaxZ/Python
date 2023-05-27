class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def compare_age(person1, person2):
        if person1.age == person2.age:
            print(person1.name, "and", person2.name, "are of the same age")
        if person1.age < person2.age:
            print(person2.name, "is older than", person1.name)
        else:
            print(person1.name, "is older than", person2.name)
        
trau = Person("Trau", 11)
william = Person("William", 13)
compare_age(trau, william)

