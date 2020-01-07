class ContaCorrente:
  def __init__(self,titular,agencia,saldo, cpf):
    self.titular = titular
    self.agencia = agencia
    self.saldo = saldo
    self.cpf = cpf
    
  def deposito(self,valor):
    self.saldo += valor

  def saque(self,valor):
    if(valor <= self.saldo):
      self.saldo -= valor