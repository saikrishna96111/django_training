from django.urls import path
#from .views import home_view, contact, about, deletestudentinfo, editstudent, createstudent
from .views import *
urlpatterns = [
    path('', home_view),
    # path('',views.home_view)
    path('delete/<id>', deletestudentinfo),
    path('contact/', contact),
    path('about/', about),
    path('edit/<id>', editstudent),
    path('create-student/', createstudent),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('register/', register, name="register"),
]
