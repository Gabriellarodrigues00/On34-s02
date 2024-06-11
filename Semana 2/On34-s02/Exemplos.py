#Númericos - int e float

numero1 = 1
print(numero1)
print(type(numero1))
print("o tipo de váriavel numero1 é: " , type(numero1))

numero2 = 7.4
print(numero2)
print("o tipo de váriavel numero2: ", type(numero2))

numero3 = 400
print(numero3)
print("o tipo de váriavel numero3: ", type(numero3))

# Booleano
trouxe_carteira = False
print("o tipo de váriavel trouxe_carteira é: ", type(trouxe_carteira))

#String
# texto = "valor do texto em aspas duplas"
#texto = 'valor do texto em aspas simples'
#texto = '''valor do texto em três aspas simples'''
# texto = """"valor do texto em três aspas duplas"""

texto="Um passo à frente e você não está mais no mesmo lugar, Chico Science"
print(texto)
print("o tipo de váriavel texto é: ", type(texto))

# Inputs
entrada=input("Digite um texto: ")
print("O valor do  Input é: ", entrada)

nome= "Gabriella"
print("olá", nome)

# Nome das variáveis - regrinhas
exemplo12345 = True #apenas nomes e números, começar por uma letra
# sem acento gráfico
endereço_residencia= "Rua x, 345"       #podemos ter underlines
endereço_trabalho = "Avenida Berimboca, 355" #sempre dar nomes coerentes

entrada1 = input("informe o primeiro valor: ")
entrada2= input("informe o segundo valor: ")

print(type(entrada1))
print(type(entrada2))

concat = entrada1+entrada2
print(concat)
print("tipo do concat: ", type(concat))
