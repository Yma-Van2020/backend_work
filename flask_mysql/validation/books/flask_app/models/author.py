from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
from flask_app.models import favorite

class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
       
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL('books').query_db(query)
        
        return results
    
    @classmethod
    def get_author_with_books( cls , data ):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books').query_db( query , data )
        
        author = cls( results[0] )
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja( ninja_data ) ) 
        return dojo
    

    