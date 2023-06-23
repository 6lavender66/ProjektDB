def generuj_tomy():
    tomy = []
    autor = "Kentarō Miura"
    data_wydania = 0 #tutaj wprowadzałem daty ręcznie xD

    for n in range(34, 42):
        tytul = f"Berserk Tom {n}"

        tom = {
            "tytuł": tytul,
            "numer": n,
            "data wydania": data_wydania,
            "autor": autor
        }

        tomy.append(tom)

    return tomy

# Wyświetlanie wynikowych tomów
tomy_berserk = generuj_tomy()
for tom in tomy_berserk:
    print("{")
    print('"tytuł":', '"' + tom["tytuł"] + '",')
    print('"numer":', tom["numer"],',')
    print('"data wydania":', tom["data wydania"], ',')
    print('"autor":', '"' + tom["autor"] +'",')
    print("},")
