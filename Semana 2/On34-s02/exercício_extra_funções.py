import math

def metros_para_centrimetros():
    metros = float(input("Digite o valor em metros: "))
    centimetros = metros * 100
    print (metros, "metros equivalem a", centimetros, "centímetros")

def area_circulo():
    raio = float(input("Digite o raio do círculo: "))
    area = math.pi * raio**2
    print("A área do círculo com raio", raio, "é", format(area, ".2f"))

def area_terreno_quadrado():
    lado = float(input("Digite o lado do terreno quadrado"))
    area = lado**2
    dobro_area = area * 2
    print("A área do terreno é: ", format(area, ".2f"), "e o dobro da área é", format(dobro_area, ".2f"))

def fahrenheit_para_celcius():
    fahrenheit = float(input("Digite a temperatura em fahrenheit: "))
    celcius = 5*((fahrenheit-32)/9)
    print(fahrenheit, "graus fahrenheit equivalem a", format(celcius, ".2f"), "graus celcius")

def celcius_para_fahrenheit():
    celcius = float(input("Digite a temperatura em celcius: "))
    fahrenheit = (celcius* 9/5) + 32
    print(celcius, "graus equivalem a", format(fahrenheit, ".2f"), "graus fahrenheit")

def calcular_salario():
    num_trabalhadores = int(input("Digite o número de trabalhadores: "))
    valor_hora = float(input("Digite o valor da hora trabalhada: "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas por mês: "))

    salario_bruto = valor_hora*horas_trabalhadas
    inss = salario_bruto*0.08
    sindicato = salario_bruto*0.05

    if salario_bruto <= 2259.2:
        ir = 0
    elif salario_bruto <=2826.65:
        ir = salario_bruto*0.0075 - 169.44
    elif salario_bruto <= 3751.05:
        ir = salario_bruto*0.15 - 381.44
    elif salario_bruto <= 4664.68:
        ir = salario_bruto*0.225 - 662.7
    else:
        ir = salario_bruto * 0.275 - 896.36

    salario_liquido = salario_bruto - ir - inss - sindicato

    print("Cálculo do salário: ")
    print("+ salário bruto: R$", format(salario_bruto,".2f"))
    print("- ir(", format(ir/salario_bruto, ".1%"), "): R$", format(ir, ".2f"))
    print("- inss(8%): R$", format(inss, ".2f"))
    print("-sindicato(5%): R$", format(sindicato, ".2f"))
    print("= Salário líquido por trabalhador: R$", format(salario_liquido, ".2f"))

while True:
    print("SISTEMA PARA EMPREITERA CANTINHO DA CONSTRUTORA")
    print("Escolha uma opção: ")
    print("1. Metros para centímetros")
    print("2. Área do círculo")
    print("3. Área do terreno quadrado")
    print("4. Fahrenheit para Celsius")
    print("5. Celsius para Fahrenheit")
    print("6. Calcular salário")
    print("0. Sair")

    opcao = input("opção: ")

    if opcao == "1":
        metros_para_centrimetros()
    elif opcao =="2":
        area_circulo()
    elif opcao == "3":
        area_terreno_quadrado()
    elif opcao == "4":
        fahrenheit_para_celcius()
    elif opcao =="5":
        celcius_para_fahrenheit()
    elif opcao =="6":
        calcular_salario()
    elif opcao == "0":
        print("Até mais!")
        break
    else:
        print("Opção inválida")
    




