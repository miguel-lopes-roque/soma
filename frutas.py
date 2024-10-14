def comando_in():
        frutas = ["maçã", "abacate", "açaí", "pêra"]
    print("maçã" in frutas)
    print(not "cajá" in frutas)#mesmo que print("cajá" not in frutas)
    
    fruta_teste = "laranja"
    if (fruta_teste not in frutas):
        frutas.append(fruta_teste)
        print(frutas)