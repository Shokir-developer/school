from django.db import models

class Teacher(models.Model):
	name = models.CharField('Ismi', max_length=100)
	surname = models.CharField('Familyasi', max_length=100)

	def __str__(self):
		return self.name

class Pupil(models.Model):
	KLASS = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),
		('7', '7'),
		('8', '8'),
		('9', '9'),
		)

	name = models.CharField('Ismi', max_length=100)
	surname = models.CharField('Familyasi', max_length=100)
	date = models.DateField('sANA', auto_now=False, null=True)
	info = models.TextField("Ma'lumot")
	klass = models.CharField('Sinfi',max_length=100 ,choices=KLASS)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	images = models.ImageField(null=False, blank=False)

	def __str__(self):
		return self.name
