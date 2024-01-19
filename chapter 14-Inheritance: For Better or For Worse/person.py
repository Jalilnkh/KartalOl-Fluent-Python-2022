from collections import OrderedDict
import collections

class Person:

    num_of_persons = 0
    collery_amount = 100
    def __init__(
        self,
        name=None,
        surname=None,
        id=None,
        age=None,
        sex=None,
        nationality=None,
        education=None,
        marriage_status=None,
        init_collery=None
        ) -> None:
        self.name = name
        self.surname = surname
        self.id = id
        self.age = age
        self.sex = sex
        self.nationality = nationality
        self.education = education
        self.marriage_status = marriage_status
        self.init_collery = init_collery
        Person.num_of_persons += 1 

    def graduate(self):
        print(f'This person is graduated from {self.education}')

    def work(self):
        print(f'this person {self.name, self.surname} is working')

    def raise_food(self):
        self.init_collery = self.init_collery + int(self.collery_amount)
        print(f'Collery of food for preson \
            {self.name, self.surname} \
            should be up to \
            {self.init_collery}')

    @classmethod
    def set_collery_amount(cls, amount):
        cls.collery_amount = amount

    @classmethod
    def from_string(cls, person_str):
        if len(person_str.split('-')) != 3:
            raise Exception(f'Check strature of string!!\
                It should have exactly three parts example:\
                jabi-ami-35!!')
        else:
            name, surname, id = person_str.split('-')
        return cls(name, surname, id)
    
    @staticmethod
    def is_old(age):
        if age > 65:
            return True
        else:
            return False
        
class Female(Person):
    pass

class LastUpdateOrderedDict(OrderedDict):

    def __init__(self, a: None, b: None) -> None:
        super().__init__(a, b)

    def __setitem__(self, key: None, value: None) -> None:
        super().__setitem__(self, key, value)
        self.move_to_end(key, value)
    
class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


class AnswerDict(dict):
    def __getitem__(self, key: None) -> None:
        return 42
    
class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

class AnswerDict2(collections.UserDict):
    def __getitem__(self, key: None) -> None:
        return 42

class Root:
    def ping(self):
        print(f'{self}.ping() in Root')
    
    def pong(self):
        print(f'{self}.pong() in Root')

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'
    

class A(Root):
    def ping(self)->None:
        print(f'{self}.ping() in A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()


class B(Root):
    def ping(self)->None:
        print(f'{self}.ping() in B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in B')


class Leaf(A, B):
    def ping(self) -> None:
        print(f'{self}.ping() in Leaf')
        super().ping()

def _upper(key):
    try:
        return key.upper()
    except AttributeError:
        return key

class UpperCaseMixin:
    def __setitem__(self, key, item):
        super().__setitem__(_upper(key), item)

    def __getitem__(self, key):
        return super().__getitem__(_upper(key))
    
    def get(self, key, default=None):
        return super().get(_upper(key), default)
    
    def __contains__(self, key):
        return super().__contains__(_upper(key))


class UpperDict(UpperCaseMixin, collections.UserDict):
    pass


class UpperCounter(UpperCaseMixin, collections.Counter):
    """Specialized 'Counter' that uppercases string keys"""


class ThreadingHTTPServer(
    socketserver.ThreadingMixIn,
    HTTPServer):
    daemon_threads = True
