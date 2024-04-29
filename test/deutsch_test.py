import random


german_to_polish = {
    "das Brot": "chleb",
    "das Vollkornbrot": "wieloziarnisty chleb",
    "das Roggenbrot": "żytny chleb",
    "das Weizenbrot": "przeniczny chleb",
    "das Brótchen": "bułka",
    "die Semmel": "bułka",
    "das Hórnchen": "rogalik",
    "die Butter": "masło",
    "der Ka:se": "ser żółty",
    "der Schmelzka:se": "ser pleśniowy",
    "der Quark": "biały serek",
    "die Wurst": "kiełbasa",
    "der Schinken": "szynka",
    "die Marmelade": "marmelada",
    "das Jam": "dżem",
    "der Honig": "miód",
    "das Ei": "jajko",
    "der Fisch": "ryba",
    "der Lechs": "łosoś",
    "die Makrele": "makrela",
    "der Thunkfisch": "tuńczyk",
    "der Joghurt": "jogurt",
    "die Margarine": "margaryna",
    "die Milch": "mleko",
    "das Mu:sli": "musli",
    "der Reis": "ryż",
    "das Mehl": "mąka",
    "der Zucker": "cukier",
    "der Tee": "herbata",
    "der Kra:utertee": "ziołowa herbata",
    "der Kaffee": "kawa",
    "die Nudeln": "makaron",
    "die Sahne": "śmietana",
    "die Pastete": "pasztet",
    "das Salz": "sól",
    "der Pfeffer": "pieprz",
    "der Senf": "musztarda",
    "der Ketschup": "ketchup",
    "der Zimt": "cynamon",
    "das O:l": "olej",
    "der Essig": "ocet",
    "der Saft": "sok",
    "die Hefe": "drożdże",
    "die Mayo": "majonez",
    "der Schokoriegel": "batonik czekoladowy",
    "das Halwa": "halwa",
    "die Bonbons": "cukierki",
    "die Pralinen": "praliny",
    "die Schokolade": "czekolada",
    "die Lutscher": "lizak",
    "die Gummiba:rchen": "żelki",
    "die Salzstangen": "paluszki solone",
    "der Kuchen": "ciasto",
    "die Torte": "tort",
    "die Waffeln": "gofry",
    "der Pfannkuchen": "placki",
    "die Tomate": "pomidor",
    "die Gurke": "ogórek",
    "der Paprika": "papryka",
    "der Salat": "sałata",
    "die Kartoffeln": "ziemniaki",
    "die Bohnen": "fasola",
    "die Erbsen": "groch",
    "die Spargel": "szparagi",
    "die Champignons": "pieczarki",
    "der Pilz": "grzyb",
    "der Spinat": "szpinak",
    "die Mo:hre": "marchew",
    "die Karotte": "marchew",
    "der Porree": "por",
    "die Zweibel": "cebula",
    "der Kohl": "kapusta",
    "der Blaumenkohl": "kalafior",
    "der Mais": "kukurydza",
    "der Dill": "koperek",
    "der/die Sellerie": "seler",
    "der Knoblauch": "czosnek",
    "die Rote Ru:be": "burak",
    "die Brokkoli": "brokuł",
    "der Meerretich": "chrzan",
    "das Sauerkraut": "kiszona kapusta",
    "das Petersiliengru:n": "natka pietruszki",
    "der Ku:rbis": "dynia",
    "der Ananas": "ananas",
    "der Apfel": "jabłko",
    "die Aprikose": "morela",
    "die Banana": "banan",
    "die Apfelsine": "pomarańcza",
    "die Orange": "pomarańcza",
    "die Birne": "gruszka",
    "die Feige": "figa",
    "die Nektarine": "nektarynka",
    "die Mandarine": "mandarynka",
    "die Mandel": "migdały",
    "die Blaubeeren": "borówki",
    "die Himbeeren": "maliny",
    "die Schwarze Johanisbeeren": "czarna porzeczka",
    "die Rote Johanisbeeren": "czerwona porzeczka",
    "die Erdnu:sse": "orzechy ziemne",
    "die Pistazien": "pistacje",
    "die Walnuß": "orzech włoski",
    "die Kiwi": "kiwi",
    "der Pfirsich": "brzoskwinia",
    "die Grapefruit": "grejpfrut",
    "die Kirsche": "wiśnia",
    "die Sußkirsche": "czereśnia",
    "die Honigmelone": "melon miodowy",
    "die Wassermelone": "arbuz",
    "die Zitrone": "cytryna",
}


if __name__ == "__main__":
    corr_answers = []
    incorr_answers = []

    keylst = list(german_to_polish.keys())

    for _ in range(20):
        question = keylst.pop(random.randint(0, len(keylst) - 1))
        available_keys = list(range(len(keylst)))
        answer = german_to_polish[question]

        answers = [answer]
        for _ in range(3):
            answers.append(
                german_to_polish.get(
                    keylst[
                        available_keys.pop(random.randint(0, len(available_keys) - 1))
                    ]
                )
            )

        random.shuffle(answers)
        print("\n", question)
        print("\n")
        print("answers :", answers)
        ind = input("\n1,2,3,4...: ")
        while ind == "" or int(ind) < 1 or int(ind) > 4:
            print("index out of range")
            print("\n", answers)
            ind = input("\n1,2,3,4...")

        choice = answers.pop(int(ind) - 1)
        if answer == choice:
            corr_answers.append(question)
        else:
            incorr_answers.append(question)

    print("\ncorrect answers:", len(corr_answers))
    print("\n", corr_answers)
    if len(corr_answers) != 0:
        print("\nincorrect answers:", len(incorr_answers))
    if len(incorr_answers) != 0:
        print("\n", incorr_answers)
