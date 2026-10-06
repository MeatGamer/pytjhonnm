n = int(input("Iveskite dalyviu skaiciu: "))

rezultatai = []

for i in range(n):
    rezultatas = int(input("Iveskite rezultata: "))
    rezultatai.append(rezultatas)

print(f"Rezultatai: {rezultatai}")

did = max(rezultatai)
maz = min(rezultatai)
suma = sum(rezultatai)
vidurkis = suma / len(rezultatai)

print(f"Didziausias rezultatas: {did}")
print(f"Maziausias rezultatas: {maz}")
print(f"Visu tasku suma: {suma}")
print(f"Rezultatu vidurkis: {vidurkis}")

kiekDaugiau = 0

for rezultatas in rezultatai:
    if rezultatas > vidurkis:
        kiekDaugiau += 1

print(f"Daugiau uz vidurki surinko: {kiekDaugiau}")

kiekDid = rezultatai.count(did)

print(f"Geriausia rezultata pasieke: {kiekDid}")

for i in range(kiekDid):
    rezultatai.remove(did)

print(f"Like rezultatai: {rezultatai}")

antras = max(rezultatai)

print(f"Antras geriausias rezultatas: {antras}")