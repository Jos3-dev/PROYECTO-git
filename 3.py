

class problema:
    def decremento(limite):
        start = limite
        end = 0
        if start >= end:
            while start > end:
                print(f"►  {start}")
                start -= 1

    def incremento(limite):
        inicio = 0
        if inicio < limite:
            while inicio < limite:
                print(f"Posicion: {inicio}")
                inicio += 1



problema.decremento(100)