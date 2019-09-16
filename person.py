class Person:
    def __init__(self, age, first_name, last_name, catch_phrase):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase

    def walk(self):
        print("Walking")

user = Person(25, "Jon", "Snow", "You know nothing")
print(user.catch_phrase)

user.walk()
