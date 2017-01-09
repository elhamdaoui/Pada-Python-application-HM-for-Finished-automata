# -*-coding:Latin-1 -*
__author__ = "abdelmajid"
__date__ = "$13 juin 2015 16:19:16$"

dictionnaire1={
"subsection0":{
"titre":"Mot",
"contenu":{
"0":"""Un alphabet A est un ensemble, en g�n�ral suppos� fini et non vide. Ses �l�ments
sont des lettres.
"""
}
},
"subsection1":{
"titre":"Alphabet",
"contenu":{
"0":"""Un mot sur un alphabet A est une suite finie d'�l�ments de A. Un mot est not�
par la juxtaposition de ses lettre. La longueur d'un mot est le nombre d'�l�ments
qui le composent. La suite vide, mot de longueur 0 souvent not�e �(epsilon), est appel�e le
mot vide. L'ensemble des mots sur A est not� A*. La concat�nation de deux mots u
= a1...an et v = b1...bn est le mot uv=a1...anb1...bn obtenu par juxtaposition.
En particulier, u�=�u=u. La concat�nation est associative, et par cons�quent A*
est un mono�de.
"""
}
}
,
"subsection2":{
"titre":"Automate fini",
"contenu":{
"0":"""Un automate fini ou automate fini non d�terministe (AFN) A sur un alphabet A est :
soit un quintuplet A=(Q, F, I, T, A), o� :
Q est un ensemble fini d'�tats.
- F in Q est un ensemble d'�tats finals ou terminaux.
- I in Q est l'ensemble des �tat initiaux.
- T in (Q*A*Q) est l'ensemble des transitions.
- A un alphabet.

soit un quintuplet A=(Q, I, F, S, A), o� :
- Q est un ensemble fini d'�tats.
- F in Q est un ensemble d'�tats finals ou terminaux.
- I in Q est l'ensemble des �tat initiaux.
- T est la fonction de transition.
- A un alphabet.

Une transition f=(p,a,q) est compos�e d'un �tat de d�part p, d'une �tiquette
a et d'un �tat d'arriv�e q. Un calcul c (on dit aussi un chemin ou une trace)
est une suite de transitions cons�cutives : c=(p0;a1;p1)(p1;a2;p2)...(pn1;an;pn).
Son �tat de d�part est p0, son �tiquette est le mot a1a2...an et son �tat d'arriv�e
est pn. Un calcul est r�ussi si son �tat de d�part est un des �tats initiaux, et son
�tat d'arriv�e est un des �tats terminaux.

Un mot w est reconnu ou accept� par l'automate s'il est l'�tiquette d'un
calcul r�ussi. Le langage reconnu par l'automate est l'ensemble des mots reconnus.
Un langage est reconnaissable s'il est reconnu par un automate fini.
Le langage reconnu par un automate A est d�not� g�n�ralement par L(A).
"""
}
},
"subsection3":{
"titre":"Automate complet, automate �mond�",
"contenu":{
"0":"""Un automate est complet si pour tout �tat q, et pour toute lettre a, il existe
au moins une transition partant de q et portant l'�tiquette a.
- Un �tat q est accessible s'il existe un chemin d'un �tat initial � q.
- Un �tat q est coaccessible s'il existe un chemin de q � un �tat final.
- Un automate est accessible (coaccessible) si tous ses �tats sont accessibles (coaccessibles).
- Un automate est �mond� si tous ses �tats sont � la fois accessibles et coaccessibles.
"""
}
},
"subsection4":{
"titre":"Automate finis d�terministe",
"contenu":{
"0":"""Un automate fini d�terministe (AFD) A sur un alphabet U est un automate fini
qui v�rifie les deux conditions suivantes :
-> il poss�de un seul �tat initial.
-> pour tout �tat q, et pour toute lettre a, il existe au plus une transition partant de q et portant l'�tiquette a.

Pour un automate d�terministe, la fonction de transition S: Q * U -> Q est la fonction partielle d�finie par :
S(q,a)=q' si (q,a,q') est une transition. Si la fonction de transition est partout
d�finie, l'automate est complet. La fonction de transition S est �tendue en une
application (partielle) Q * U* ->Q en posant :
- S(q,�)=q pour tout �tat q. Ici � d�note le mot vide.
- S(q,wa)=S(S(q,w),a) pour tout �tat q, tout mot w et toute lettre a.
"""
}
}
}
