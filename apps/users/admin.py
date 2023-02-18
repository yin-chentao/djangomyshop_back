# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import *


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
	list_display = ['username', 'email', 'is_active', 'truename', 'mobile']

