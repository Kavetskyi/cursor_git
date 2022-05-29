# Lecture #2 OOP
# Task 3
import json

class DictMixin():
    def to_dict(self):
        return self.__dict__

class JSONMixin():
    def to_json(self):
        return json.dumps(self.to_dict())

class Profile(DictMixin, JSONMixin):
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_namber = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex


person1 = Profile('Sara', 'Smith', '+39393939', 'Lviv', 'email@email', 'april 22', 30, 'woman')
print(person1.to_dict())
print(person1.to_json())
