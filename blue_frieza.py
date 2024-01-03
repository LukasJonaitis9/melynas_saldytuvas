### Pridedi produktą

def prideti_produkta(saldytuve, produktas, kiekis):
    if produktas in saldytuve:
        saldytuve[produktas] += kiekis
    else:
        saldytuve[produktas] = kiekis

### Išimti produktą
        
def isimti_produkta(saldytuve, produktas, kiekis):
    if produktas in saldytuve:
        if saldytuve[produktas] >= kiekis:
            saldytuve[produktas] -= kiekis
        else:
            print(f"Kieko nepakanka: {produktas}")
    else:
        print(f"Produktas nerastas: {produktas}")

### Patikrinti produktų kiekį šaldytuve
        
def patikrinti_kieki(saldytuve, produktas, reik_kiekis):
    if produktas in saldytuve:
        return saldytuve[produktas] >= reik_kiekis
    else:
        return False

### Spausdinti šaldytuvo turinį
    
def spausdinti_saldytuva(saldytuve):
    print("Šaldytuve yra: ")
    for produktas, kiekis in saldytuve.items():
        print(f"{produktas}: {kiekis}")

### Patikrinti ar yra pakankamai produktų receptui
        
def patikrinti_recepta(saldytuve, receptas):
    trukstami_produktai = {}

    for produktas, reik_kiekis in receptas.items():
        if produktas in saldytuve:
            trukstantis_kiekis = reik_kiekis - saldytuve[produktas]
            if trukstantis_kiekis > 0:
                trukstami_produktai[produktas] = trukstantis_kiekis
        else:
            trukstami_produktai[produktas] = reik_kiekis

    if trukstami_produktai:
        print("Trūksta šių produktų: ")
        for produktas, trukstantis_kiekis in trukstami_produktai.items():
            print(f"{produktas}: {trukstantis_kiekis}")
    else:
        print("Receptas išeina!")

### Šaldytuvo sąrašas
        
saldytuve = {}

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
        prideti_produkta(saldytuve, produktas, kiekis)
    elif pasirinkimas.startswith('2'):
        produktas = input('Produktas: ')
        kiekis = float(input('Kiekis: '))
        isimti_produkta(saldytuve, produktas, kiekis)
    elif pasirinkimas.startswith('3'):
        produktas = input('Produktas: ')
        reik_kiekis = float(input("Patikrinkite kiekį: "))
        if patikrinti_kieki(saldytuve, produktas, reik_kiekis):
            print(f"{produktas} yra pakankamai.")
        else:
            print(f"Trūksta {produktas} šaldytuve")
    elif pasirinkimas.startswith('4'):
        patikrinti_recepta(saldytuve, receptas)
    elif pasirinkimas.startswith('5'):
        spausdinti_saldytuva(saldytuve)