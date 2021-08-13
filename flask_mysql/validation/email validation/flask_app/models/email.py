from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import email
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails"
        results = connectToMySQL('email').query_db( query)

        return results
    
    @classmethod
    def create(cls, data ):
        query = "INSERT INTO emails (address ,created_at, updated_at ) VALUES ( %(address)s , NOW() , NOW() );"
        return connectToMySQL('email').query_db( query, data )
    
    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['address']):
            flash("Invalid email address!",'error')
            is_valid = False
        return is_valid
    