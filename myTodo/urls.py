from django.urls import path
from . import views

urlpatterns = [
    path("", views.getLoginPage,name="loginPage"),
    path("register", views.registerPage,name="registerPage"),
    path("task", views.task,name="taskPage"),
    path("logout", views.logout,name="logout"),
    path("view_task", views.viewSpeficTask,name="viewTask"),
]
