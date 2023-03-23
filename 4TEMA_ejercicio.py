import random

###### 1er PARTE ######

numero = random.randint(-5, 5)


def condicional(parametro):
    if parametro <= 0:
        return f"►El numero {parametro} es Negativo\n"
    elif parametro > 0:
        return f"►El numero {parametro} es Positivo\n"
    else:
        return "►Numero incorrecto, vuelve a intentar!!\n"


print(condicional(numero))

###### 2da PARTE ######


def incremento():
    num_uno = 0

    while num_uno < 3:
        num_uno += 1
        print(num_uno)


incremento()

###### 3er PARTE ######

"""
PYTHON NO TIENE EL BUCLE DO WHILE
"""

###### 4ta PARTE ######


def bucleFor():

    # inicio = 0

    for inicio in range(0, 3):
        inicio += 1
        print(inicio)


bucleFor()
###### 5ta PARTE ######


def switch(estacion):

    match estacion:
        case "primavera":
            print("Es primavera")
        case "verano":
            print("Es verano")
        case "otono":
            print("Es otono")
        case "invierno":
            print("Es invierno")
        case _:
            print("No es ninguna estacion del anio!!")


switch("primavera")
###### 6ta PARTE ######
