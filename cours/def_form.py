# -*-coding:Latin-1 -*
__author__ = "abdelmajid"
__date__ = "$13 juin 2015 16:19:16$"

dictionnaire1={
"subsection0":{
"titre":"Mot",
"contenu":{
"0":"""Un alphabet A est un ensemble, en général supposé fini et non vide. Ses éléments
sont des lettres.
"""
}
},
"subsection1":{
"titre":"Alphabet",
"contenu":{
"0":"""Un mot sur un alphabet A est une suite finie d'éléments de A. Un mot est noté
par la juxtaposition de ses lettre. La longueur d'un mot est le nombre d'éléments
qui le composent. La suite vide, mot de longueur 0 souvent notée £(epsilon), est appelée le
mot vide. L'ensemble des mots sur A est noté A*. La concaténation de deux mots u
= a1...an et v = b1...bn est le mot uv=a1...anb1...bn obtenu par juxtaposition.
En particulier, u£=£u=u. La concaténation est associative, et par conséquent A*
est un monoïde.
"""
}
}
,
"subsection2":{
"titre":"Automate fini",
"contenu":{
"0":"""Un automate fini ou automate fini non déterministe (AFN) A sur un alphabet A est :
soit un quintuplet A=(Q, F, I, T, A), où :
Q est un ensemble fini d'états.
- F in Q est un ensemble d'états finals ou terminaux.
- I in Q est l'ensemble des état initiaux.
- T in (Q*A*Q) est l'ensemble des transitions.
- A un alphabet.

soit un quintuplet A=(Q, I, F, S, A), où :
- Q est un ensemble fini d'états.
- F in Q est un ensemble d'états finals ou terminaux.
- I in Q est l'ensemble des état initiaux.
- T est la fonction de transition.
- A un alphabet.

Une transition f=(p,a,q) est composée d'un état de départ p, d'une étiquette
a et d'un état d'arrivée q. Un calcul c (on dit aussi un chemin ou une trace)
est une suite de transitions consécutives : c=(p0;a1;p1)(p1;a2;p2)...(pn1;an;pn).
Son état de départ est p0, son étiquette est le mot a1a2...an et son état d'arrivée
est pn. Un calcul est réussi si son état de départ est un des états initiaux, et son
état d'arrivée est un des états terminaux.

Un mot w est reconnu ou accepté par l'automate s'il est l'étiquette d'un
calcul réussi. Le langage reconnu par l'automate est l'ensemble des mots reconnus.
Un langage est reconnaissable s'il est reconnu par un automate fini.
Le langage reconnu par un automate A est dénoté généralement par L(A).
"""
}
},
"subsection3":{
"titre":"Automate complet, automate émondé",
"contenu":{
"0":"""Un automate est complet si pour tout état q, et pour toute lettre a, il existe
au moins une transition partant de q et portant l'étiquette a.
- Un état q est accessible s'il existe un chemin d'un état initial à q.
- Un état q est coaccessible s'il existe un chemin de q à un état final.
- Un automate est accessible (coaccessible) si tous ses états sont accessibles (coaccessibles).
- Un automate est émondé si tous ses états sont à la fois accessibles et coaccessibles.
"""
}
},
"subsection4":{
"titre":"Automate finis déterministe",
"contenu":{
"0":"""Un automate fini déterministe (AFD) A sur un alphabet U est un automate fini
qui vérifie les deux conditions suivantes :
-> il possède un seul état initial.
-> pour tout état q, et pour toute lettre a, il existe au plus une transition partant de q et portant l'étiquette a.

Pour un automate déterministe, la fonction de transition S: Q * U -> Q est la fonction partielle définie par :
S(q,a)=q' si (q,a,q') est une transition. Si la fonction de transition est partout
définie, l'automate est complet. La fonction de transition S est étendue en une
application (partielle) Q * U* ->Q en posant :
- S(q,£)=q pour tout état q. Ici £ dénote le mot vide.
- S(q,wa)=S(S(q,w),a) pour tout état q, tout mot w et toute lettre a.
"""
}
}
}
