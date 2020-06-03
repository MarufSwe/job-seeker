from django.contrib import admin
from .models import Personals, Professionals, EducationLevel, Degree, Academics, Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'token']


class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ['organization_name', 'organization_type', 'designation', 'user_id']


admin.site.register(Personals)
admin.site.register(Professionals, ProfessionalAdmin)
admin.site.register(EducationLevel)
admin.site.register(Degree)
admin.site.register(Academics)

