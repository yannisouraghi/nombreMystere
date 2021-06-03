#Niveau 1

#Importation bibliothèque random
from random import *
#Initialisation du nombre mystère
rand = randint(1,100)
nombreChoisis = input("Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel je pense, il se situe entre 1 et 100 : ")
nombreChoisis = int(nombreChoisis)
#Boucle while infini
while True:
    if nombreChoisis == rand :
        print("C'est ça")
        #Met fin au programme
        break
    if nombreChoisis < rand :
        print("C est plus")
    if nombreChoisis > rand :
        print("C est moins")
    nombreChoisis = input("Choisissez un nombre : ")
    nombreChoisis = int(nombreChoisis)

#Niveau 2

#Importation bibliothèque random et time
import time
from random import *
#J'ai initialiser l'heure au moment de l'execution de end à laquel j'ai ajouter 60 secondes afin d'avoir un delai de 1 minute
end = time.time() + 60
rand = randint(1,100)
nombreChoisis = input("Bienvenue sur le célèbre jeu du juste prix, tu dois deviner le prix auquel je pense, il se situe entre 1 et 100 : ")
nombreChoisis = int(nombreChoisis)
tentatives = 1
while True:
    if nombreChoisis == rand :
        print("C'est ça")
        break
    if nombreChoisis < rand :
        print("C est plus")
    if nombreChoisis > rand :
        print("C est moins")
    nombreChoisis = input("Choisissez un nombre : ")
    nombreChoisis = int(nombreChoisis)
    tentatives +=1
    if(tentatives > 4):
        print("C'est perdu")
        #Arrete le programme au bout de 5 tentatives
        break
    if(time.time() >= end ):
        print("Trop tard")
        break
        #Arrete le programme au bout de 1 minute

#Niveau 3

from Tkinter import *

fenetre = Tk()
fenetre.config(bg = #0e20)

#Impossible de proceder à la compilation
