from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PW_REGEX = re.compile(r"^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$")

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
 
    @classmethod
    def create(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , password, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s ,%(password)s, NOW() , NOW() );"
        return connectToMySQL('user_schema').query_db( query, data )
    
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM users"
        result = connectToMySQL('user_schema').query_db(query)
        users = []
        for user in result:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('user_schema').query_db(query,data)
        
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def getOneByEmail(cls,email):
        query = "SELECT * FROM users WHERE email = %(email)s"
        data = {'email':email}
        result = connectToMySQL('user_schema').query_db(query,data)
        if not result:
            return " "
        return cls(result[0])
    
    @staticmethod
    def validate_user(user):
        is_valid = True 
   
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False  
        if User.getOneByEmail(user["email"]):
            flash('Email already in database')
            is_valid = False
        if len(user['fname']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(user['lname']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if not PW_REGEX.match(user['password']): 
            flash("password should be at least 8 characters with one uppercase and one number no special characters!")
            is_valid = False
        if user['password'] != user["cpassword"]:
            flash("Both passwords don't match")
            is_valid = False
        return is_valid
    
   
    
   