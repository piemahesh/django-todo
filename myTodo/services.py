from .db import students


def checkUser(email, password):
    try:
        user = students.find_one({"email": email, "password": password})
        print(user)
        print("🎈🎈🎈🎈🎈🎈🎈")
        return True if user else False
    except Exception as e:
        print(f"Error occurred while checking user: {e}")
        return e

