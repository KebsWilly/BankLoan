#from msilib.schema import Property
from django.db import models

# Create your models here.
class approvals(models.Model):
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    Married = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    Education = (
        ('Graduate', 'Graduated'),
        ('Not_Graduate', 'Not_Graduated')
    )
    Employment = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    Property = (
        ('Urban', 'Urban'),
        ('Semiurban', 'Semiurban'),
        ('Rural', 'Rural')
    )
    

    firstname = models.CharField(max_length=12)
    lastname = models.CharField(max_length=12)
    dependants = models.IntegerField(default=0)
    applicantincome = models.IntegerField(default=0)
    coapplicantincome = models.IntegerField(default=0)
    loan_amount = models.IntegerField(default=0)
    loan_term = models.IntegerField(default=0)
    credit_history = models.IntegerField(default=0)
    gender = models.CharField(max_length=18, choices= Gender)
    married = models.CharField(max_length=10, choices= Married)
    education = models.CharField(max_length=18, choices= Education)
    employment_status = models.CharField(max_length=18, choices= Employment)
    area = models.CharField(max_length=18, choices= Property)


    def __str__(self):
        return '{}, {}'.format(self.lastname, self.firstname)