from django.contrib import admin
from .models import *

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher_name', 'created_at']
    class Meta:
        model = Teachers

@admin.register(Abouts)
class AboutsAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']
    class Meta:
        model = Abouts


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']
    class Meta:
        model = Contacts

