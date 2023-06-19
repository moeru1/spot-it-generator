from dobble import *

N = 2

for _ in range(1,N):
   # rnd = randint(1, N)
   # rnd_prime = next_prime(rnd)
    rnd_prime = 7
    print("rnd_prime ", rnd_prime)
    mazo = genera_mazo(rnd_prime + 1)
    dobble = IncidenceStructure(len(mazo), mazo)

    plano_proy = designs.projective_plane(rnd_prime)

    print(plano_proy.is_isomorphic(dobble))
