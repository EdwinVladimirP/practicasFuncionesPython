"""def puntuacion(alumno):
    return sum(alumno) / len(alumno)

nombre = input("ingresa tu nombre: ")
print(f"Hola {nombre}, sigue los pasos: ")
alumno = [int(input("Ingresa la primera nota: ")), int(input("Ingresa la segunda nota: ")), int(input("Ingresa la tercera nota: "))]
media = puntuacion(alumno)
print(f"¡{nombre}! La puntuación media de esta clase es: {media:.2}")
"""

"""def mostrar_linea(num, linea):
    print(nombre, ", el resultado de", num, "X", linea, "=>", num * linea)


nombre = input("hola, practiquemos las tablas, primero bríndame tu nombre: ")

mostrar_linea(int(input("tanto: ")), int(input("Por: ")))
"""

# Funciones con parámetros:

"""def saludar(nombre, saludo="Buenos días!!!"):  # ---->solo se le pasó 1 argumento.
    print(nombre + " " + saludo)

nombre = "Edwin"
saludar(nombre)"""

"""
def filtro(numeros, condicion):
    resultado = []
    for numero in numeros:
        if condicion(numero):
            resultado.append(numero)
    return resultado


def es_par(numero):
    return numero % 2 == 0


def es_positivo(numero):
    return numero > 0


numeros = [1, 2, 3, 4, 5, 6]
print(filtro(numeros, es_par))
print(filtro(numeros, es_positivo))
"""

"""Programa que toma las tres notas de un estudiante y diga la not final
del curso. Tenga en cuenta que la primera y segunda nota vale el 30% 
de la nota final. la tercera nota vale un 40%. """

"""
def calcularNota(nota1, nota2, nota3):
    return (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.4)

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

notaFinal = calcularNota(nota1, nota2, nota3)
print(f"La nota final del estudiante es: {round(notaFinal, 2)}")
"""

"""Programa que calcule el IVA de una compra, siendo el IVA del 19% sobre
el valor total de la compra"""

"""
def calcularIva(p):
    iva = p * 0.19
    return iva


precioCompra = float(input("Ingrese el valor de la compra: "))
iva = calcularIva(precioCompra)
print(f"El valor de la compra sin IVA es de: {precioCompra}")
print(f"El valor a pagar en total (IVA incluido) es de: {round(precioCompra + iva, 2)}")
"""
# https://www.youtube.com/watch?v=3HgXt-keJT4
# 07:00

"""Programa que calcule la tabl de multiplicar de cualquier número entero
dado por el usuario.
Debe calcular la tabla desde el 0 hasta el 12."""

"""def tablaDeMultiplicar(n1, n2):
    return str(n1) + " * " + str(n2) + " = " + str(n1*n2)
n = int(input("Ingresa un número entero: "))
for i in range(0, 13):
    print(tablaDeMultiplicar(n, i))"""

"""Programa que valide si una contraseña especificada por el usuario
es segura: 
--> Tiene más de 8 caracteres ----->len()
--> Tiene al menos una letra mayúscula -----> .isupper()
--> Tiene al menos un número -----> .isnumeric()    """
"""
def comprobarContrasenia(password):
    largo = False
    mayus = False
    numer = False
    if len(password) > 8:
        largo = True
    for i in range(len(password)):
        if password[i].isupper():
            mayus = True
        if password[i].isnumeric():
            numer = True

    if largo and mayus and numer:
        return True
    else:
        return False
password = input("Ingrese una contraseña: ")
verificacion = comprobarContrasenia(password)
if verificacion:
    print(f"La contraseña es segura. ")
else:
    print("La contraseña NO es segura. ")"""

"""Programa que valide si un número es primo"""

"""
def testPrimo(n):  # --->Un número es primo si es divisible entre él mismo y 1.
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:  # -------->Se va a buscar un dígito para una divición exacta.
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


# for i in range(-10, 101):
#   print(i, "", testPrimo(i))
n = int(input("Ingresa el número: "))
verificacion = testPrimo(n)
if verificacion:
    print(f"El número {n} es primo, Exito!")
else:
    print(f"Nej!, {n} no lo es. ")
"""

"""Programa que calcula el nuevo salario de un trabajador si obtuvo
un incremento del x %"""
"""
salarioActual = float(input("Ingrese el salario actual del trabajador: "))
incremento = float(input("Ingrese el porcentaje de incremento que tendrá el salario: "))


def calcularIncremento(salario, x):
    nuevoSalario = salario + (salario * (x / 100))
    return nuevoSalario


nuevoSalario = calcularIncremento(salarioActual, incremento)
print(f"El nuevo salario del trabajador es de {nuevoSalario}")
"""

