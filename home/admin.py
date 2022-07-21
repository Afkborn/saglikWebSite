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


#PERSON EDUCATIN, CLINICALAPPLICATIONS, CERTIFICATE, JOBEXPERIENCE
admin.site.register(Person,PersonAdmin)
# admin.site.register(Education)
# admin.site.register(ClinicalApplications)
# admin.site.register(Certificate)
# admin.site.register(JobExperience)

#SERVICE
admin.site.register(Service)

#LANG
admin.site.register(Language)