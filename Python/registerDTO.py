import requests
import json

URL_BASE = 'http://localhost:5000/users'
class registerDto:
    def __init__(self,firstName,lastName,userName, password):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.password = password

    def register(self):
        return requests.post(URL_BASE+'/register', json=self.__dict__)