from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name , location, language, comment, created_at, updated_at ) VALUES ( %(name)s , %(location)s ,%(language)s ,%(comment)s, NOW() , NOW() );"
        return connectToMySQL('dojo_survey_schema').query_db( query, data )

    @staticmethod
    def validate_survey(dojo):
      is_valid = True # asumimos que esto es true
      if len(dojo['name']) < 1:
        flash("Name can't be null")
        print("Hi1")
        is_valid = False
      if dojo['location'] == "0":
        flash("Must select a location option")
        print("Hi1")
        is_valid = False
      if dojo['language'] == "0":
        flash("Must select a language option")
        print("Hi1")
        is_valid = False
      if len(dojo['comment']) < 1:
        flash("Comment can't be null")
        print("Hi1")
        is_valid = False
      return is_valid
