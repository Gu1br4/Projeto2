lista_funcionario = {}
cont = 0

def menu():
    print("1 - Cadastrar funcionário")
    print("2 - Remover funcionários")
    print("3 - Determinar folha de pagamento")
    print("4 - Relatório de funcionários")
    print("5 - Maior salário")
    print("6 - Mais faltas")
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
    if salario < 2259.2:
        imposto = 0
    elif salario >= 2259.2 and salario < 2828.65:
        imposto = 0.075
    elif salario >= 2828.65 and salario < 3751.05:
        imposto = 0.15
    elif salario >= 3751.05 and salario < 4664.68:
        imposto = 0.225
    elif salario > 4664.68:
        imposto = 0.275
    return salario * imposto

def funcionario():
    print("-" * 30)
    matricula = input("Matricula: ")
    if matricula in lista_funcionario:
        print("Matricula já cadastrada")
        return
    nome = input("Nome: ")
    faltas = int(input("Número de faltas no mês: "))
    desconto = 0
    salario_bruto = 0
    salario_liquido = 0
    codigo_funcao = input("Código da função (101 para vendedor e 102 para administrativo): ")
    
    if codigo_funcao == "101":
        valor_vendas = float(input("Valor das vendas: "))
        salario_base = 1500
        comissao = 0.09
        desconto = (salario_base / 30) * faltas
        salario_bruto = salario_base - desconto + (valor_vendas * comissao)
        salario_liquido = salario_bruto - calc_imposto(salario_bruto)
        
    elif codigo_funcao == "102":
        salario_base = float(input("Salário bruto: "))
        desconto = (salario_base / 30) * faltas
        salario_bruto = salario_base - desconto
        salario_liquido = salario_bruto - calc_imposto(salario_bruto)
    
    funcionario1 = {
        "nome": nome,
        "faltas": faltas,
        "codigo_funcao": codigo_funcao,
        "salario_base": salario_base,
        "salario_bruto": salario_bruto,
        "salario_liquido": salario_liquido,
        "desconto": desconto
    }
    
    lista_funcionario[matricula] = funcionario1
    print("Funcionário cadastrado com sucesso.")
    print("-" * 30)

def mostrar_todos_usuarios():
    if not lista_funcionario:
        print("Não há funcionários cadastrados.")
        return
    print("\t Funcionários Cadastrados \t")
    print("-" * 30)
    for matricula, dados in lista_funcionario.items():
        print(f"\tFuncionario {matricula}")
        print(f"Matricula: {matricula}")
        print(f"Nome: {dados['nome']}")
        print(f"Faltas: {dados['faltas']}")
        print(f"Código da função: {dados['codigo_funcao']}")
        print(f"Salário base: {dados['salario_base']:.2f}")
        print(f"Salário bruto: {dados['salario_bruto']:.2f}")
        print(f"Desconto por faltas: {dados['desconto']:.2f}")
        print(f"Salário líquido: {dados['salario_liquido']:.2f}")
        print(f"Imposto: {(dados['salario_bruto'] - dados['salario_liquido']):.2f}")
        print("-" * 30)

def folha_pagamento():
    
    print("-" * 30)
    print("Folha de pagamento")
    x = input("Digite a matricula do funcionário que deseja ver a folha de pagamento: ")
    
    if x in lista_funcionario:
        funcionario = lista_funcionario[x]
        print(f"Matricula: {x}")
        print(f"Nome: {funcionario['nome']}")
        print(f"Faltas: {funcionario['faltas']}")
        print(f"Código da função: {funcionario['codigo_funcao']}")
        print(f"Salário base: {funcionario['salario_base']:.2f}")
        print(f"Salário bruto: {funcionario['salario_bruto']:.2f}")
        print(f"Desconto por faltas: {funcionario['desconto']:.2f}")
        print(f"Salário líquido: {funcionario['salario_liquido']:.2f}")
        print(f"Imposto: {(funcionario['salario_bruto'] - funcionario['salario_liquido']):.2f}")
        
    else:
        print("Matricula não cadastrada")
    print("-" * 30)

def maior_salario():
    print("-" * 30)
    print("\tFuncionário com maior salário")
    
    if not lista_funcionario:
        print("Não há funcionários cadastrados.")
        return
    
    matricula_maior_salario = None
    maior_salario = 0
    for matricula, dados in lista_funcionario.items():
        if dados['salario_liquido'] > maior_salario:
            maior_salario = dados['salario_liquido']
            matricula_maior_salario = matricula
            
    funcionario_maior_salario = lista_funcionario[matricula_maior_salario]
    print(f"Matricula: {matricula_maior_salario}")
    print(f"Nome: {funcionario_maior_salario['nome']}")
    print(f"Código da função: {funcionario_maior_salario['codigo_funcao']}")
    print(f"Salário bruto: {funcionario_maior_salario['salario_bruto']:.2f}")
    print(f"Salário líquido: {funcionario_maior_salario['salario_liquido']:.2f}")
    print(f"Imposto: {(funcionario_maior_salario['salario_bruto'] - funcionario_maior_salario['salario_liquido']):.2f}")
    print("-" * 30)

def mais_faltas():
    print("-" * 30)
    print("\tFuncionário com mais faltas")
    
    if not lista_funcionario:
        print("Não há funcionários cadastrados.")
        return
    
    matricula_mais_faltas = None
    mais_faltas = 0
    for matricula, dados in lista_funcionario.items():
        if dados['faltas'] > mais_faltas:
            mais_faltas = dados['faltas']
            matricula_mais_faltas = matricula
            
    funcionario_mais_faltas = lista_funcionario[matricula_mais_faltas]
    print(f"Matricula: {matricula_mais_faltas}")
    print(f"Nome: {funcionario_mais_faltas['nome']}")
    print(f"Código da função: {funcionario_mais_faltas['codigo_funcao']}")
    print(f"Salário bruto: {funcionario_mais_faltas['salario_bruto']:.2f}")
    print(f"Salário líquido: {funcionario_mais_faltas['salario_liquido']:.2f}")
    print(f"Imposto: {(funcionario_mais_faltas['salario_bruto'] - funcionario_mais_faltas['salario_liquido']):.2f}")
    print("-" * 30)
    
opcao = menu()

while opcao != 0:
    if opcao == 1:
        a = input("Deseja cadastrar um funcionário? (s/n): ")
        if a == "s":
            funcionario()
        else:
           opcao=menu()
    elif opcao == 2:
        matricula = input("Digite a matricula do funcionário que deseja remover: ")
        remover(matricula)
    elif opcao == 3:
        folha_pagamento()
    elif opcao == 4:
        mostrar_todos_usuarios()
    elif opcao == 5:
        maior_salario() 
    elif opcao == 6:    
        mais_faltas()   
    
    opcao = menu()