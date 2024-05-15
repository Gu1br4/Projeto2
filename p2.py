#perguntar onde usar dicionario

lista_funcionario = {}
cont = 0
def menu():
    print("1 - Cadastrar funcionário")
    print("2 - Remover funcionários")
    print("3 - Determinar folha de pagamento")
    print("4 - Relatório de funcionários")
    print("5 - Maior salário")
    print("5 - Mais faltas")
    print("6 - Ver funcionários")
    print("0 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

def remover(matricula):
        if matricula in lista_funcionario:
            lista_funcionario.pop(matricula)
            print(f"Funcionário com matricula {matricula} removido")
            print("Nova lista de funcionários:")
            print(lista_funcionario)
        else:
            print("Matricula não cadastrada")

def calc_imposto(salario):
    imposto = 0
    if(salario<2259.2):
        imposto = 0
    elif(salario>=2259.2 and salario<2828.65):
        imposto = 0.075
    elif(salario>=2828.65 and salario<3751.05):
        imposto = 0.15
    elif(salario>=3751.05 and salario<4664.68):
        imposto = 0.225
    elif(salario>4664.68):
        imposto = 0.275
    return (salario*imposto)

def funcionario():

    funcionario1 = {}
    matricula = input("Matricula: ")
    if matricula in lista_funcionario:
        print("Matricula já cadastrada")
        matricula = input("Matricula: ")
    nome = input("Nome: ")
    faltas = int(input("Número de faltas no mês: "))
    desconto = 0
    salario_liquido = float(0)
    salario_bruto = 0
    codigo_funcao = input("Código da função (101 para vendedor e 102 para administrativo): ")
    if codigo_funcao == "101":
        valor_vendas = float(input("Valor das vendas: "))
        salario_bruto = float(1500)
        comissao = float(0.09)
        if faltas > 0:
            desconto = (salario_bruto / 30) * faltas
            salario_bruto = salario_bruto - desconto
        salario_liquido = salario_bruto + (valor_vendas * comissao)
        salario_liquido =salario_liquido-calc_imposto(salario_liquido)
        funcionario1 = {matricula:[nome, faltas, codigo_funcao,salario_bruto, salario_liquido, desconto]}
    elif codigo_funcao == "102":
        salario_bruto = float(input("Salário bruto: "))
        if faltas > 0:
            desconto = (salario_bruto / 30) * faltas
            salario_bruto = salario_bruto - desconto
        salario_liquido=salario_bruto-calc_imposto(salario_bruto)
        funcionario1 = {matricula:[nome, faltas, codigo_funcao,salario_bruto, salario_liquido, desconto]}
    lista_funcionario.update(funcionario1)
    print("funcionario:")
    for x in range(cont):
        print(funcionario1)
        print("time:")
        print(lista_funcionario)
cont+=1

def folha_pagamento():
    print("Folha de pagamento")
    print(lista_funcionario)
    x = input("Digite a matricula do funcionário que deseja ver a folha de pagamento: ")
    for i in lista_funcionario:
        if i == x:
            print(f"Matricula: {i}")
            print(f"Nome: {lista_funcionario[i][0]}")
            print(f"Faltas: {lista_funcionario[i][1]}")
            print(f"Código da função: {lista_funcionario[i][2]}")
            print(f"Salário bruto com faltas: {lista_funcionario[i][3]}")
            print(f"Salário sem faltas: {lista_funcionario[i][3]+lista_funcionario[i][5]}")
            print(f"Salário líquido: {lista_funcionario[i][4]}")
            print(f"imposto: {lista_funcionario[i][3]-lista_funcionario[i][4]}")
            print(f"desconto por faltas: {lista_funcionario[i][5]}") 
        else:
            print("Matricula não cadastrada")

opcao = menu()
while(opcao != 0):
    if (opcao == 1):
        a = input("Deseja cadastrar um funcionário? (s/n): ")
        if a == "s":
            funcionario()
        else:
           opcao=menu()

    elif (opcao == 2):
        matricula = input("Digite a matricula do funcionário que deseja remover: ")
        remover(matricula)
        opcao = menu()
    
    elif (opcao == 3):
        folha_pagamento()
        opcao = menu()
