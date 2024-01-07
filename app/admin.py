from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('Name', 'RollNumber', 'Department', 'Sem', 'Year', 'Sgpa', 'Type')
    search_fields = ('Name', 'RollNumber', 'Department', 'Sem', 'Year', 'Sgpa', 'Type')
    list_filter = ('Department', 'Sem', 'Year', 'Type')