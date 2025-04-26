import pygame
import time
from colorama import init, Fore  # Aqui estamos importando corretamente o 'init' e o 'Fore'
init(autoreset=True)  # Isso inicializa o colorama para funcionar corretamente


# Inicia a música
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/alexa/Desktop/scriptpyt/dawnofchange.mp3")
pygame.mixer.music.play(-1)

# Cabeçalho do quiz
texto = "Seja bem-vindo ao Quiz de...!"
print(texto.center(80))

print("""
████████████████████████████████████████████████████████████████████████████
██╗░░██╗░█████╗░██████╗░██████╗░██╗░░░██╗  ██████╗░░█████╗░████████╗████████╗
██║░░██║██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝
███████║███████║██████╔╝██████╔╝░╚████╔╝░  ██████╔╝██║░░██║░░░██║░░░░░░██║░░░
██╔══██║██╔══██║██╔══██╗██╔══██╗░░╚██╔╝░░  ██╔═══╝░██║░░██║░░░██║░░░░░░██║░░░
██║░░██║██║░░██║██║░░██║██║░░██║░░░██║░░░  ██║░░░░░╚█████╔╝░░░██║░░░░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝░░░░░░╚════╝░░░░╚═╝░░░░░░╚═╝░░░
████████████████████████████████████████████████████████████████████████████
""")

# Começa com 0 acertos
acertos = 0

# Perguntas
print(Fore.YELLOW + "\n1) Qual é o nome completo do protagonista da saga?")
print("(a) Harry Weasley\n(b) Harry Black\n(c) Harry Potter\n(d) Harry Malfoy\n(e) Harry Lupin")
resposta1 = input("> ")

if resposta1.lower() == "c":
    print(Fore.GREEN + "Correto! Harry Potter é o personagem principal da série criada por J.K. Rowling.")
    acertos += 1
else:
    print(Fore.RED + "Errado! A resposta correta é (c) Harry Potter.")
    print(Fore.CYAN + "Ele é o 'menino que sobreviveu', protagonista da história.")

print(Fore.YELLOW + "\n2) Em que escola de magia Harry estuda?")
print('\n (a) Durmstrang\n (b) Ilvermorny\n (c) Hogwarts\n (d) Beauxbatons\n (e) Avalon\n> ')
resposta2 = input("> ")

if resposta2.lower() == "c":
    print(Fore.CYAN + "Correto! Hogwarts é a escola de magia onde Harry e seus amigos estudam e enfrentam muitos desafios.")
    acertos += 1
else:
    print(Fore.RED + "Errado! A resposta correta é (c) Hogwarts")
    print(Fore.CYAN + "Hogwarts é a escola mais renomada do Reino Unido, dividida em quatro casas: Grifinória, Sonserina, Lufa-Lufa e Corvinal.")

print(Fore.YELLOW + "\n3) Quem são os melhores amigos de Harry?")
print("\n (a) Draco e Crabbe\n (b) Neville e Luna\n (c) Rony e Hermione\n (d) Sirius e Lupin\n (e) Fred e George\n> ")
resposta3 = input("> ")

if resposta3.lower() == "c":
    print(Fore.CYAN + "Correto! Rony e Hermione são os melhores amigos de Harry e o acompanham em todas as suas aventuras.")
    acertos += 1
else:
    print(Fore.RED + "Errado! A resposta correta é (c) Rony e Hermione")
    print(Fore.CYAN + "Rony é leal e sempre ao lado de Harry, enquanto Hermione traz inteligência e coragem para o grupo.")

print(Fore.YELLOW + "\n4) Qual casa de Hogwarts tem como símbolo um leão?")
print("\n (a) Sonserina\n (b) Lufa-Lufa\n (c) Corvinal\n (d) Grifinória\n (e) Durmstrang\n> ")
resposta4 = input("> ")

if resposta4.lower() == "d":
    print(Fore.CYAN + "Correto! A Grifinória tem como símbolo o leão, representando coragem e bravura.")
    acertos += 1
else:
    print(Fore.RED + "Errado! A resposta certa é (d) Grifinória")
    print(Fore.CYAN + "A Grifinória é conhecida por sua coragem e determinação, sendo representada pelo leão.")

print(Fore.YELLOW + "\n5) Quem é o diretor de Hogwarts na maior parte da saga?")
print("\n (a) Severus Snape\n (b) Alvo Dumbledore\n (c) Minerva McGonagall\n (d) Gilderoy Lockhart\n (e) Hagrid\n> ")
resposta5 = input("> ")

if resposta5.lower() == "b":
    print("Correto! Alvo Dumbledore é o diretor de Hogwarts durante a maior parte da saga.")
    acertos += 1
else:
    print(Fore.RED + "Errado! A resposta correta é (b) Alvo Dumbledore")
    print(Fore.CYAN + "Dumbledore é uma figura chave no mundo bruxo, famoso por sua sabedoria e liderança.")

print(Fore.YELLOW + "\n6) Quem entrega a carta de Hogwarts para Harry no primeiro livro?")
print("\n (a) Dumbledore\n (b) Minerva\n (c) Hagrid\n (d) Snape\n> ")
resposta6 = input("> ")

if resposta6.lower() == "c":
    print("Correto! Hagrid entrega a carta de Hogwarts para Harry no primeiro livro.")
    acertos += 1
else:
    print(Fore.RED + "Errado! A resposta correta é (c) Hagrid")
    print(Fore.CYAN + "Hagrid vai até a casa dos Dursley para entregar pessoalmente a carta de Harry. ")

