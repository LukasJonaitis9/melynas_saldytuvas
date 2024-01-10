class Saldytuvas:
    def __init__(self):
        self.maisto_grupes = {
            'daržovės': {},
            'mėsa': {},
            'pieno_produktai': {},
            'vaisiai': {},
            'kepiniai': {}
        }

    def prideti_produkta(self, grupes_pavadinimas, produktas, kiekis, matavimo_vienetas):
        if grupes_pavadinimas in self.maisto_grupes:
            grupes = self.maisto_grupes[grupes_pavadinimas]
            if produktas in grupes:
                grupes[produktas]['kiekis'] += kiekis
            else:
                grupes[produktas] = {'kiekis': kiekis, 'matavimo_vienetas': matavimo_vienetas}
            print(f"Pridėtas produktas: {produktas}, Kiekis: {kiekis} {matavimo_vienetas}, Grupė: {grupes_pavadinimas}")
        else:
            print(f"Netinkama maisto grupė: {grupes_pavadinimas}")

    def isimti_produkta(self, grupes_pavadinimas, produktas, kiekis):
        if grupes_pavadinimas in self.maisto_grupes:
            grupes = self.maisto_grupes[grupes_pavadinimas]
            if produktas in grupes:
                if grupes[produktas]['kiekis'] >= kiekis:
                    grupes[produktas]['kiekis'] -= kiekis
                    print(f"Išimtas produktas: {produktas}, Kiekis: {kiekis} {grupes[produktas]['matavimo_vienetas']}, Grupė: {grupes_pavadinimas}")
                else:
                    print(f"Kieko nepakanka: {produktas}")
            else:
                print(f"Produktas nerastas: {produktas}")
        else:
            print(f"Netinkama maisto grupė: {grupes_pavadinimas}")

    def tikrinti_produktus(self):
        print("\nŠaldytuvo turinys:")
        for grupes_pavadinimas, grupes in self.maisto_grupes.items():
            print(f"\n{grupes_pavadinimas.capitalize()}:")
            for produktas, info in grupes.items():
                print(f"  {produktas}: {info['kiekis']} {info['matavimo_vienetas']}")

    def tikrinti_pakanka_produktu(self, recepto_produktai):
        pakanka = True
        for grupes_pavadinimas, produktai in recepto_produktai.items():
            for produktas, kiekis in produktai.items():
                if grupes_pavadinimas in self.maisto_grupes:
                    grupes = self.maisto_grupes[grupes_pavadinimas]
                    if produktas in grupes and grupes[produktas]['kiekis'] < kiekis:
                        pakanka = False
                        print(f"Trūksta produkto: {produktas}, Kiekis reikalingas: {kiekis} {grupes[produktas]['matavimo_vienetas']}")
                else:
                    pakanka = False
                    print(f"Netinkama maisto grupė: {grupes_pavadinimas}")
        return pakanka


class MaistoProduktas:
    def __init__(self, pavadinimas):
        self.pavadinimas = pavadinimas


def main():
    saldytuvas = Saldytuvas()

    while True:
        print("\nPasirinkite veiksmą:")
        print("1: Tikrinti produkto kiekį")
        print("2: Pridėti produktą")
        print("3: Išimti produktą")
        print("4: Tikrinti ar pakanka produktų receptui")
        print("0: Išeiti")

        choice = input("Jūsų pasirinkimas: ")

        if choice == "1":
            saldytuvas.tikrinti_produktus()

        elif choice == "2":
            grupes_pavadinimas = input("Įveskite maisto grupę: ")
            produktas = input("Įveskite produkto pavadinimą: ")
            kiekis = float(input("Įveskite kiekį: "))
            matavimo_vienetas = input("Įveskite matavimo vienetą (kg, vnt., l, etc.): ")
            saldytuvas.prideti_produkta(grupes_pavadinimas, produktas, kiekis, matavimo_vienetas)

        elif choice == "3":
            grupes_pavadinimas = input("Įveskite maisto grupę: ")
            produktas = input("Įveskite produkto pavadinimą: ")
            kiekis = float(input("Įveskite kiekį: "))
            saldytuvas.isimti_produkta(grupes_pavadinimas, produktas, kiekis)

        elif choice == "4":
            recepto_produktai = {
                'daržovės': {'Pomidoras': 2, 'Agurkas': 1},
                'mėsa': {'Kiauliena': 1},
                'vaisiai': {'Obuolys': 3}
            }
            if saldytuvas.tikrinti_pakanka_produktu(recepto_produktai):
                print("Pakanka produktų receptui!")
            else:
                print("Trūksta produktų receptui.")

        elif choice == "0":
            print("Programa baigia darbą.")
            break

        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")


if __name__ == "__main__":
    main()
