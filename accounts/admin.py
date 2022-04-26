from django.contrib import admin

from accounts.models import Accounts, Department

# Register your models here.

admin.site.register(Accounts)
admin.site.register(Department)