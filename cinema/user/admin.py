from django.contrib import admin
from user.models import CustomUser

# Register your models here.
class CustomUserInLine(admin.TabularInline):
    model = CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']


admin.site.register(CustomUser, CustomUserAdmin)