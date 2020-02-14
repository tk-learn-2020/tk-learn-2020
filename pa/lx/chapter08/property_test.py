from datetime import date, datetime

class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value

if __name__ == '__main__':
    user = User("zzlion", date(year=1993, month=3, day=3))
    print(user.age)
    user.age = 19
    print(user.age)
    print(user._age)
