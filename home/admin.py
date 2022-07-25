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
    list_filter = ("lang","show_home_screen")
    search_fields = ['name']
admin.site.register(Service, ServiceAdmin)

#LANG
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviated_name')
    search_fields = ['name']
admin.site.register(Language,LanguageAdmin)

#COMMENT
from django_object_actions import DjangoObjectActions
from datetime import datetime
from home.google.getComment import getCommentFromGoogle
from django.contrib import messages
class CommentAdmin(DjangoObjectActions,admin.ModelAdmin):
    def get_comment_from_Google(modeladmin, request, queryset):
        new_comment_count = 0
        comment_list = getCommentFromGoogle()
        for i in comment_list:
            comment_list = Comment.objects.filter(comment_date=i.comment_date,author_first_name=i.author_first_name,author_last_name=i.author_last_name)
            if (len(comment_list) == 0):
                i.save()
                new_comment_count += 1
        if new_comment_count > 0:
            messages.add_message(request, messages.INFO, f'Toplam {new_comment_count} yeni yorum eklendi.')
        else:
            messages.add_message(request, messages.INFO, f'Yeni mesaj yok.')
    get_comment_from_Google.label = "Get Comment from Google"
    list_display = ('author_first_name', 'author_last_name', 'score', 'is_google_comment', 'show_home_page')
    list_filter = ('show_home_page','is_google_comment')
    search_fields = ['author_first_name','author_last_name']
    changelist_actions = ('get_comment_from_Google', )

    
admin.site.register(Comment,CommentAdmin)



#HomeScreenSlide
class HomeScreenSlideAdmin(admin.ModelAdmin):
    list_display = ('slide_name','lang')
    list_filter = ("lang",)
    search_fields = ['slide_name']
    
admin.site.register(HomeScreenSlide,HomeScreenSlideAdmin)