import requests
URL_BASE = 'http://localhost:5000/api/contacorrente/'

class Deposito:
    def __init__(self, agencia, conta, deposito):
        self.agencia = agencia
        self.conta = conta
        self.deposito = deposito

    def fazer_deposito(self, token):
        hed = {'Authorization': 'Bearer ' + token}
        r = requests.post(URL_BASE+'deposito', json=self.__dict__, headers = hed)
        if r.status_code == 200:
            return r.text

class ContaCorrente:
    def __init__(self, agencia, conta, saldo,userId):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.userId = userId

    def criarConta(self, token):
        hed = {'Authorization': 'Bearer ' + token}
        r = requests.post(URL_BASE, json=self.__dict__, headers = hed)
        if r.status_code == 200:
            return True

    