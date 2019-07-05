from django.shortcuts import render, redirect

# Create your views here.
from home.forms import StudentSearchForm, StudentEditModelForm, StudentCreateForm, UserRegisterForm
from home.models import Student
from django.contrib import messages
# def home_view(request):
#     return render(request,'home.html')
from django.contrib.auth import login, logout, authenticate


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def home_view(request):
    if request.method == "POST":
        search = StudentSearchForm(request.POST)
        if search.is_valid():
            value = search.cleaned_data.get('q')
            result = Student.objects.filter(student_name__contains=value)
            return render(request, 'home.html', {'result': result, 'form': StudentSearchForm()})
    else:
        form = StudentSearchForm()
        result = Student.objects.all()
        return render(request, 'home.html', {'form': form, 'result': result})
    # msg="hello form from django"
    # context = {'formsssss':form ,'msg':msg }
    # return render(request,'home.html',context)


def deletestudentinfo(request, id):
    result = Student.objects.get(id=id)
    result.delete()
    messages.success(request, "Deleted Successfully !!")
    return redirect('/home/')


def editstudent(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        modelform = StudentEditModelForm(request.POST, instance=student)
        if modelform.is_valid():
            modelform.save()
            messages.success(request, 'Edited Successfully')
            return redirect('/home/')
    else:
        modelform = StudentEditModelForm(instance=student)
        return render(request, 'edit.html', {'form': modelform, 'value': 'Edit'})


def createstudent(request):
    if request.method == "POST":
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            student = Student.objects.create(student_name=form.cleaned_data.get(
                'student_name'), department=form.cleaned_data.get('department'))
            student.save()
            messages.success(request, 'Created Successfully')
            return redirect('/home/')
    else:
        form = StudentCreateForm()
        return render(request, 'create.html', {'form': form, 'value': 'Create'})


def home_view1(request):
    return render(request, 'testpage.html')

# def loginpage(request):
#     return render(request,'auth/login.html')


def user_logout(request):
    logout(request)
    return redirect('/home/')


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserRegisterForm()
    return render(request, 'auth/signup.html', {'form': user_form, 'registered': registered, 'value': 'SignUp'})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/home/')
            else:
                return HttpResponse("Your account was inactive")
        else:
            print("Someone tried to login and failed")
            print("They used username as {} and password as {}".format(
                username, password))
            return HttpResponse("Invalid Login Details given")
    else:
        return render(request, 'auth/login.html', {})
