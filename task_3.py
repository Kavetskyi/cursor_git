# Lecture #2 OOP
# Task 3

class DictMixin():
    def to_dict(self):
         return self._convert_dict(self.__dict__)

    def _convert_dict(self, attributes):
        result = {}
        for key, value in attributes.items():
            result[key] = self._convert(key, value)
        return result


    def _convert(self, key, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._convert_dict(value)
        elif isinstance(value, list):
            return [self._convert(key, v) for v in value]
        elif hasattr(value, '__dict__'):
            return self._convert_dict(value.__dict__)
        else:
            return value

class Profile(DictMixin):
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


# Task 3 ( )

class DictMixin():
    def to_dict(self):
        return self.__dict__


class Profile(DictMixin):
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

