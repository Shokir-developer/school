from django.shortcuts import render, redirect
from .models import Teacher, Pupil
from .forms import TeacherForm, PupilForm, RegisterForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
	teachers = Teacher.objects.all()
	pupils = Pupil.objects.all()

	context = {'teachers':teachers, 'pupils':pupils}
	return render(request, 'index.html', context)

def add_Teacher(request):

	form = TeacherForm()
	if request.method == 'POST':
		form = TeacherForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'teacherAdd.html', context)

def add_Pupil(request):

	form = PupilForm()
	if request.method == 'POST':
		form = PupilForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'pupilAdd.html', context)

def update_teacher(request, pk):
	edit = Teacher.objects.get(id=pk)
	form = TeacherForm(instance=edit)
	if request.method == 'POST':
		form = TeacherForm(request.POST, instance=edit)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'teacherAdd.html', context)

def update_pupil(request, pk):
	edit = Pupil.objects.get(id=pk)
	form = PupilForm(instance=edit)
	if request.method == 'POST':
		form = PupilForm(request.POST, instance=edit)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'pupilAdd.html', context)

def delete_teacher(request, pk):
	remove = Teacher.objects.get(id=pk)
	if request.method == 'POST':
		remove.delete()
	context = {'remove':remove}
	return render(request, 'deleteTeacher.html', context)

def delete_pupil(request, pk):
	remove = Pupil.objects.get(id=pk)
	if request.method == 'POST':
		remove.delete()
	context = {'remove':remove}
	return render(request, 'deletePupil.html', context)

def registerpage(request):
	form = RegisterForm()
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request, 'register.html', context)


def loginPage(request):
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')

	context = {}
	return render(request, 'login.html')

def logoutPage(request):
	logout(request)
	return redirect('login')
