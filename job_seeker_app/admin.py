from django.contrib import admin

from .models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'password']


class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'mobile', 'email', 'father_name', 'mother_name',
                    'gender', 'religion', 'nid', 'dob']


class ProfessionalInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'company_type', 'employee_id', 'designation', 'department',
                    'responsibilities', 'company_location', 'employment_period']


class EducationLevelAdmin(admin.ModelAdmin):
    list_display = ['name']


class DegreeAdmin(admin.ModelAdmin):
    list_display = ['id', 'degree_name']


class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'board_name']


class AcademicInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'degree', 'board', 'institute_name', 'result', 'year_from', 'year_to']


admin.site.register(CustomUser, UserAdmin)
admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(ProfessionalInfo, ProfessionalInfoAdmin)
admin.site.register(AcademicInfo, AcademicInfoAdmin)
admin.site.register(EducationLevel, EducationLevelAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Board, BoardAdmin)
