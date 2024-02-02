lista = ["gato", "cachorro", "elefante", "camelo", "girafa", "tigre", "bicho preguiça", "papagaio", "baleia", "cobra",
           "macaco", "gorila", "urso", "rinoceronte", "camelo", "lagarto", "harpia", "pato", "coala", "tamandua"]
 
animais_ordenados = sorted(lista)
print([animal for animal in animais_ordenados])
 
with open("animais.csv", "w") as arquivo:
    for animal in animais_ordenados:
        arquivo.write(f"{animal}\n")