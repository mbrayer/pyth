#!/usr/bin/env python3.8
import random
tableau_jeu=[]

#init de la liste de 10 elements
for i in range(0,10):
	tableau_jeu.append(random.randint(1,10))

##saisie du nombre
saisie=int(input("votre nombre entre 1 et 10 : "))
lg_tableau_jeu=len(tableau_jeu)

# curseur position dans le tableau
pos=0

# on parcourt la liste tant que la valeur n'as pas ete trouvé et que l'on ne depasse pas la taille du tableau
while ((pos<lg_tableau_jeu) and (tableau_jeu[pos] != saisie)):
	pos+=1
if (pos<lg_tableau_jeu):
	print("gagne")
else:
	print("perdu")

print("\ncontrole visuel")
# affiche resultat
for tirage in tableau_jeu:
	print(tirage,end=",")
print()

