from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    def __str__(self):
        return 'Предмет :'[self.name]

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return 'Імя вчителя :'[self.name]

class Class(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(default= 1)
    def __str__(self):
        return 'клас :'[self.name]

class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)
    def __str__(self):
        return 'Імя учня :'[self.name]
    
class Schedule(models.Model):
    name = models.CharField(max_length=10)
    student = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return 'Розклад :'[self.name]

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return 'Оцінка :'[self.name]
