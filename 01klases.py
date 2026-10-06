n = int(input("Iveskite pazymiu skaiciu: "))

pazymiai = []

for i in range(n):
    pazymys = int(input("Iveskite pazymi: "))
    pazymiai.append(pazymys)

print(f"Pazymiai: {pazymiai}")

vidurkis = sum(pazymiai) / len(pazymiai)
print(f"Visu pazymiu vidurkis: {vidurkis}")

did = max(pazymiai)
maz = min(pazymiai)

print(f"Didziausas pazymys: {did}")
print(f"Maziausias pazymys: {maz}")

kiekDid = pazymiai.count(did)
kiekMaz = pazymiai.count(maz)

for i in range(kiekDid):
    pazymiai.remove(did)

for i in range(kiekMaz):
    pazymiai.remove(maz)

print(f"Like pazymiai: {pazymiai}")

naujasVid = sum(pazymiai) / len(pazymiai)

print(f"Naujas vidurkis: {naujasVid}")