from django.urls import path
from .views import index, add_Teacher, add_Pupil, update_teacher, update_pupil, delete_teacher, delete_pupil, registerpage, loginPage, logoutPage


urlpatterns = [
	path('', index, name='index'),   
	path('addteacher/', add_Teacher, name='add_teacher'),
	path('addpupil/', add_Pupil, name='add_pupil'),
	path('update/<str:pk>/', update_teacher, name='update_teacher'),
	path('pupils/<str:pk>/', update_pupil, name='update_pupil'),

	path('deleteT/<str:pk>/', delete_teacher, name='delete_teacher'),
	path('deleteP/<str:pk>/', delete_pupil, name='delete_pupil'),

	path('register/', registerpage, name='register'),
	path('login/', loginPage, name='login'),
	path('logout/', logoutPage, name='logout'),
]
