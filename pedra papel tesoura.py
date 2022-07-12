print("pedra papel tesoura simples.")
print(f'''
pedra
papel
tesoura
''')
loop="positivo"
while loop == "positivo":
    input("escolhe uma das opções: ")
    import random
    resposta = ["pedra", "papel", "tesoura"]
    print (random.choice(resposta))
    #ajuda
if "ajuda":
        print(f'''
        As duas equipes deverão ficar em fila, cada participante
        com as mãos para trás. Quando o coordenador da brincadeira
        der o sinal, uma pessoa de cada equipe deverá mostrar a mão,
        no formato de pedra (mão fechada), papel (mão aberta) ou tesoura
        (dois dedos, indicador e médio, formando um "V").    
        ''')
loop="negativo"