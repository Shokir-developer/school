from django.contrib import admin
from .models import Teacher, Pupil

class AdminTeacher(admin.ModelAdmin):
	list_display = ['name', 'surname']
	list_display_links = ['name', 'surname']
	list_filter = ['name']

class AdminPupil(admin.ModelAdmin):
	list_display = ['name', 'surname', 'date', 'info', 'klass', 'teacher']
	list_display_links = ['name', 'surname']

admin.site.register(Teacher, AdminTeacher)
admin.site.register(Pupil, AdminPupil)
