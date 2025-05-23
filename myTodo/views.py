from django.shortcuts import render,redirect,HttpResponse
from .db import students
from .services import checkUser
from .validate import registerValidation
import bcrypt
import re
# Create your views here.
def getLoginPage(req):
    try:
        userId = req.session.get("userId")
        if userId:
            return redirect('taskPage')
        
        if(req.method == "POST"):
            reqMethod = req.POST
            email = reqMethod.get("email")
            password = reqMethod.get("password")
            if(checkUser(email)):
                user = students.find_one({"email": email})
                hashed = user["password"]
                if bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8")):
                    req.session['userId'] = str(user["_id"])
                    
                    return render(req,'task.html',{"data":"login successfully"})
                else:
                    print("password is incorrect")
                    return render(req,"Login.html",{"data":"password is incorrect"})
            else:
                print("user not found")
                return render(req,"Login.html",{"data":"user not found"})
    except Exception as e:
        print(f"Error occurred while getting login page: {e}")
        return render(req,"Login.html",{"data":str(e)})
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
                    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode('utf-8')
                    print("hashed password",hashed)
                    data = {"email": email, "password": hashed}
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
    userId = req.session.get("userId")
    if not userId:
        return redirect('loginPage')
    studentCol = students.find()
    studentsData = []
    for student in studentCol:
        studentsData.append(student)
    return render(req,"task.html",{"data":studentsData})


def logout(req):
    try:
        req.session.flush()
        return redirect('loginPage')
    except Exception as e:
        print(f"Error occurred while logging out: {e}")
        return redirect('loginPage')
    
    
def viewSpeficTask(req):
    userId = req.session.get("userId")
    if not userId:
        return redirect('loginPage')
    mydata = [
        {
            "task": "Task 1",
            "description": "Description for Task 1",
            "status": "Completed"
        },
        {
            "task": "Task 2",
            "description": "Description for Task 2",
            "status": "Pending"
        },
        {
            "task": "Task 3",
            "description": "Description for Task 3",
            "status": "In Progress"
        }
    ]
    return render(req,"viewTask.html",{"data":mydata})