# -*-coding:Latin-1 -*

__author__ = "abdelmajid"
__date__ = "$13 juin 2015 17:50:12$"

dictionnaire1={
"contenu":{
"0":"""
Il est toujours possible, � partir d�un automate fini non d�terministe A, de
construire un automate fini d�terministe A0 reconnaissant le m�me langage :
""",
"00bold":"Th�or�me 3.5.1.",
"1":"""Pour tout automate fini A, il existe un automate fini d�terministe
A' reconnaissant le m�me langage.

La m�thode de construction est appel�e la construction par sous-ensembles
en fran�ais, et powerset construction en anglais.
""",
"2":"""
    Soit A= (Q, F, I, T, A) un automate fini.
On construit l'automate A' comme suit :
 - l'ensemble d'�tats de A' est l'ensemble P=2Q des parties de l'ensemble Q.
 - l'�tat initial de A' est I.
 - les �tats terminaux de A' sont les parties F' de Q qui ont une intersection non vide avec F.
 - la fonction de transition de A' est d�finie, pour Q' inclut dans Q et a de A, par
     S.a={s' de Q| il existe s de S : (s,a,s') de F}.
     
 L'automate A' est d�terministe par construction.
 
 Le nombre d'�tats de l'automate d�terminis� peut �tre exponentiel par
rapport au nombre d'�tats de l'automate de d�part.
"""
}
}
