import itertools


mesafeler = {
    ('a', 'b'): 10,
    ('a', 'c'): 15,
    ('a', 'd'): 20,
    ('b', 'c'): 35,
    ('b', 'd'): 25,
    ('c', 'd'): 30,
}


sehirler = set(sehir for cift in mesafeler.keys() for sehir in cift)

def tsp(mesafeler, sehirler):
    min_mesafe = float('inf')
    min_rota = None


    for sıralama in itertools.permutations(sehirler):
        toplam_mesafe = 0
        rota = list(sıralama) + [sıralama[0]]  

        for i in range(len(rota) - 1):
            sehir1, sehir2 = rota[i], rota[i + 1]
            toplam_mesafe += mesafeler.get((sehir1, sehir2), mesafeler.get((sehir2, sehir1), 0))

        if toplam_mesafe < min_mesafe:
            min_mesafe = toplam_mesafe
            min_rota = rota

    return min_rota, min_mesafe

rota, toplam_mesafe = tsp(mesafeler, sehirler)
print("En Kısa Rota:", " --> ".join(rota))
print("Toplam Mesafe:", toplam_mesafe)
