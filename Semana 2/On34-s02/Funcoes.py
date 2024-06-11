def calculo_IMC(altura,peso):
    imc = peso/(altura**2)
    print("Seu IMC é:" , imc)

#print(calculo_IMC(1.60,80)) #aqui aparecia o none pois a função não tava retornando nada

def calculo_IMC_retorno(altura,peso):
    imc = peso/altura**2
    return imc

#print(calculo_IMC_retorno(1.60,80)) #aqui já é o valor retornado

retorno_funcao = calculo_IMC_retorno(1.6,80)
print(retorno_funcao)


################

def desconto_salario(salario) :
    salario = (salario/10)*3
    print("O desconto será de", salario)

#quando eu for chamar
desconto_salario(1000)

###########
def gorjeta_garcom(conta) :
    gorjeta = conta/10
    return gorjeta

print(gorjeta_garcom(500))
    

