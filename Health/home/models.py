from email.policy import default
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="person_image", default= "person_image/default.png")
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Education(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    start_date = models.IntegerField(default=0)
    finish_date = models.IntegerField(default=0)
    school_name = models.CharField(max_length=50)
    school_department_name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.school_name} {self.school_department_name} ({self.start_date}-{self.finish_date})"


class JobExperience(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    start_date = models.IntegerField(default=0)
    finish_date = models.IntegerField(default=0)
    business_name = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    def __str__(self):
        return  f"{self.business_name} {self.position} ({self.start_date}-{self.finish_date})"

class ClinicalApplications(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    def __str__(self):
        return f"{self.name}"

class Certificate(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    certificate_year = models.IntegerField(default=0)
    educator_name = models.CharField(max_length=80, default=None, null=True, blank=True)
    def __str__(self):
        return  f"{self.name} - {self.educator_name} ({self.certificate_year})"