"""Programa que pida dos números al usuario y una operación matemática a " \
Las operaciones son: 
->Suma
->Resta
->Multiplicación
->Divición
->Exponenciación (el primero es la base y el segundo el exponente)
->Radicación (el primero es el radicando y el segundo es el índice"""
"""
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. Divición")
print("6. Exponenciación")
print("7. Radicación")
opc = int(input("Ingresa la opción que deseas: "))


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


def exponenciacion(a, b):
    return a ** b


def radicacion(a, b):
    return a ** (1 / b)  # ----->Raíz cuadrada de 9 (9 es el radicando, 2 es el índice) 9 ** (1 / b)


if opc == 1:
    print(f"{n1} + {n2} = {(suma(n1, n2))}")
elif opc == 2:
    print(f"{n1} - {n2} = {(resta(n1, n2))}")
elif opc == 3:
    print(f"{n1} x {n2} = {(multiplicacion(n1, n2))}")
elif opc == 4:
    print(f"{n1} / {n2} = {(division(n1, n2))}")
elif opc == 5:
    print(f"{n1} ^ {n2} = {(exponenciacion(n1, n2))}")
elif opc == 6:
    print(f"{n1} ^ 1 / {n2} = {round((radicacion(n1, n2)), 3)}")
else:
    print("Ingrese un dato válido.")
"""

"""Programa que convierta una unidad en días, horas, minutos y segundos a segundos"""

"""
def calcularSegundos(d, h, m, s):
    segundosTotales = 0
    segundosTotales += s  # ----> el símbolo += se agrega el valor de la izquierda a la variable de la derecha.
    segundosTotales += m * 60
    segundosTotales += h * 60 * 60
    segundosTotales += d * 24 * 60 * 60
    return segundosTotales


d = int(input("Ingresa la cantidad de días: "))
h = int(input("Ingresa la cantidad de horas: "))
m = int(input("Ingresa la cantidad de minutos: "))
s = int(input("Ingresa la cantidad de segundos: "))
segundosTotales = calcularSegundos(d, h, m, s)
print(f"La cantidad de segundos en el tiempo ingresado es de : {segundosTotales}")
"""
# https://www.youtube.com/watch?v=3HgXt-keJT4&t=422s        46:36
"""Programa que calcula el índice de masa corporal(IMC) de una persona dado
su peso y estatura. Luego, idicar su nivel de peso así:
-------------------------------------------
    IMC                 CLASIFICACIÓN
-------------------------------------------
    <18.5       -> Bajo peso
18.5 -- 24.9    -> Normal
25.0 -- 29.9    -> Sobrepeso
30.0 -- 34.9    -> Obesidad I
35.0 -- 39.9    -> Obesidad II
40.0 -- 49.9    -> Obesidad III
    >50.0       -> Obesidad IV

IMC = peso / (estatura * estatura)  """

"""
def calcularIMC(p, a):
    return p / (a * a)


def nivelDePeso(IMC):
    if IMC < 18.5:
        return "Bajo peso"
    elif 18.5 <= IMC <= 24.9:
        return "Normal"
    elif 25.0 <= IMC <= 29.9:
        return "Sobrepeso"
    elif 30.0 <= IMC <= 34.9:
        return "Obesidad I"
    elif 35.0 <= IMC <= 39.9:
        return "Obesidad II"
    elif 40.0 <= IMC <= 49.9:
        return "Obesidad III"
    elif IMC >= 50.0:
        return "Obesidad IV"


peso = float(input("Ingresa el peso (kg): "))
altura = float(input("Ingresa la altura (m): "))
print("Su nivel de peso es: ", nivelDePeso(calcularIMC(peso, altura)))
"""

"""Comprobar si una palabra o frase es palíndroma. 
ej: 
-> Reconocer
-> Anna
-> Ojo rojo
-> La ruta nos aportó otro paso natural

Tener en cuenta que no se tienen en cuenta ni los espacios ni las mayúsculas ni las tíldes"""

palabra = input("Ingresa una palabra o una frase: ")
print(f"Palabra o frase ingresada: {palabra}")


def esPalindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")

    a = 0
    b = len(palabra) - 1

    for i in range(0, len(palabra)):
        if palabra[a] == palabra[b]:
            a += 1
            b -= 1
        else:
            return False
    return True


if esPalindromo(palabra):
    print("La palabra o frase ingresada es un palíndromo")
else:
    print("La palabra o frase ingresada no es un palíndromo")









