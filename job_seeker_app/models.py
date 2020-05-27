from django.db import models


# Create your models here.

class CustomUser(models.Model):
    user_name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.user_name


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=14)
    email = models.EmailField(max_length=50)
    father_name = models.CharField(max_length=35)
    mother_name = models.CharField(max_length=35)
    gender = models.CharField(max_length=10)
    religion = models.CharField(max_length=15)
    nid = models.CharField(max_length=50)
    dob = models.DateField(max_length=25)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)


class ProfessionalInfo(models.Model):
    company_name = models.CharField(max_length=50)
    company_type = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=25)
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    responsibilities = models.CharField(max_length=100)
    company_location = models.CharField(max_length=100)
    employment_period = models.CharField(max_length=25)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)


class EducationLevel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Degree(models.Model):
    degree_name = models.CharField(max_length=50)

    def __str__(self):
        return self.degree_name


class Board(models.Model):
    board_name = models.CharField(max_length=50)

    def __str__(self):
        return self.board_name


class AcademicInfo(models.Model):
    result = models.CharField(max_length=15)
    year_from = models.DateField(max_length=10)
    year_to = models.DateField(max_length=10)
    institute_name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, default=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
