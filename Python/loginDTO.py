import requests
import json


URL_BASE = 'http://localhost:5000/users'

class Login:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
    
    def login(self):
        r = requests.post(URL_BASE+'/authenticate', json=self.__dict__)
        if r.status_code == 200:            
            return json.loads(r.text)['token'], json.loads(r.text)['id']
        elif r.status_code == 400:
            return  json.loads(r.text)['message'] , 0
        