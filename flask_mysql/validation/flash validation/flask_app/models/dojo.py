from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.loca_select = data['loca_select']
        self.language = data['lang_select']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if dojo['loca_select'] == "none":
            flash("Choose one location.")
            is_valid = False
        if dojo['lang_select'] == "none":
            flash("Choose at least one language.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid