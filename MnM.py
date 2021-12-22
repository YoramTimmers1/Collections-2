Kleuren = ["oranje","groen","bruin","blauw"]

def MnM(Kleuren):
    print("Wil je nog een extra kleur toevoegen dit zijn de kleuren die je al hebt")
    print(Kleuren)
    extrakleur  = input("voeg een extra kleur toe : ")
    
    Kleuren.append(extrakleur)
    HoeveelMnMkleuren = input("hoeveel M&M's wil je :")   
    import random
    for i in range(int(HoeveelMnMkleuren)):
        print(random.choice(Kleuren))
MnM(Kleuren)