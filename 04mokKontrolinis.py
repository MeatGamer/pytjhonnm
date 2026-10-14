taskai = [78, 45, 92, 61, 35, 88, 100, 54, 67, 29, 73, 85]
def vidurkis(taskai):
    return sum(taskai) / len(taskai)
def kiekViršVidurkio(taskai):
    kiek = 0
    vid = vidurkis(taskai)
    for taskas in taskai:
        if taskas > vid:
            kiek += 1
    return kiek
did = max(taskai)
maz = min(taskai)
print(f"Didziausias tasku skaicius: {did}")
print(f"Maziausias tasku skaicius: {maz}")
vid = vidurkis(taskai)
print(f"Visu mokiniu tasku vidurkis: {vid:.2f}")
kiek = 0
for taskas in taskai:
    if taskas >= 50:
        kiek += 1
print(f"Mokiniu, surinkusiu ne maziau kaip 50 tasku: {kiek}")
naujas = []
for taskas in taskai:
    if taskas >= 80:
        naujas.append(taskas)
print(f"Mokiniai, surinke 80 ir daugiau tasku: {naujas}")
kiek = kiekViršVidurkio(taskai)
print(f"Mokiniu, surinkusiu daugiau uz vidurki: {kiek}")