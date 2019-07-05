from django.db import models

# Create your models here.


class Student(models.Model):
    student_name = models.CharField('Student Name', null=True, max_length=30)
    dept = (
        ('CSE', 'Computer Science'),
        ('MH', 'Mech'),
        ('CV', "Civil"),
    )
    department = models.CharField(
        'Department', choices=dept, blank=True, null=True, max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name


class employee(models.Model):
    name = models.CharField('Employee Name', max_length=30, null=True)
    salary = models.IntegerField('Salary', null=True)
    fields = (
        ('PM', 'Project Manager'),
        ('SE', 'Software Engineer'),
        ('DA', 'Data Analyst'),
    )
    job = models.CharField('Post', max_length=30, choices=fields)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Library(models.Model):
    # deletes student data in main tables n keeps that column null
    sut = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
    # sut = models.ForeignKey('Student',on_delete = models.CASCADE) #deletes student data in all the tables
    books = models.ManyToManyField('Book', null=True)
    library_name = models.CharField('Library', max_length=30, null=True)

    def __str__(self):
        return self.library_name


class Section(models.Model):
    section = models.CharField('Section', max_length=30, null=False)
    advisor = models.OneToOneField(
        'Teacher', on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField('Student', null=False)

    def __str__(self):
        return self.section


class Teacher(models.Model):
    teacher = models.CharField('TeacherName', max_length=30, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teacher


class Book(models.Model):
    book = models.CharField('Book', max_length=30, null=True)

    def __str__(self):
        return self.book
