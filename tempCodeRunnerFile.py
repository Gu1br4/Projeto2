lista_funcionario = []
cont = 0
def menu():
    print("1 - Cadastrar funcionário")
    print("2 - Remover funcionários")
    print("3 - Determinar folha de pagamento")
    print("4 - Relatório de funcionários")
    # matricula, nome, codigo_funcao, salario_bruto, percentual de imposto, salario_liquido	de todos os func
    print("5 - Maior salário")
    # matricula, nome, codigo_funcao, salario_bruto, percentual de imposto, salario_liquido	
    print("5 - Mais faltas")
    print("0 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    return opcao
def funcionario():

    funcionario1 = []
    matricula = input("Matricula: ")
    nome = input("Nome: ")
    faltas = int(input("Número de faltas no mês: "))
    desconto = 0
    salario_bruto = 0
    codigo_funcao = input("Código da função (101 para vendedor e 102 para administrativo): ")
    if codigo_funcao == "101":
        valor_vendas = float(input("Valor das vendas: "))
        salario_bruto = float(1500)
        comissao = float(0.09)
        if faltas > 0:
            desconto = (salario_bruto / 30) * faltas
            salario_bruto = salario_bruto - desconto
        salario_final = salario_bruto + (valor_vendas * comissao)

        funcionario1.append([matricula, nome, faltas, codigo_funcao, salario_final])
    elif codigo_funcao == "102":
        salario_bruto = float(input("Salário bruto: "))
        if faltas > 0:
            desconto = (salario_bruto / 30) * faltas
            salario_final = salario_bruto - desconto
        funcionario1.append([matricula, nome, faltas, codigo_funcao, salario_final])
    lista_funcionario.append(funcionario1)
    print("funcionario:")
    for x in range(cont):
        print(funcionario1[0])
        print("time:")
        print(lista_funcionario)
cont+=1


def listar():
    for x in range(cont):
        print(lista_funcionario[x][0])
        print(lista_funcionario[x][1])
        print(lista_funcionario[x][2])
        print(lista_funcionario[x][3])
        print(lista_funcionario[x][4])
        print("___________________________")
opcao = menu()
while(opcao != 0):
    if(opcao == 1):
        a = input("Deseja cadastrar um funcionário? (s/n): ")
        if a == "s":
            funcionario()
        else:
            menu()
            
# ###Para cada funcionário existem as seguintes informações:
# • Matrícula
# • Nome
# • Código da função
# • 101 – Vendedor
# • 102 – Administrativo
# • Número de faltas no mês
# • Salário Bruto

# Se o funcionário é Vendedor ele possui um salário fixo mais uma comissão de 9% pelo
# volume de vendas no mês. O salário fixo do vendedor é sempre de R$1500,00
# • Se o funcionário é da Área Administrativa o salário é fixo e varia entre R$2150,00 até
# R$6950,00###