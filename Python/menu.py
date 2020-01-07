import time #importando a função sleep
def menu_banco():
  time.sleep(1) #deixando o menu mais demorado
  opcao = int(input("""\033[1;32m       |--------------| Menu |--------------|
       |(1) Cadastrar                       | 
       |(2) Login                           | 
       |(3) Criar Conta                     |
       |(4) Depósito                        |
       |(4) Saldo                           |
       |(5) Transferência                   |       
       |(6) Saída                           |
       |------------------------------------|    
        \033[m( )Digite aqui:"""))
    
  return opcao