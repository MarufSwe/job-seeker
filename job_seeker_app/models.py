from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=250)

    def __str__(self):
        return str(self.token)

# model Personals start
class Personals(models.Model):
    class Gender(models.TextChoices):
        MALE = 'Male', _('MALE')
        FEMALE = 'Female', _('FEMALE')
        OTHERS = 'Others', _('OTHERS')

    class Religion(models.TextChoices):
        ISLAM = 'Islam', _('ISLAM')
        HINDUISM = 'Hinduism', _('HINDUISM')
        BUDDHISM = 'Buddhism', _('BUDDHISM')
        CRISTIAN = 'Christianity', _('CRISTIAN')
        OTHERS = 'Others', _('OTHERS')

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField()
    gender = models.CharField(max_length=50, default=True, choices=Gender.choices)
    religion = models.CharField(max_length=50, default=True, choices=Religion.choices)
    nid = models.PositiveSmallIntegerField()

    class Meta:
        # ordering = ['-id']
        verbose_name_plural = 'Personals'

    def __str__(self):
        return self.first_name
        # model Personals end


# model Professionals start


class Professionals(models.Model):
    class OrganizationType(models.TextChoices):
        GOVERNMENT = 'Government', _('GOVERNMENT')
        SEMI_GOVERNMENT = 'Semi Government', _('SEMI_GOVERNMENT')
        NGO = 'NGO', _('NGO')
        PRIVATE_FIRM = 'Private firm', _('OTHERS')
        INTERNATIONAL_AGENCY = 'International Agency', _('INTERNATIONAL_AGENCY')
        OTHERS = 'Others', _('OTHERS')

    class Department(models.TextChoices):
        ACCOUNTING = 'Government', _('ACCOUNTING')
        BANK = 'Bank', _('BANK')
        ENGINEER = 'Engineer', _('ENGINEER')
        GARMENTS = 'Garments', _('GARMENTS')
        HR = 'HR', _('HR')
        OTHERS = 'Others', _('OTHERS')

    organization_name = models.CharField(max_length=100)
    organization_type = models.CharField(max_length=50, default=True, choices=OrganizationType.choices)
    department = models.CharField(max_length=50, default=True, choices=Department.choices)
    designation = models.CharField(max_length=100)
    responsibilities = models.CharField(max_length=100)
    employment_from = models.DateField(default=False, null=True, blank=True)
    employment_to = models.DateField(default=False, null=True, blank=True)
    company_location = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        # ordering = ['-id']
        verbose_name_plural = 'Professionals'

    def __str__(self):
        return self.organization_name

    # model Professionals end


class EducationLevel(models.Model):
    edu_level_name = models.CharField(max_length=100)


class Degree(models.Model):
    degree_name = models.CharField(max_length=100)


def current_year():
    return datetime.date.today().year


# model Academics start


class Academics(models.Model):
    class Board(models.TextChoices):
        DHAKA = 'DHAKA', _('DHAKA')
        RAJSHAHI = 'RAJSHAHI', _('RAJSHAHI')
        COMILLA = 'COMILLA', _('COMILLA')
        JESSORE = 'JESSORE', _('JESSORE')
        CHITTAGONG = 'CHITTAGONG', _('CHITTAGONG')
        BARISHAL = 'BARISHAL', _('BARISHAL')
        SYLHET = 'SYLHET', _('SYLHET')
        DINAJPUR = 'DINAJPUR', _('DINAJPUR')
        MADRASAH = 'MADRASAH', _('MADRASAH')

    board = models.CharField(max_length=20, choices=Board.choices, default=Board.DHAKA)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    result = models.FloatField(default=0.00)
    year = models.IntegerField(_('year'), default=current_year)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # ordering = ['-id']
        verbose_name_plural = 'Academics'

    def __str__(self):
        return self.board
# model Academics end




"""This code used for dynamic year field creation"""
# import datetime
#
# def year_choices():
#     return [(r, r) for r in range(1984, datetime.date.today().year + 1)]
#
# def current_year():
#     return datetime.date.today().year
#
# class MyModel(models.Model):
#     year = models.IntegerField(_('year'), choices=year_choices, default=current_year)
