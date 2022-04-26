from django.db import models

# Create your models here.
DEPARTMENTS=(
    ('Computer Science','Computer Science'),
    ('Mathematics','Mathematics'),
    ('Chemistry','Chemistry'),
    ('Physics','Physics'),
)

PROGRAM_TYPE=(
    ('UG','UG'),
    ('PG','PG'),
)


class Accounts(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_hod = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Department(models.Model):
    program_type=models.CharField(max_length=10, choices=PROGRAM_TYPE)
    dept_name = models.CharField(max_length=30, choices=DEPARTMENTS)
    hod= models.OneToOneField(Accounts, on_delete=models.cascade, primary_key=True)

    def __str__(self):
        return self.dept_name+' ('+self.program_type+')'