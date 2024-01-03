#def saldytuvo_turinys(saldytuve_yra):
saldytuve_yra = {'Duona': 1.6, 'Sūris': 0.5, 'Grietinė': 0.7, 'Sūrelis': 5, 'Sviestas': 0.32}

def prideti_produkta(saldytuve_yra, produktas, kiekis):
        saldytuve_yra[produktas, kiekis] = input("Ko ir kiek pridėsite?:")
        if produktas in saldytuve_yra:
            if saldytuve_yra[produktas] >= kiekis:
                saldytuve_yra[produktas] += kiekis
                print(f"{produktas} pridėtas prie šaldytuvo. Naujas kiekis: {saldytuve_yra[produktas]}")
            else:
                saldytuve_yra[produktas] = kiekis

def atimti_produkta(saldytuve_yra, produktas, kiekis):
        saldytuve_yra[produktas, kiekis] = input("Ko ir kiek išimsite?:")
        if produktas in saldytuve_yra:
            if saldytuve_yra[produktas] >= kiekis:
                saldytuve_yra[produktas] -= kiekis
                print(f"{produktas} išimtas iš šaldytuvo. Naujas kiekis: {saldytuve_yra[produktas]}")
            else:
                print(f"Produkto {produktas} kiekis nepakankamas.")
        else:
            print(f"Produkto {produktas} nėra.\nLaikas eiti į parduotuvę.")

for produktas, kiekis in saldytuve_yra.items():
    print(f'{produktas}: {kiekis} vnt.')
    #def kiekio_patikrinimas(saldytuve_yra, produktas, kiekis):