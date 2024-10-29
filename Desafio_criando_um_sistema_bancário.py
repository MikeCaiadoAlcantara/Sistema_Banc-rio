from datetime import datetime
import os

conta = 0  
quantidade_de_depositos_realizados = 0 
limite_saques_diarios = 3  
quantidade_de_saques_realizados = 0 
saques_realizados = 0 
transacoes_realizadas = 0 
numero_da_agencia = "0001"
numero_da_conta = 0

lista_de_depositos = []
lista_de_saques = []
lista_de_usuarios = []
lista_de_contas = []

def limpar():
    os.system("cls")

def depositar(deposito, /):
    global quantidade_de_depositos_realizados, conta
    quantidade_de_depositos_realizados += 1 
    hora_do_deposito = datetime.now().strftime("%d-%m-%Y %H:%M")
    conta += deposito
    lista_de_depositos.append((deposito, hora_do_deposito))  
    print(f"Valor depositado: R$ {deposito}")
    print(f"\033[32mSaldo em conta: R$ {conta:.2f}\033[m")
    print()

def sacar(*, saque):
    global quantidade_de_saques_realizados, conta, saques_realizados
    if saque > 500:
        print("Seu limite de saque é de R$ 500,00.")
        print(f"\033[32mSaldo em conta: R$ {conta:.2f}\033[m")
        print()
    elif saque > conta:
        print("\033[31mSaldo insuficiente!\033[m")
        print()
    else:
        hora_do_saque = datetime.now().strftime("%d-%m-%Y %H:%M")  
        conta -= saque
        lista_de_saques.append((saque, hora_do_saque))  
        saques_realizados += saque
        quantidade_de_saques_realizados += 1
        print("Retire seu dinheiro na boca do caixa.")
        print(f"\033[32mSaldo restante: R$ {conta:.2f}\033[m")
        print(f"Você já realizou {quantidade_de_saques_realizados} saques hoje.")
        print()    

def extrato(saldo, /, *, depositos, saques):
    print(f"\033[32mSaldo em conta: R$ {saldo:.2f}\033[m")
    
    if depositos:
        total_depositado = sum(valor for valor, _ in depositos)
        print(f"\nTotal dos depósitos: R$ {total_depositado:.2f}")
        print("Depósitos:")
        for i, (valor, hora) in enumerate(depositos, 1):
            print(f"{i}. R$ {valor:.2f} em {hora}")
    else:
        print("Nenhum depósito realizado.")
    
    if saques:
        total_sacado = sum(valor for valor, _ in saques)
        print(f"\nTotal sacado: R$ {total_sacado:.2f}")
        print(f"Você realizou {len(saques)} saques até agora.")
        print("Saques:")
        for i, (saque, hora_2) in enumerate(saques, 1):
            print(f"{i}. R$ {saque:.2f} em {hora_2}")
    else:
        print("Nenhum saque realizado.")
    
def usuario():
    global lista_de_usuarios
    novo_usuario = {
        "Nome": input("Crie um nome de usuário: "),
        "Data de nascimento": input("Digite sua data de nascimento: "),
        "CPF": input("Digite seu CPF: "),
        "Endereço": {
            "Logradouro": input("Digite seu logradouro: "),
            "Número": input("Número: "),
            "Bairro": input("Bairro: "),
            "Cidade": input("Cidade/Estado: ")
        }
    }
    for usuario in lista_de_usuarios:
        if usuario["CPF"] == novo_usuario["CPF"]:
            print("\033[31mCPF já cadastrado!\033[m")
            return None 
    
    print("Usuário cadastrado com sucesso!")
    return novo_usuario  

def salvar_usuario():
    novo_usuario = usuario()
    if novo_usuario:
        lista_de_usuarios.append(novo_usuario)  

def exibir_usuarios():
    if lista_de_usuarios:
        print("\nLista de usuários cadastrados:")
        for i, usuario in enumerate(lista_de_usuarios, 1):
            print(f"Usuário {i}: {usuario['Nome']}, CPF: {usuario['CPF']}")
    else:
        print("\nNenhum usuário cadastrado.")

def criar_conta(cpf):
    global lista_de_contas, numero_da_conta, numero_da_agencia
    for usuario in lista_de_usuarios:
        if usuario["CPF"] == cpf:
            numero_da_conta += 1
            conta = {
                "CPF": cpf,
                "Agência": numero_da_agencia,
                "Número da conta": numero_da_conta
            }
            lista_de_contas.append(conta)
            print("Conta cadastrada com sucesso!")
            print(f"O número da sua conta e agência é {numero_da_agencia}-{numero_da_conta}")
            return  
    print("Você precisa criar um cadastro antes de abrir uma conta.")

while transacoes_realizadas < 10:
    tela = int(input("""Escolha qual operação deseja efetuar:
[1] Depositar 
[2] Sacar
[3] Extrato 
[4] Criar usuário
[5] Lista de usuários
[6] Criar conta
[7] Sair
Digite a opção escolhida: """))
    limpar()
    
    if tela == 1:
        deposito = float(input("Qual valor deseja depositar? R$ "))
        depositar(deposito)
        transacoes_realizadas += 1
        
    elif tela == 2:
        if quantidade_de_saques_realizados >= limite_saques_diarios:
            print("\033[31mVocê atingiu o limite de 3 saques diários!\033[m")
            continue
        saque = float(input("Qual valor deseja sacar? R$ "))
        sacar(saque=saque)
        transacoes_realizadas += 1
        
    elif tela == 3:
        extrato(conta, depositos=lista_de_depositos, saques=lista_de_saques)
    
    elif tela == 4:
        salvar_usuario()
        
    elif tela == 5:
        exibir_usuarios()
        
    elif tela == 6:
        criar_conta(input("Digite seu CPF: "))
        
    elif tela == 7:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")

