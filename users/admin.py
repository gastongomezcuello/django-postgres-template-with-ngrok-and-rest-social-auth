from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class ProfileInline(admin.StackedInline):
    model = Profile


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]
    fieldsets = UserAdmin.fieldsets + ()


admin.site.register(User, CustomUserAdmin)
