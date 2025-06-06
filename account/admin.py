from django.contrib import admin
from .models import Profile
# Register your models here.
@admin.register(Profile)
class adminprofile(admin.ModelAdmin):
    list_display = ['user_type']