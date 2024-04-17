"""
Recomendaciones para hacer y entregar la tarea:

    0. HACER MINIMO 5 EJERCICIOS
    1. Si vas a usar chatgpt no preguntes la pregunta de frente, asi nada tiene sentido, mejor hazlo sin chatgpt
    2. Guarda por archivo 1 o máximo 2 (la continiuación) ejercicio(s)
    3. Entrega en un solo 1 Archivo.zip 
    4. Trata de comentar la máyoria del codigo que hagas

Info ps:
    - Los 2 bonuses resueltos da 1 pregunta menos para el exámen final
    - El exámen final se hara sin chatgpt, google o algun tipo de ayuda con el internet, se permitira un cheatsheet pero solo puede ser la dada por el profe

"""
import datetime

"""
1. Ingresa la edad de alguien e imprime su nombre pero da un error si no se ingresa un número - (Dificultad 1 de 5).
"""
# edad = input("Edad: ")

# if edad.isdigit():
#     print(edad)
# else:
#     print("Eso no es una edad perro(a) :v")

"""
2. Amplia el primer ejercicio y si la edad de la persona es mayor a 50, obten el apellido de la persona y luega trata de adivinar el año en que nació. Luego imprime su apellido y el año de nacimiento restando su edad con el año actual, el print debe ser solo de 1 linea. Investigue en la internet sobre como importar e usar algunas funciones básicas que tendra que importar del modulo: datetime
Importante: Compruebe el ejercicio cambiando manualmente el año actual de su computadora
(Dificultad 2 de 5)
"""
# edad = input("Edad: ")

# if edad.isdigit():
#     print(edad)
# if int(edad) > 50:
#     apellido = input("Apellido: ")
#     current_year = datetime.datetime.now().year
#     print(f"El señor {apellido} nació probablemente en: {current_year}")
# else:
#     print("Eso no es una edad perro(a) :v")

"""
3. Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula. En el caso del número, se deben aceptar números enteros y decimales  - (Dificultad 2 de 5).
Ejemplo:
Ingrese caracter: 9
Es numero.
Ingrese caracter: A
Es letra mayúscula.
Ingrese caracter: #
No es letra ni número.
"""
# caracter = input("Ingrese caracter: ")

# if caracter.isalpha():
#     if caracter.isupper():
#         print("Es letra mayúscula.")
#     else:
#         print("Es letra minúscula.")
# elif "." in caracter or caracter.isdigit():
#     print("Es número.")
# else:
#     print("No es letra ni número.")

"""
4. Haga una calculadora que solo haga lo siguiente - (Dificultad 2 de 5): 
- Programa la potenciación
- Programa la suma y resta
La elección del simbolo para las operaciones es de elección libre pero se debe dar a conocer cuales son.
Se debe saltar de linea (↵ ) como en el ejemplo usando solo 1 linea de codigo, osea no más de 2 print().
Ejemplo:
Que tipo de operación?                                      ↵ (esto no es imprime btw)
Opciones: + (Suma), - (Resta), ^ (Potenciación): +
1° Nr: 5
2° Nr: 5
Resultado: 10
"""
# operacion = input("Que tipo de operación? \n Opciones: + (Suma), - (Resta), ^ (Potenciación): ")

# num1 = float(input("1° Nr: "))
# num2 = float(input("2° Nr: "))

# if operacion == "+":
#     print(num1+num2)
# elif operacion == "-":
#     print(num1-num2)
# elif operacion == "^":
#     print(num1**num2)
# else:
#     print("Error, pon una operacion correcta ps")

"""
5. Amplia la calculadora - (Dificultad 4 de 5): 
- Programa la conversión de número de base 10 a base 2 (binario).
- Despues de que una operación haya sido realizada, pregunta si se quiere realizar una operación más? Si se repite, hacer la operación sin salir del programa o tener que hacer correr al programa de nuevo. (No darle al boton de play más de 1 vez)
- No se aceptan decimales para convertir a números binarios
Se calificara la calidad de la calculadora probandolada con estos números:
Tip secreto: bin(), is_integer(), la salida del binario en python inicia con 0b, break, True, False, isdigit()
Ejemplo:
Que tipo de operación?
Opciones: + (Suma), - (Resta), ^ (Potenciación), ~ (Número de Base 10 a Base 2): ~
Nr. de Base 10: 15
Binario: 1111
Realizar una operación más? Si/No: Si
Que tipo de operación?
Opciones: + (Suma), - (Resta), ^ (Potenciación), ~ (Número de Base 10 a Base 2): 
... etc
"""

# condicion = True --- en python tambien puede ser asi
# while True: # normal: condicion == True
#     operacion = input("Que tipo de operación? \nOpciones: + (Suma), - (Resta), ^ (Potenciación), ~ (Número de Base 10 a Base 2): ")
#     num1 = input("1° Nr: ")
#     if "." in num1 or num1.isdigit():
#         if operacion == "+":
#             num2 = input("2° Nr: ")
#             print(float(num1)+float(num2))
#         elif operacion == "-":
#             num2 = input("2° Nr: ")
#             print(float(num1)-float(num2))
#         elif operacion == "^":
#             num2 = input("2° Nr: ")
#             print(float(num1)**float(num2))
#         elif operacion == "~":
#             if(int(num1).is_integer()):
#                 print("Binario:", bin(int(num1)))
#             else:
#                 print("No se aceptan números decimales")
#         else:
#             print("Error, pon una operacion correcta ps\n Opciones: + (Suma), - (Resta), ^ (Potenciación)")
#     else:
#         print("Ponga un Número como indicado.")
#     decision = input("Realizar una operación más? Si/No: ")

#     if decision.lower() == "no":
#         break
#     else:
#         print("Sera pues otra")

# print("Ni fue tan complicado xd")

"""
6. Escriba un programa que dibuje este triángulo con 2 tipos distintos de bucles (tiene máximo 5 astericos) - (Dificultad 1 de 5):
*
**
***
****
*****
"""
# contador = 0
# while contador <= 5:
#     print("*" * contador)
#     contador += 1 # <= contador = contador + 1 

# for i in range(1, 6):
#     print('*' * i)


"""
Bonus: 
1. Nivel pollo: Usa un decriptador en linea del enigma maschine, literal en google hay varios, y decripta este mensaje: (Hecho con Enigma M3)
ntdfx xysqr mdcef komhy fvnpv zsxhd ghvcs scdnm syypd gmzyw upqxb hdmiw jrjak akxto nnkjs fywtd eymhq yovsb doowh vcezj llsca cklzz inhel yvovj ksncj cxbbl tzzk

2. Escriba un programa que permita determinar el número mayor perteneciente a un conjunto de n números, donde tanto el valor de n como el de los números deben ser ingresados por el usuario. Puntos extra si le logra exactamente lo del ejemplo. Si no se logra tambien vale pero la cosa es que funcione algo.
Ejemplo:
Ingrese n: 4
Ingrese el número 1: 23
Ingrese el número 2: -34
Ingrese el número 3: 0
Ingrese el número 4: 1
El mayor es 23
"""
# n = int(input("Cuantos números?: "))
# mayor = 0 # creamos la variable para que tenga una referencia 

# for i in range(n):
#     num = float(input(f"Ingrese el número {i+1}: "))
    
#     # Si es el primer número ingresado, lo establecemos como el mayor
#     if mayor == 0:
#         mayor = num
#     # Si el número actual es mayor que el mayor registrado hasta ahora, lo actualizamos
#     elif num > mayor:
#         mayor = num

# print("El número mayor es:", mayor)