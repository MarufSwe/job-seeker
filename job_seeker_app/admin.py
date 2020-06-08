from django.contrib import admin
from .models import Personals, Professionals, EducationLevel, Degree, Academics, Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'token']


class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ['organization_name', 'organization_type', 'designation', 'user_id']


class AcademicsAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'degree', 'board', 'institution', 'result','year']

class DegreeAdmin(admin.ModelAdmin):
    list_display = ['id', 'degree_name']

admin.site.register(Personals)
admin.site.register(Professionals, ProfessionalAdmin)
admin.site.register(EducationLevel)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Academics, AcademicsAdmin)

