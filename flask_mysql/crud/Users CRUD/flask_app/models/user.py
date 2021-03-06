# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, render_template, request, redirect
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        
        results = connectToMySQL('users').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users').query_db( query, data )
    
    @classmethod
    def delete_one(cls, id):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {
            "id": id
        }
        connectToMySQL('users').query_db(query,data)
        
    @classmethod
    def update_one(cls, id):
        query = "UPDATE users SET first_name = %(new_fname)s, last_name = %(new_lname)s, email = %(new_email)s, updated_at = NOW() WHERE id = %(id)s;"
        data = {
            'id': id,
            "new_fname" : request.form["new_fname"],
            "new_lname" : request.form["new_lname"],
            "new_email" : request.form["new_email"]
        }

        connectToMySQL("users").query_db(query,data)
    
        
    
    @classmethod 
    def show_one(cls, id):
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        data = {
            "id":id
        }
        results = connectToMySQL("users").query_db(query,data)
        user = cls(results[0])
        return user
        
  
    