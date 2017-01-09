# -*-coding:Latin-1 -*

__author__ = "abdelmajid"
__date__ = "$13 juin 2015 17:50:12$"

dictionnaire1={
"contenu":{
"0":"""
Il est toujours possible, à partir d’un automate fini non déterministe A, de
construire un automate fini déterministe A0 reconnaissant le même langage :
""",
"00bold":"Théorème 3.5.1.",
"1":"""Pour tout automate fini A, il existe un automate fini déterministe
A' reconnaissant le même langage.

La méthode de construction est appelée la construction par sous-ensembles
en français, et powerset construction en anglais.
""",
"2":"""
    Soit A= (Q, F, I, T, A) un automate fini.
On construit l'automate A' comme suit :
 - l'ensemble d'états de A' est l'ensemble P=2Q des parties de l'ensemble Q.
 - l'état initial de A' est I.
 - les états terminaux de A' sont les parties F' de Q qui ont une intersection non vide avec F.
 - la fonction de transition de A' est définie, pour Q' inclut dans Q et a de A, par
     S.a={s' de Q| il existe s de S : (s,a,s') de F}.
     
 L'automate A' est déterministe par construction.
 
 Le nombre d'états de l'automate déterminisé peut être exponentiel par
rapport au nombre d'états de l'automate de départ.
"""
}
}
