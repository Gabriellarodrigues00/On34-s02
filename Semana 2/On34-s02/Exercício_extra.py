# Sistema de uma empreiteira
# Crie um conjunto de funções, dessa vez para uma empreiteira. 

''' Conversor de metros para centímetros
 - Aqui, ele vai poder digitar na sequência a entrada em metros, para ser mostrado depois o valor em centímetros
- Mostre a saída informando qual foi o valor de entrada, e qual o de saída '''

metros = float(input("Digite o valor em metros para converter para centímetros: "))
centímetros = metros*100
print("O valor digitado em metros foi: ", metros, "m", "e a conversão para centímetros é", centímetros, "cm")

''' Calculadora de área de círculo
- Será pedido o raio de um círculo, e depois exibida sua área'''

raio_do_círculo = float(input("Digite o raio do círculo: "))
área_do_círculo = (raio_do_círculo**2)*3.14
print("O valor da área do círculo é: ", área_do_círculo)

'''Calculadora de área de um terreno quadrado
- Aqui, deve se calcular a área do terreno
- Também deve se calcular o dobro da área'''

print("Para descobrir o tamanho do terreno que você quer calcular: ")
lado = float(input("Digite o tamanho do lado em metros: "))
comprimento = float(input("Digite o tamanho do comprimento em metros: "))
área_do_terreno = lado*comprimento
dobro_da_área = área_do_terreno*2
print("O tamanho da área do terreno é: ", área_do_terreno, "m²", "e o dobro da área do terreno é: ", dobro_da_área, "m²")


'''Cálculo de temperatura do local da obra - FaFahrenheit para Celsius
- Peça a entrada em Fahrenheit, e mostre a saída em Celsius
- C = 5 * ((F-32) / 9)'''

Fahrenheit = float(input("Digite o valor da temperatura em Fahrenheit (°F): "))
Celsius = 5 * ((Fahrenheit-32) / 9)
print("A temperatura do local da obra em Celsius é: ", Celsius, "°C")

'''Cálculo da temperatura do local da obra - Celsius para Fahrenheit'''

Celsius1 = float(input("Digite o valor da temperatura em Celsius (°C): "))
Fahrenheit1 = Celsius*(9/5) + 32
print("A temperatura do local da obra em Fahrenheit é: ", Fahrenheit1, "°F")


'''Calculadora das horas de trabalho totais dos obreiros
-Deve se informar a quantidade de trabalhadores para a obra, quanto cada um ganha por hora, e as horas trabalhadas por mês
-Calcule o valor bruto do salário final de um obreiro, e o custo total de salários de todos os obreiros para o mês referido'''

quantidade_trabalhadores = float(input("Digite a quantidade de trabalhadores para a obra:"))
ganho_por_hora = float(input("Digite o valor pago por hora para cada trabalhador: "))
horas_trabalhadas_mês= float(input("Digite a quantidade de horas trabalhadas por mês pelo trabalhador: "))

valor_bruto_salário_final_obreiros = ganho_por_hora*horas_trabalhadas_mês

custo_total_salários_todos_mês = valor_bruto_salário_final_obreiros*quantidade_trabalhadores

print("O valor bruto do salário final de um obreiro é: R$ ", valor_bruto_salário_final_obreiros, ". Sendo o custo total de salário de todos os obreiros para o mês de Junho: R$ ", custo_total_salários_todos_mês )


'''Calculadora do salário líquido de um obreiro
- Pergunte quanto um obreiro ganha por hora e o número de horas trabalhadas no mês
- De acordo com a tabela do IR de 2024, e considerando que a contribuição ao INSS é de 8%, e ao Sindicato é 5%, retorne na saída:'''

valor_horas_trabalhadas = float(input("Digite o valor pago por sua hora trabalhada:"))
quantidade_horas_trabalhadas_mês = float(input("Digite quantas horas foram trabalhadas no mês: "))
salário_bruto = valor_horas_trabalhadas*quantidade_horas_trabalhadas_mês
IR = float(input("Digite o valor pago em IR:"))
INSS = (salário_bruto/100)*8
Sindicato = (salário_bruto/100)*5
Salário_Líquido = salário_bruto-IR-INSS-Sindicato

print("+Salário Bruto: R$ ", salário_bruto) 
print("-IR: R$", IR)
print("-INSS(8%): R$", INSS)
print("-Sindicato(5%): R$", Sindicato) 
print("=Salário Liquido: R$", Salário_Líquido)


