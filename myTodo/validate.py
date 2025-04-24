
def registerValidation(email, password, confirm_password):
    if("@"in email and email.endswith(".com")):
        if(len(password) >= 8):
            if(password == confirm_password):
                return True
            else:
                raise Exception("Password and confirm password do not match.")
        else:
            raise Exception("Password must contain above 8 characters.")
    else:
        raise Exception("Invalid email format. Please enter a valid email address.")
        
        