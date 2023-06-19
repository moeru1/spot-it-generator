#retorna el intervalo cerrado [k, n]
def range_in(k,n):
    return range(k, n+1)

#retorna el simbolo s correspondiente a
#la columna col en un mazo de orden n, 0 <= s <= n-2
def columna_sym(s, col, n):
    return (n-1) * col  + 1 + s

#concatena toda las sublistas de L y las guarda en una nueva
#lista L'
def flatten(L):
    flat = []
    for sublista in L:
        for x in sublista:
            flat.append(x)

    return flat

# retorna una lista de lista que representan las cartas
# del mazo con cartas de tamano n
def genera_mazo(n):
    if n <= 1:
        return []

    renglon = [[]]

    #renglon inicial
    offset = 0
    for carta_ind in range_in(1,n):
        carta = [0]
        for sym in range_in(1,n-1):
            carta.append(offset + sym)

        #print("carta ", carta_ind , " ",carta)
        renglon[0].append(carta)
        offset = offset + (n-1)

    for renglon_ind in range_in(1, n-1):
#        print("in")
        renglon.append([])
        #i = carta i del renglon renglon_ind
        for i in range_in(0, n - 2):
            carta_i = [renglon_ind]
            # la columna fija siempre tiene la misma estructura
            sym = columna_sym(i, 1, n)
            carta_i.append(sym)

            for columna in range_in(2, n-1):
                #elemento del cuadrado latino de tamano n-1 x n-1
                sym_en_columna = ( (columna - 1) * (renglon_ind - 1) + i) % (n-1)
                sym = columna_sym(sym_en_columna, columna, n)
                carta_i.append(sym)

            renglon[renglon_ind].append(carta_i)

    juego_dobble = flatten(renglon)
    return juego_dobble


def imprimir_juego(C):
    for C_i in C:
        for s in C_i:
            print("{:4}".format(s),end=" ")
        print("")

# verifica si n es primo o no usando fuerza bruta
def prueba_primacidad(n):
    i = 2
    while True:
        if i*i > n:
            return True
        elif n % i == 0:
            return False
        i = i + 1

# verifica si las cartas de tamano n forman un juego Dobble
# suponiendo que no hay un simbolo en comun para todas las cartas
def test_juego(C, n):
    for i in range(0,len(C)):
        for j in range(i + 1, len(C)):
            iguales = len(set(C[i]) & set(C[j]))
            #si su interseccion es mayor a 1
            if iguales != 1:
                return False
    return True


