from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import BorrowerProfile,User

# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(BorrowerProfile)
