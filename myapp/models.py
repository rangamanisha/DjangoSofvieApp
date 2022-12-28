from django.db import models

# Create your models here.
class StateModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CityModel(models.Model):
    state = models.ForeignKey(StateModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CompanyModel(models.Model):
    company_name  = models.CharField(max_length=120)
    dob = models.DateTimeField()
    state = models.ForeignKey(StateModel,on_delete=models.CASCADE)
    city = models.ForeignKey(CityModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name