from menu import menu_banco
from registerDTO import registerDto
from loginDTO import Login
from ContaCorrenteDTO import ContaCorrente, Deposito

URL_BASE = 'http://localhost:5000'
register = registerDto
opcao = menu_banco()
token = ''
userId = 0



while(opcao != 9):    
    if opcao == 1:
        name = input("Seu primeiro nome: ")
        lastName = input("Seu último nome: ")
        password = input("Sua senha: ")
        userName = f'{name}.{lastName}'
        print("Seu username é: "+userName)

        reg = register(name, lastName, userName, password)
        req = reg.register()
        if req.status_code == 200:
            print("Usuário cadastrado com sucesso!")

    elif (opcao == 2):
        userName = input("Digite seu username: ")
        senha = input("Digite sua senha: ")
        l = Login(userName, senha)
        token, userId = l.login()  
        if userId == 0:
            print(token)

    
    elif (opcao == 3):
        agencia = int(input("Digite a agência: "))
        conta = int(input("Digite a conta: "))
        saldo = float(input("Digite o saldo da conta: "))
        c = ContaCorrente(agencia, conta,saldo, userId)
        if c.criarConta(token) == True:
            print("Conta criada com sucesso")
    
    elif (opcao == 4):
        agencia = int(input("Digite a agência: "))
        conta = int(input("Digite a conta: "))
        valor = float(input("Digite o valor do depósito: "))
        D = Deposito(agencia=agencia, conta=conta, deposito=valor)
        print(str(D.fazer_deposito(token=token)))


    opcao = menu_banco()
        



       