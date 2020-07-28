class Student:

    def __init__(self,name,branch):
        self.name = name
        self.branch = branch

    def statement(self):
        return f'{self.name} is studying {self.branch}'

    def __str__(self):
        return f'{self.name}'