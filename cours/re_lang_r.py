# -*-coding:Latin-1 -*

__author__ = "abdelmajid"
__date__ = "$14 juin 2015 03:44:12$"

dictionnaire1 = {
"contenu":{
"0":"""
   Les expressions rationnelles, ou expressions régulières sont des expressions qui
décrivent les langages rationnels. Le terme expression régulière est antérieur, et
les langages décrits par ces expressions sont naturellement aussi appelés langages
réguliers. Les expressions rationnelles, plus ou moins étendues, servent notamment
à la recherche de motifs dans un texte.
"""
},
"subsection0":{
"titre":"Expressions rationnelles",
"contenu":{
"0":"""
Une expression rationnelle E sur un alphabet A est soit :
- Un symbole dénotant le mot vide : £ ou 1.
- une lettre <a> de l'alphabet A.
- une réunion (ou somme, en notation algébrique) de deux expressions rationnelles
M et N, notée E = M|N ou E = M+N.
- une concaténation (ou un produit, en notation algébrique) de deux expressions
rationnelles M et N, notée E = M.N ou simplement E = MN.
- une répétition, ou étoile, ou itération, d'une expression rationnelle M notée
E = M*.
"""
}
},
"subsection1":{
"titre":"Construction d-automates finis à partir des expressions rationnelles",
"contenu":{
"0":"""
   Il existe plusieurs méthodes pour construire un automate fini à partir d’une
expression rationnelle :

""",
"0bold":"   la méthode de Thompson",
"1":""" Elle a été utilisée par Ken Thompson dans l'implémentation
de la commande grep du système Unix. On construit récursivement
des automates pour les composants d'une expression. La forme particulière des
automates permet de les combiner avec une grande facilité. L'automate obtenu est
non déterministe asynchrone.

""",
"1bold":"   la méthode de Glushkov",
"2":""" Cette méthode, attribuée à l'informaticien Glushkov,
permet de construire un automate non déterministe de même taille (nombre d'états)
que la taille (nombre de symboles) de l'expression rationnelle. Il a été
observé que l'automate de Glushkov est le même que l'automate obtenu en supprimant
les £-transitions de l'automate de Thompson.

""",
"2bold":"   la méthode des quotients ou résiduels ou dérivées, due à Brzozowski",
"3":""" On
forme les quotients (ou résiduels) successifs de l'expression. Il n'y en a qu'un
nombre fini de différents, après application d'un certain nombre de règles de simplification
qui sont l'associativité, la commutativité et l'idempotente de l'opération +.


    Aucune de ces méthodes ne donne directement l'automate minimal d'un langage.
On peut aussi employer des constructions simples d'automates pour la réunion, le
produit et l'étoile de langages, et opérer récursivement.

    Soit A(M) (respectivement A(N)) l'automate fini reconnaissant le langage
dénoté par l'expression rationnelle M (respectivement N). Les constructions sont
les suivantes :

- Automate A(M|N) pour la réunion :
Il suffit de faire la réunion disjointe des automates A(M) et A(N).
- Automate A(M.N) pour le produit :
L'automate a pour états les états de A(M) et de A(N). Les états initiaux
sont ceux de A(M), les terminaux sont ceux de A(N). Les transitions sont
celles de A(M) et de A(N), et de plus des £-transitions des états terminaux
de A(M) vers les états initiaux de A(N).

Automate A(M*) pour l'étoile :
On part de l'automate A(M) que l'on augmente de deux états <i> et <t>. On
ajoute des £-transitions.
- de <i> à tout état initial de A(M)
- de tout état final de A(M) à <t>
- de <i> à <t> et de <t> à <i>.
L'état <i> (resp. <t>) est l'état initial (resp. final) de A(M*).
"""
}
},
"subsection2":{
"titre":"Convertion d'un automate en une expression régulière",
"contenu":{
"0bold":"""
Théorème 3.8.1. """,
"1":"""Un langage est rationnel si, et seulement si, il est reconnaissable.

""",
"1bold":"""Algorithme d'élimination de Brzozowski-McCluskey
""",
"2":"""On décrit ici un algorithme qui permet de déterminer un expression régulière
correspondant au langage reconnu par un automate standard.

- On standardise l'automate en ajoutant au besoin un état initial et final (voir
l'algorithme de Thompson pour un exemple).
- On considère chaque transition étiquetée avec une expression régulière (et
donc pas seulement avec des caractères ou £) puis on fusionne les transitions
entre deux mêmes états.

- On élimine chaque état autre que l'état initial et l'état final. Pour éliminer
un état <q1>, on considère tout couple (<q0> , <q2>) tel qu'il existe une transition
de <q0> vers <q1> (étiquetée avec l'expression <e>) et une transition de <q1> vers <q2>
(étiquetée avec l'expression <g>) ; notons <f> l'expression de l'éventuelle transition
de <q1> vers <q1> et <h> l'expression de l'éventuelle transition de <q0> vers <q2>.
On crée alors lors de l'élimination de <q1> (et des transitions associées) une
transition de <q0> vers <q2> étiquetée <ef*g+h>.

-L'expression régulière étiquetant la transition entre l'état initial et l'état
final s'interprète en le langage reconnu par l'automate initial..
"""
}
}
}
