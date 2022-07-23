from django.contrib import admin

# Register your models here.
from .models import  *

class EducationInline(admin.TabularInline):
    model = Education
class ClinicalApplicationsInline(admin.TabularInline):
    model = ClinicalApplications
class CertificateInline(admin.TabularInline):
    model = Certificate
class JobExperienceInline(admin.TabularInline):
    model = JobExperience
class PersonAdmin(admin.ModelAdmin):
    inlines = [
        EducationInline,
        ClinicalApplicationsInline,
        CertificateInline,
        JobExperienceInline
    ]
    list_display = ('first_name', 'last_name','position', 'lang')
    list_filter = ("lang",)
    search_fields = ['first_name', 'last_name']
#PERSON EDUCATIN, CLINICALAPPLICATIONS, CERTIFICATE, JOBEXPERIENCE
admin.site.register(Person,PersonAdmin)


#SERVICE
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'brief','lang')
    list_filter = ("lang",)
    search_fields = ['name']
admin.site.register(Service, ServiceAdmin)

#LANG
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviated_name')
    search_fields = ['name']
admin.site.register(Language,LanguageAdmin)

#COMMENT
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_first_name', 'author_last_name','lang', 'score')
    list_filter = ("lang",)
    search_fields = ['author_first_name','author_last_name']
    
admin.site.register(Comment)