print(Fore.YELLOW +"\n7) Qual é o animal de estimação de Harry?")
print("\n (a) Coruja\n (b) Rato\n (c) Gato\n (d) Sapo\n> ")
resposta7 = input("> ")

if resposta7.lower() == "a":
    print("Correto! A coruja de Harry é Edwiges, seu fiel animal de estimação.")
    acertos += 1
else:
    print(Fore.RED + "Errado! A resposta correta é (a) Coruja")
    print(Fore.CYAN + "Edwiges é uma coruja branca que acompanha Harry em todas as suas aventuras.")

print(Fore.YELLOW + "\n8) Quem é o Ele-Que-Não-Deve-Ser-Nomeado?")
print("\n (a) Hagrid\n (b) Voldemort\n (c) Dobby\n (d) Dumbledore\n> ")
resposta8 = input("> ")

if resposta8.lower() == "b":
    print(Fore.CYAN + "Correto! O Ele-Que-Não-Deve-Ser-Nomeado é Voldemort, o maior bruxo das trevas da história.")
    acertos += 1
else:
    print(Fore.RED + "Errado! A resposta correta é (b) Voldemort")
    print(Fore.CYAN + "Voldemort é o bruxo das trevas que aterrorizou o mundo bruxo e é o principal vilão da série.")

print(Fore.YELLOW + "\n9) Qual é o feitiço usado para iluminar a varinha?")
print("\n (a) Alohomora\n (b) Lumus\n (c) Nox\n (d) Expelliarmus\n> ")
resposta9 = input("> ")

if resposta9.lower() == "b":
    print(Fore.CYAN + "Correto! O feitiço para iluminar a varinha é Lumos.")
    acertos += 1
else:
    print(Fore.RED + "Errado! A resposta correta é (b) Lumus")
    print(Fore.CYAN + "Lumos é o feitiço que ilumina a ponta da varinha, funcionando como uma lanterna mágica.")

print(Fore.YELLOW + "\n10) Qual é o esporte jogado em vassouras em Hogwarts?")
print("\n (a) Basquete\n (b) Xadrez mágico\n (c) Quadribol\n (d) Snap explosivo\n> ")
resposta10 = input("> ")

if resposta10.lower() == "c":
    print(Fore.CYAN + "Correto!  Quadribol é o esporte jogado em vassouras em Hogwarts.")
    acertos += 1
else:
    print(Fore.RED + "Errado! A resposta correta é (c) Quadribol")
    print(Fore.CYAN + "Quadribol é o esporte mais famoso do mundo bruxo, e Harry é apanhador do time da Grifinória.")


# Resultado final
print(f"\nVocê acertou {acertos} de 10 perguntas.")

if acertos > 8:
    print("Parabéns! Você passou para o próximo nível! 🎉")
    print("⚡ Nível Médio (2 pontos cada")
else:
    print("Tente novamente. Você ainda não passou. 💪")


print(Fore.YELLOW + "\n11) Qual é o patrono de Harry Potter?")
print("\n (a) Veado\n (b) Lobo\n (c) Corça\n (d) Cervo")
resposta11 = input("> ")

if resposta11.lower() == "a":
    print(Fore.CYAN + "Correto! O patrono de Harry Potter é um veado. ")
    acertos += 2
else:
    print(Fore.RED + "Errado! A resposta certa é (a) Cervo")
    print(Fore.CYAN + "O patrono de Harry Potter é um veado, que representa sua conexão com seu pai, James Potter, cuja forma de patrono também era um veado.")

print(Fore.YELLOW + "\n12) Quem mata Sirius Black?")
print("\n (a) Bellatrix Lestrange\n (b) Lucius Malfoy\n (c) Voldemort\n (d) Snape\n> ")
resposta12 = input("> ")

if resposta12.lower() == "a":
    print(Fore.CYAN + "Correto! Bellatrix Lestrange mata Sirius Black no Ministério da Magia. ")
    acertos +=2
else:
    print(Fore.RED + "Errado! A resposta correta é (a) Bellatrix Lestrange.")
    print(Fore.CYAN + "Sirius Black é morto por Bellatrix Lestrange durante a batalha no Ministério da Magia no quinto livro.")

print(Fore.YELLOW + "\n13) Qual é o nome da professora de Trato das Criaturas Mágicas no terceiro livro?")
print("\n (a) Minerva McGonagall\n (b) Sibila Trelawney\n (c) Pomona Sprout\n (d) Rúbeo Hagrid\n> ")
resposta13 = input("> ")

if resposta13.lower() == "d":
    print(Fore.CYAN + "Correto! Hagrid é o professor de Trato das Criaturas Mágicas no terceiro livro")
    acertos += 2
else:
    print(Fore.RED + "Errado! A resposta correta é (d) Rubeus Hagrid.")
    print(Fore.CYAN + "Hagrid é o professor de Trato das Criaturas Mágicas e tem uma grande paixão por todas as criaturas mágicas.")

print(Fore.YELLOW + "\n14) Quem é o 'Príncipe Mestiço?' ")
print("\n (a) Harry Potter\n (b) Tom Riddle\n (c) Severus Snape\n (d) Draco Malfoy\n> ")
resposta14 = input("> ")

if resposta14.lower() == "b":
    print(Fore.CYAN + "Correto! O 'Príncipe Mestiço' é Tom Riddle, que mais tarde se tornaria Lord Voldemort. ")
    acertos += 2
else:
    print(Fore.RED + "Errado! A resposta correta é (b) Tom Riddle.")
    print(Fore.CYAN + "Tom Riddle é o verdadeiro 'Príncipe Mestiço' e usou esse pseudônimo quando era estudante em Hogwarts.")
    
# Para a música
pygame.mixer.music.stop()
