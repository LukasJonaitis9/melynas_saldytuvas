biudzetas = {}

def prideti_pajamas(paskirtis, suma):
    if paskirtis not in biudzetas:
        biudzetas[paskirtis] = 0
    biudzetas[paskirtis] += suma

def prideti_islaidas(paskirtis, suma):
    if paskirtis not in biudzetas:
        biudzetas[paskirtis] = 0
    biudzetas[paskirtis] -= suma

def spausdinti_zurnala():
    print("Pajamų/Išlaidų Žurnalas:")
    for paskirtis, suma in biudzetas.items():
        print(f"{paskirtis}: {suma}")

def skaiciuoti_balansa():
    balansas = sum(biudzetas.values())
    print(f"Biudžeto balansas: {balansas}")

while True:
    print('=-=-=Balansas=-=-=')
    print('1: Prideti pajamas')
    print('2: Islaidos')
    print('3: Balansas')