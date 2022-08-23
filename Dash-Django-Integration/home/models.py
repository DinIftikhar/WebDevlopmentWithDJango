from symtable import SymbolTableFactory
from tokenize import Name
from turtle import setx
from django.db import models

class HR(models.Model):
    Name = models.CharField(max_length=50)
    Dep_Id = models.IntegerField()
    Salary=models.IntegerField()
    #sex=models.TextChoices('Male', 'Female')
    age=models.IntegerField()

    def get_data(self):
        return self.Name, self.Dep_Id,self.Salary, self.age