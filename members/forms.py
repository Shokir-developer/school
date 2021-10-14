from django import forms
from .models import Teacher, Pupil

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = '__all__'


class PupilForm(forms.ModelForm):
	class Meta:
		model = Pupil
		fields = '__all__'

class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']