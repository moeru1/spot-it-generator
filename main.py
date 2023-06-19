from spot_it_lib import *

if __name__ == "__main__":
    n = input("Size of the cards: ")
    n = int(n)
    if not prueba_primacidad(n-1):
        print("Deck cannot be generated (n-1 is not a prime number)")
    else:
        juego = genera_mazo(n)
        test = test_juego(juego, n)
        if not test:
            print("The deck couldn't be generated correctly")
        else:
            print("The deck is below:")
            imprimir_juego(juego)
