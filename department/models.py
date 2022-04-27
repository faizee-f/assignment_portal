from django.db import models
from accounts.models import User

DEPARTMENTS = (
    ("Computer Science", "Computer Science"),
    ("Mathematics", "Mathematics"),
    ("Chemistry", "Chemistry"),
    ("Physics", "Physics"),
)

PROGRAM_TYPE = (
    ("UG", "UG"),
    ("PG", "PG"),
)


class Department(models.Model):
    program_type = models.CharField(max_length=10, choices=PROGRAM_TYPE)
    dept_name = models.CharField(max_length=30, choices=DEPARTMENTS)
    hod = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.dept_name + " (" + self.program_type + ")"
