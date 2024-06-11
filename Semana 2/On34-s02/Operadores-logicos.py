# operador AND - todos precisam ser verdadeiros para ele dar true
and_operador = True and True
print(and_operador)

and_operador = True and False
print(and_operador)

and_operador = False and False
print(and_operador)

and_operador = (12==12) and True
print(and_operador)

and_operador = (12<11) and True
print(and_operador)

# operador OR
or_operador = True or True
print(or_operador)

or_operador = True or False
print(or_operador)

or_operador = False or False
print(or_operador)

or_operador = (12==12) or False
print(or_operador)

# operador NOT
print(not True)
print(not False)
not_operador = (True and False) or (not(True and True))
print(not_operador)

