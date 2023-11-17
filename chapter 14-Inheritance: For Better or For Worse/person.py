class Person:

    name = None
    surname = None
    id = None
    age = None
    sex = None
    blood = None
    nationality = None
    education = None
    marriage_status = None

    def graduate(self):
        print(f'This person is graduated from {self.education}')

    def work(self):
        print(f'this person {self.name, self.surname} is working')