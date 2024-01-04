def pridet_daikta(spintele, daiktas, kiekis): ### funkcija: prideti_daikta, kintamieji: spintele(kur viskas yra), daiktas (str), kiekis (int)
    if daiktas in spintele: ### jeigu daiktas yra spinteleje, tada
        spintele[daiktas] += kiekis ### pridedam kieki
        print(f"{daiktas} buvo pridėtas prie spintelės.")
    else:
        spintele[daiktas] = kiekis ### kiekis keiciasi tik paminetam daiktui, lieka toks pats kitiems
    return spintele ### grazinam funkcija tolimesniem veiksmam

def isimti_daikta(spintele, daiktas, kiekis):
    if daiktas in spintele:
        if spintele[daiktas] >= kiekis: ### patikrina ar tinkamas kiekis, nes neatimsi daikto, jei jo nera
            spintele[daiktas] -= kiekis ### atimam kieki
            print(f"'{daiktas}' išimtas iš spintelės.")
        else: ### neatimsi daikto, jei jo nera
            print(f"{daiktas} kiekis per mažas.")
    else: ### daikto nera spinteleje, atimtis neivyksta
        print(f"'{daiktas}' spintelėje nėra.")
    return spintele

def patikrinti_kieki(spintele, daiktas, reikiamas_kiekis):
    if daiktas in spintele:
        return spintele[daiktas] >= reikiamas_kiekis ### patikrina ar yra pakankamai daiktu konstrukcijai
    else:
        return False ### daiktu kiekio neuztenka

def spinteles_turinys(spintele, daiktas, kiekis):
    print("Spintelėje yra:")
    for daiktas, kiekis in spintele.items(): ### parodo visus daiktus ir ju kiekius
        print(f"{daiktas}: {kiekis}")

def daiktai_konstrukcijai(spintele, konstrukcija):
    
        #reikia suformuluot konstrukcijas ir patikrint ar yra pakankamai daiktu, kad jas sukonstruot