conta = 0  
quantidade_de_depositos_realizados = 0 
limite_saques_diarios = 3  
quantidade_de_saques_realizados = 0 
saques_realizados = 0  

lista_de_depositos = []
lista_de_saques = []

while True:
    tela = int(input("""Escolha qual operação deseja efetuar:
[1] Depositar 
[2] Sacar
[3] Extrato 
Digite a opção escolhida: """))
    
    if tela in [1, 2, 3]:
        print("Perfeito")
    else:   
        print("\033[31mSelecione uma opção válida!\033[m\n")
        continue  
    
    if tela == 1:
        quantidade_de_depositos_realizados += 1 
        deposito = int(input("Qual valor deseja depositar? R$"))
        conta += deposito
        lista_de_depositos.append(deposito)  
        print("Valor depositado")
        print(f"\033[32mR${conta:.2f}\033[m")
    
    elif tela == 2:
        if quantidade_de_saques_realizados >= limite_saques_diarios:
            print("\033[31mVocê atingiu o limite de 3 saques diários!\033[m")
            continue
        
        saque = int(input("Qual valor deseja sacar? R$"))
        
        if saque > 500:
            print("Seu limite de saque é de R$500,00.")
        elif saque > conta:
            print("\033[31mSaldo insuficiente!\033[m")
        else:
            conta -= saque
            lista_de_saques.append(saque)  
            saques_realizados += saque
            quantidade_de_saques_realizados += 1 
            print("Retire seu dinheiro na boca do caixa.")
            print(f"\033[32mSaldo restante: R${conta:.2f}\033[m")
            print(f"Você já realizou {quantidade_de_saques_realizados} saques hoje.")
    
    elif tela == 3:
        print(f"O saldo da sua conta é de R${conta:.2f}")
        
        print("\nDepósitos realizados:")
        if lista_de_depositos:
            for i, deposito in enumerate(lista_de_depositos, 1):
                print(f"{i}. R${deposito:.2f}")
        else:
            print("Nenhum depósito realizado.")
        
        print("\nSaques realizados:")
        if lista_de_saques:
            for i, saque in enumerate(lista_de_saques, 1):
                print(f"{i}. R${saque:.2f}")
        else:
            print("Nenhum saque realizado.")
        
        print(f"\nTotal de saques realizados hoje: {quantidade_de_saques_realizados}")
        print(f"Valor total sacado hoje: R${saques_realizados:.2f}")
