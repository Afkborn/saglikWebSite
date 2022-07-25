
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from ckeditor.fields import RichTextField


class Language(models.Model):
    name = models.CharField(max_length=50, blank=True)
    abbreviated_name = models.CharField(max_length=8, blank=True)
    
    def __str__(self) -> str:
        return f"{str(self.abbreviated_name).upper()}"
    
def get_default_lang():
    try:
        return Language.objects.get(pk=1)
    except:
        defaultLang = Language(name="Türkçe",abbreviated_name="tr")
        defaultLang.save()
        return Language.objects.get(abbreviated_name="tr")


class Person(models.Model):
    """Person model, all fields are required, except for the image field. The image field is optional. first_name,last_name and position type is CharField"""
    first_name = models.CharField(max_length=30, help_text="İsim")
    last_name = models.CharField(max_length=30, help_text="Soyisim")
    position = models.CharField(max_length=30,help_text="Pozisyon")
    photo = models.ImageField(upload_to="person_image", default= "person_image/default.png")
    lang = models.ForeignKey(Language,on_delete=models.DO_NOTHING, default=1,help_text="Hangi dile sahip üyelerde gözükeceğini belirler")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} [{self.lang}]"    



class Education(models.Model):
    """Person's education, scholl name and department name are required. start_date and finish_date = IntegerField(), school_name and school_department_name type is CharField"""
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    start_date = models.IntegerField(default=0,help_text="Başlangıç tarihi")
    finish_date = models.IntegerField(default=0,help_text="Bitiş tarihi")
    school_name = models.CharField(max_length=50, help_text="Okul Adı")
    school_department_name = models.CharField(max_length=50,help_text="Bölüm Adı")
    
    def __str__(self):
        return f"{self.school_name} {self.school_department_name} ({self.start_date}-{self.finish_date})"


class JobExperience(models.Model):
    """Person's job experience, business name and position are required. start_date and finish_date = IntegerField(), business_name and position type is CharField"""
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
    """Person's clinical applications, name is required. name: str """
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    name = models.CharField(max_length=80,help_text="Uygulama adı")
    
    def __str__(self):
        return f"{self.name}"

class Certificate(models.Model):
    """Person's certificate model.
    name is required. name type CharField. 
    educator_name and certificate_year are optional. 
    educator_name: str,certificate_year: int"""
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
    """Service model.
    name, brief, instruction, lang are required.
    name: str, brief: str, instruction: str, lang: Language"""
    name = models.CharField(max_length=250,help_text="Servis adı")
    brief = models.TextField()  
    show_home_page = models.BooleanField(default=True, help_text="Ana sayfa da gösterilsin mi?")
    photo = models.ImageField(upload_to="service_image", default= "service_image/default.png")
    lang = models.ForeignKey(Language, on_delete=models.DO_NOTHING,default=1,help_text="Hangi dile sahip üyelerde gözükeceğini belirler")
    instruction = RichTextField()
    
    def __str__(self):
        return f"{self.name} [{self.lang}]"


class Comment(models.Model):
    """User comment."""
    author_first_name = models.CharField(max_length=30, help_text="İsim")
    author_last_name = models.CharField(max_length=30, help_text="Soyisim")
    comment_date = models.DateField(help_text="Tarih")
    is_google_comment = models.BooleanField(default=False,help_text="Google'dan gelen mesaj mi?")
    show_home_page = models.BooleanField(default=True, help_text="Ana sayfa da gösterilsin mi?")
    photo = models.ImageField(upload_to="person_image", default= "person_image/default.png")
    score = models.PositiveSmallIntegerField(help_text="Puan", validators=[MinValueValidator(0),MaxValueValidator(5)], default=0)
    comment = models.CharField(max_length=500,help_text="Yorum")
 
    def __str__(self):
        return f"{self.author_first_name} {self.author_last_name}"
    
    @admin.display
    def getScore(self):
        scoreText = ''
        for _ in range(self.score):
            scoreText += "<span class='fa fa-star checked'></span>"
        for _ in range(5-self.score):
            scoreText += "<span class='fa fa-star'></span>"
        return format_html(scoreText)
    getScore.allow_tags = True
        

    
class HomeScreenSlide(models.Model):
    """Use this model to add slides to the home page"""
    slide_name = models.CharField(max_length=250,help_text="")
    href = models.CharField(max_length=250,help_text="Tıklanıldığında açılacak site konumu", blank=True)
    photo = models.ImageField(upload_to="home_slide_image", default= "home_slide_image/default.png")
    lang = models.ForeignKey(Language, on_delete=models.DO_NOTHING,default=1,help_text="Hangi dile sahip üyelerde gözükeceğini belirler")
    slide_desc = RichTextField(blank=True)
    def __str__(self):
        return f"{self.slide_name} [{self.lang}]"


class Gallery(models.Model):
    """Use this model to store images in gallery"""
    gallery_name = models.CharField(max_length=50,help_text="")
    gallery_desc = models.TextField(blank=True)
    photo = models.ImageField(upload_to="gallery", default= "gallery/default.png")
    lang = models.ForeignKey(Language, on_delete=models.DO_NOTHING,default=1,help_text="Hangi dile sahip üyelerde gözükeceğini belirler")
    show_home_page = models.BooleanField(default=True, help_text="Ana sayfa da gösterilsin mi?")
    def __str__(self):
        return f"{self.gallery_name} [{self.lang}]"