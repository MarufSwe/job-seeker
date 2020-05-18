from django.db import models


# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.user_name


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField()
    mobile = models.CharField(max_length=14)
    email = models.EmailField(max_length=30)
    father_name = models.CharField(max_length=25)
    mother_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=6)
    religion = models.CharField(max_length=10)
    nid = models.CharField(max_length=50)
    dob = models.DateField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ProfessionalInfo(models.Model):
    company_name = models.CharField(max_length=25)
    company_type = models.CharField(max_length=15)
    employee_id = models.CharField(max_length=15)
    designation = models.CharField(max_length=15)
    department = models.CharField(max_length=15)
    responsibilities = models.CharField(max_length=25)
    company_location = models.CharField(max_length=35)
    employment_period = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Degree(models.Model):
    degree_name = models.CharField(max_length=30)

    def __str__(self):
        return self.degree_name


class EducationLevel(models.Model):
    edu_level_name = models.CharField(max_length=30)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)

    def __str__(self):
        return self.edu_level_name


class Board(models.Model):
    board_name = models.CharField(max_length=30)

    def __str__(self):
        return self.board_name


class AcademicInfo(models.Model):
    result = models.CharField(max_length=15)
    year_from = models.DateField(max_length=10)
    year_to = models.DateField(max_length=10)
    institute_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    education_level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
