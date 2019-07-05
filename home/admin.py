from django.contrib import admin

# Register your models here.

from home.models import Student,employee,Library,Teacher,Book,Section

# admin.site.register(Student) 
# admin.site.register(employee)
# admin.site.register(Library)
# admin.site.register(Teacher)
# admin.site.register(Book)
# admin.site.register(Section)

#ONE MORE WAY TO REGISTER

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields=('department','student_name')
    list_filter=('department','student_name','timestamp')
    fields = ('department','student_name','pic')

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass