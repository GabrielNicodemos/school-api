from django.db import models
from django.core.validators import MinLengthValidator

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=False, max_length=254)
    cpf = models.CharField(max_length=11, unique=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediary'),
        ('A', 'Advanced'),
    )

    code = models.CharField(
        max_length=10,
        unique=True,
        validators=[MinLengthValidator(3)]
    )
    description = models.CharField(max_length=255, blank=False)
    level = models.CharField(
        max_length=1,
        choices= LEVEL,
        blank=False,
        null=False,
        default='b'
    )

    def __str__(self):
        return self.code

class Registered(models.Model):
    PERIOD = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('E', 'Evening'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    period = models.CharField(
        max_length=1,
        choices= PERIOD,
        blank=False,
        null=False,
        default='E'
    )