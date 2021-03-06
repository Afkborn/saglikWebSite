from email.policy import default
from unicodedata import name
from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=50)
    abbreviated_name = models.CharField(max_length=8)
    def __str__(self) -> str:
        return f"{str(self.abbreviated_name).upper()}"
    
def get_default_lang():
    try:
        return Language.objects.get(pk=1)
    except:
        defaultLang = Language("Türkçe","tr")
        defaultLang.save()
        return Language.objects.get(abbreviated_name="tr")


class Person(models.Model):
    first_name = models.CharField(max_length=30, help_text="İsim")
    last_name = models.CharField(max_length=30, help_text="Soyisim")
    position = models.CharField(max_length=30,help_text="Pozisyon")
    photo = models.ImageField(upload_to="person_image", default= "person_image/default.png")
    lang = models.ForeignKey(Language,on_delete=models.DO_NOTHING, default=1,help_text="Hangi dile sahip üyelerde gözükeceğini belirler")
    def __str__(self):
        return f"{self.first_name} {self.last_name} [{self.lang}]"    



class Education(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    start_date = models.IntegerField(default=0,help_text="Başlangıç tarihi")
    finish_date = models.IntegerField(default=0,help_text="Bitiş tarihi")
    school_name = models.CharField(max_length=50, help_text="Okul Adı")
    school_department_name = models.CharField(max_length=50,help_text="Bölüm Adı")
    def __str__(self):
        return f"{self.school_name} {self.school_department_name} ({self.start_date}-{self.finish_date})"


class JobExperience(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    start_date = models.IntegerField(default=0,help_text="Başlangıç tarihi")
    finish_date = models.IntegerField(default=0,help_text="Bitiş tarihi")
    business_name = models.CharField(max_length=50,help_text="İş yerinin adı")
    position = models.CharField(max_length=30,help_text="Pozisyon")
    def __str__(self):
        returnText = ""
        if (self.business_name != None):
            returnText += f"{self.business_name} "
        if (self.position != None):
            returnText += f"{self.position} "
            
        if (self.start_date != 0 and self.finish_date != 0):
            returnText += f"- ({self.start_date}-{self.finish_date}) "
        elif (self.start_date != 0):
            returnText += f"- ({self.start_date}) "
        elif (self.finish_date != 0):
            returnText += f"- ({self.finish_date}) "
        return returnText
    

class ClinicalApplications(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    name = models.CharField(max_length=80,help_text="Uygulama adı")
    def __str__(self):
        return f"{self.name}"

class Certificate(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    name = models.CharField(max_length=80,help_text="Sertifikat adı")
    certificate_year = models.IntegerField(default=0,help_text="Veriliş tarihi")
    educator_name = models.CharField(max_length=80, default="", null=True, blank=True, help_text="Eğitmen adı/yeri")
    def __str__(self):
        returnText = ""
        if (self.name != None):
            returnText += f"{self.name} "
            
        if (self.educator_name != None):
            returnText += f"- {self.educator_name} "

        if (self.certificate_year != 0):
            returnText += f"({self.certificate_year})"
        return returnText
    
    
class Service(models.Model):
    name = models.CharField(max_length=250,help_text="Servis adı")
    brief = models.CharField(max_length=500,help_text="Kısa özet")
    instruction = models.CharField(max_length=5000,help_text="Detaylı açıklama")
    show_home_screen = models.BooleanField(default=False,help_text="Ana ekranda gözüksün mü?")
    photo = models.ImageField(upload_to="service_image", default= "service_image/default.png")
    lang = models.ForeignKey(Language, on_delete=models.DO_NOTHING,default=1,help_text="Hangi dile sahip üyelerde gözükeceğini belirler")
    def __str__(self):
        return f"{self.name} [{self.lang}]"

