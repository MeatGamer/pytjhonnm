n = int(input("Iveskite lentynu skaiciu: "))

lentynos = []

for i in range(n):
    kiekis = int(input("Iveskite prekiu kieki: "))
    lentynos.append(kiekis)

print(f"Lentynu likuciai: {lentynos}")

suma = sum(lentynos)
vidurkis = suma / len(lentynos)
maz = min(lentynos)
did = max(lentynos)

print(f"Visu prekiu kiekis: {suma}")
print(f"Vidutinis prekiu kiekis: {vidurkis}")
print(f"Maziausias prekiu kiekis: {maz}")
print(f"Didziausias prekiu kiekis: {did}")

kiekMaz = lentynos.count(maz)

print(f"Lentynu su maziausiu kiekiu: {kiekMaz}")

siunta = int(input("Iveskite naujos siuntos dydi: "))

vieta = lentynos.index(maz)
lentynos[vieta] += siunta

print(f"Atnaujintos lentynos: {lentynos}")

kiekNuliniu = lentynos.count(0)

for i in range(kiekNuliniu):
    lentynos.remove(0)

print(f"Lentynos be tusciu lentynu: {lentynos}")

naujasVidurkis = sum(lentynos) / len(lentynos)

print(f"Naujas vidutinis prekiu kiekis: {naujasVidurkis}")