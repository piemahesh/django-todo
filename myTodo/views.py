from django.shortcuts import render,redirect
from .db import students
# Create your views here.
def getLoginPage(req):
    return render(req,"Login.html")


def registerPage(req):
    print("hi im hitted")
    if(req.method == "POST"):
        reqMethod = req.POST
        email = reqMethod.get("email")
        password = reqMethod.get("password")
        confirmPassword = reqMethod.get("confirmPassword")
        if(password == confirmPassword):
            data = {"email": email, "password": password}
            print(data)
            students.insert_one(data)
            return redirect('loginPage')
        else:
            print("password is mismatched")
    return render(req,"register.html")


def task(req):
    return render(req,"task.html")