from pymongo import MongoClient

mongo = MongoClient("mongodb://localhost:27017/")
# database
db = mongo.studentDB 
# collection
students = db.students

