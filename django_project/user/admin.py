from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,healthworker,patient
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(healthworker)
admin.site.register(patient)
