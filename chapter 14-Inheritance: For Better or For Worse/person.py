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
        print(f'Collery of food for preson {self.name, self.surname} should be up to {self.init_collery}')

    @classmethod
    def set_collery_amount(cls, amount):
        cls.collery_amount = amount

    @classmethod
    def from_string(cls, person_str):
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