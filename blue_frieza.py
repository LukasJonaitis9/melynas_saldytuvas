### Pridedi produktą

def prideti_produkta(saldytuvas, produktas, kiekis):
    if produktas in saldytuvas:
        saldytuvas[produktas] += kiekis
    else:
        saldytuvas[produktas] = kiekis
    return saldytuvas

### Išimti produktą
        
def isimti_produkta(saldytuvas, produktas, kiekis):
    if produktas in saldytuvas:
        if saldytuvas[produktas] >= kiekis:
            saldytuvas[produktas] -= kiekis
        else:
            print(f"Kieko nepakanka: {produktas}")
    else:
        print(f"Produktas nerastas: {produktas}")
    return saldytuvas

### Patikrinti produktų kiekį šaldytuve
        
def patikrinti_kieki(saldytuvas, produktas, reikalingas_kiekis):
    if produktas in saldytuvas:
        return saldytuvas[produktas] >= reikalingas_kiekis
    else:
        return False

### Spausdinti šaldytuvo turinį
    
def spausdinti_saldytuva(saldytuvas):
    print("Šaldytuve yra: ")
    for produktas, kiekis in saldytuvas.items():
        print(f"{produktas}: {kiekis}")

### Patikrinti ar yra pakankamai produktų receptui
        
def patikrinti_recepta(saldytuvas, receptas):
    trukstami_produktai = {}

    for produktas, reikalingas_kiekis in receptas.items():
        if produktas in saldytuvas:
            trukstantis_kiekis = reikalingas_kiekis - saldytuvas[produktas]
            if trukstantis_kiekis > 0:
                trukstami_produktai[produktas] = trukstantis_kiekis
        else:
            trukstami_produktai[produktas] = reikalingas_kiekis

    if trukstami_produktai:
        print("Trūksta šių produktų: ")
        for produktas, trukstantis_kiekis in trukstami_produktai.items():
            print(f"{produktas}: {trukstantis_kiekis}")
    else:
        print("Receptas išeina!")

### Šaldytuvo sąrašas
        
saldytuvas = {}

### Receptas

receptas = {"Suris": 0.5, "Pomidoras": 2, "Duona": 0.4}

while True:
    print('===[ Šaldytuvas ]===')
    print('0: Išeiti')
    print('1: Pridėti produktą')
    print('2: Išimti produktą')
    print('3: Patikrinti kiekį šaldytuve')
    print('4: Patikrinti receptą')
    print('5: Išspausdinti šaldytuvo turinį')
    pasirinkimas = input('Pasirinkimas: ')
    if pasirinkimas.startswith('0'):
        break
    elif pasirinkimas.startswith('1'):
        produktas = input('Produktas: ')
        kiekis = float(input('Kiekis: '))
        saldytuvas = prideti_produkta(saldytuvas, produktas, kiekis)
    elif pasirinkimas.startswith('2'):
        produktas = input('Produktas: ')
        kiekis = float(input('Kiekis: '))
        saldytuvas = isimti_produkta(saldytuvas, produktas, kiekis)
    elif pasirinkimas.startswith('3'):
        produktas = input('Produktas: ')
        reikalingas_kiekis = float(input("Patikrinkite kiekį: "))
        if patikrinti_kieki(saldytuvas, produktas, reikalingas_kiekis):
            print(f"{produktas} yra pakankamai.")
        else:
            print(f"Trūksta {produktas} šaldytuve")
    elif pasirinkimas.startswith('4'):
        patikrinti_recepta(saldytuvas, receptas)
    elif pasirinkimas.startswith('5'):
        spausdinti_saldytuva(saldytuvas)