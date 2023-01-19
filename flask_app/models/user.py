from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash 



class User: 
    db = 'iqra'
    def __init__(self,data): 
        self.id = data['id']
        self.admin = data['admin']
        self.password = data['password']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( admin, password, createdAt, updatedAt ) VALUES (%(admin)s, %(password)s, NOW() , NOW() );"
        return connectToMySQL(cls.db).query_db( query, data )

