from datetime import datetime

fecha_actual = datetime.now()
hora = fecha_actual.strftime("%H")
print("Tiempo del sistema =", hora)
hora = int(hora)

try:
    if hora >= 7:
        print("Tu jornada laboral ha terminado")
    elif hora < 7:
        print(f"Te falta {7 - hora} hora para que termine tu turno.")
    else:
        print("FIN del programa")
except:
    print("El programa ha fallado!!")