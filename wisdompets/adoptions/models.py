from django.db import models

class Pet(models.Model):
    # Selection Tuples
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    
    #Fields
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    #Fields
    name = models.CharField(max_length=50)

    #Methods
    def __str__(self):
        return self.name