from django.shortcuts import render,redirect
from .db import students
from .services import checkUser
from .validate import registerValidation
# Create your views here.
def getLoginPage(req):
    return render(req,"Login.html")


def registerPage(req):
    try:
        print("hi im hitted")
        if(req.method == "POST"):
           
            reqMethod = req.POST
            email = reqMethod.get("email")
            password = reqMethod.get("password")
            confirmPassword = reqMethod.get("confirmPassword")
            if(registerValidation(email, password, confirmPassword)):
                if(not checkUser(email,password)):
                    data = {"email": email, "password": password}
                    students.insert_one(data)
                    return redirect('loginPage')
                else:
                    print("user already exists")
                    return render(req,"register.html",{"data":"user already exists"})
                
        else:
            print("password is mismatched")
        return render(req,"register.html")
    except Exception as e:
        print(f"Error occurred while registering user: {e}")
        return render(req,"register.html",{"data":str(e)})
        


def task(req):
    return render(req,"task.html")