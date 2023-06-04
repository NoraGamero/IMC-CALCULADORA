# Se realizará el calculo del INDICE DE MASA CORPORAL
# Se da la bienvenida y la intención de la operación
print ("*" * 60)
print (" ¡Bienvenido al calculador del Índice de Masa Corporal (IMC)!\n")
print ("*" * 60)

print ("""Este consiste en medir la relación entre su peso y talla,
y de esta manera conozca mejor su estado de salud.\n""")
print ("-" * 60)

# Se toman en cuenta las personas a realizarce el IMC para imprimirlos juntos
# Si no son entre 1 y 10 se cancela la calculadora
pers = int(input("""Favor de proporcionar el número de personas que desean calcular su IMC 
(máximo 10 personas):\t"""))
if pers > 0 and pers <=10:
    print("Continua")
else:
    print("¡Error en la cantidad de personas! Favor de intententar de nuevo")
    exit(None)
print ("-" * 60) 
     
# Le pediremos el nombre para la diferenciación con las personas
name = input("¿Cual es su nombre?       \t")
# Se le pide la edad, peso y altura
age = int (input("¿Cuántos años tiene?                  \t"))
# Aclara a los menores de edad que puede variar el resultado 
if age < 18:
    print ("        Usted es menor de edad")
    print ("        El resultado puede estar desfazado debido a su crecimiento")
else:
    print ("        Usted es mayor de edad")
weight = float (input("Proporcione su peso (kg)          \t"))
height = float (input("¿De cuántos metros es tu estatura?\t"))
print ("-" * 60) 

# Calculo del IMC
# Formula: IMC = KG/ M**2
IMC = weight / height**2

# Ponderaciones y recomendaciones
print("RESULTADO:")
if IMC < 18.4:
  print("       Peso Bajo \nEs importante subir de peso así se sentirá mejor.")
elif IMC >= 18.5 and IMC <= 24.99:
  print("       Peso Normal \n¡Genial! Que gusto que este en su mejor peso.")
elif IMC >= 25.0 and IMC <= 29.99:
  print("       Sobrepeso \n¡Ánimo! Con un poco de cuidados y llegas a la meta de estar en tu peso ideal.")
elif IMC >= 30.0 and IMC <= 34.99:
  print("       Obesidad Leve \nEs importante cambiar algunos habitos.")
elif IMC >= 35.0 and IMC <= 39.99:
  print("       Obesidad Media \nSe le recomienda ver a los especialistas de la salud")
elif IMC >= 40.0:
  print("       Obesidad Mórbida \nAcerquece a los especialistas de la sulud, se encuentra en riesgo")
print ("*" * 60) 