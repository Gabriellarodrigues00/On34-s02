nome = "Carla"
sobrenome = "dos Santos"
print(nome, "" , sobrenome)

conteudo = "Meu ano de nascimento é " + str(2000) #converte número em string
print(conteudo)

#salário = input("Digite o seu salário: ")
#salário_ano = salário*12 #ele entende que é um texto e vai repetir 12x
#print(salário_ano)

#salário1 = input("Digite o seu salário: ")
#salário1= int(salário1)
#salário_ano1 = salário1 *12
#print(salário_ano1)

valor = 5
print(float(valor))
print(bool(0)) #false
print(bool(1)) #true
print(bool("conteudo")) #true
print(bool(""))  #false
print(bool(-200)) #true

'''
Exercício
'''
#   usuário digita dois números
# você retorna:
# soma, multiplicação, potenciação

valor1 = input("Digite o valor 1: ")
valor2 = input("Digite o valor 2: ")

#opção 1 -  soma = int(valor1) + int(valor2) 
#opção 2 
# valor1= int(valor1)
#valor2= int(valor2)
#soma= valor1 + valor2
#opção 3 -  valor1= int(input('digite um número:'))

valor1 = int(valor1)
valor2 = int(valor2)
soma = valor1 + valor2
print("O resultado da soma é: ", soma)

multiplicação =  valor1 * valor2
print("O resultado da Multiplicação é: ", multiplicação)

potenciação = valor1**valor2
print("O resultado da potenciação é: ", potenciação)

#outra maneira
#print("O resultado da soma é", soma, "\n O resultado da multiplicação é", multiplicação, "\n O resultado da potencição é", potenciação)

#Segundo
#usuário digita o valor
# você retorna se um número é par ou ímpar

numero = int(input("Digite um número: ")) #pego a entrada, convertendo
numero_sendo_impar = numero%2 #resto da divisão por 2, se for par, o resto da divisão é zero; se for impar, o resto é 1.
numero_sendo_impar = bool(numero_sendo_impar) #retornará true se tiver 1 e false se tiver 0
print("O número", numero, "é impar?", numero_sendo_impar) # printando se o numero é impar (true) ou não (false)
