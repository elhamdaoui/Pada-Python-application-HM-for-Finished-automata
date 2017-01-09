# -*-coding:Latin-1 -*

__author__ = "abdelmajid"
__date__ = "$14 juin 2015 04:33:25$"

dictionnaire1 = {
"subsection0":{
"titre":" ",
"contenu":{
"0bold":"""
Théorème 3.9.1. """,
"1":"""Tout langage reconnaissable est reconnu par un unique (au renommage
près des états) automate déterministe complet tel que tout autre automate
déterministe complet a au moins autant d'états que lui.

   L'automate décrit ci-dessus est appelé automate minimal complet ou plus
simplement automate minimal reconnaissant le langage.

   Deux automates finis sont équivalents s'ils reconnaissent le même langage. C'est
un résultat remarquable de la théorie qu'il existe, pour tout automate fini, un seul
automate fini déterministe minimal (c'est-à-dire ayant un nombre minimal d'état)
qui est équivalent à l'automate donné. De plus, cet automate, appelé automate
minimal, se calcule efficacement par l'algorithme de Moore (d'une complexité en
O(n2) quadratique), l'algorithme de Hopcroft (Sa complexité dans le pire est nlog(n)),
ou l'algorithme de Brzozowski (Sa complexité dans le pire est exponentielle;).

L'unicité de l'automate ayant un nombre minimal d'état n'est plus vraie pour les automates
non déterministes.

On peut ainsi décider de l'équivalence de deux automates en calculant, pour
chacun, l'automate minimal déterministe correspondant, et en testant l'égalité des
deux automates obtenus.
"""
}
},
"subsection1":{
"titre":"Equivalence de Nérode",
"contenu":{
"0":"""
Définition : étant donnés un automate Aut, des états p et q et un
entier n >= 0, notons :
1. p [=] q le fait que p et q ne sont séparés par aucun mot
2. p [=n] q le fait que p et q ne sont séparés par aucun mot de
longueur inférieure ou égale à n.
La relation [=] (définie sur les états de Aut) est appelée Relation de
Nérode.
Lemme : ?tant donné un automate Aut, les relations [=] et [=n]
(pour tout entier n >= 0) sont des relations d’équivalence (i.e.
réflexive, symétrique et transitive).

Lemme : Pour un automate de k états :
  1. pour tout entier n >= 0, p [=n+1] q si et seulement si p [=n] q et
pour toute lettre a, S(p,a) [=n] S(q,a) ,(S est la fonction du transition).
  2. il existe un entier n avec 0 <= n >= k tel que [=n]=[=n+1] (i.e.
pour tous états p et q, p [=n] q si et seulement si p [=n+1] q) et
pour tout entier m >= n, [=m] = [=n] = [=];
  3. Si [=n]=[=n+1] alors [=n+1] = [=n+2].
"""
}
},
"subsection2":{
"titre":"Algorithme de Moore",
"contenu":{
"0":"""
Donnée : un automate complet déterministe accessible
Résultat : l'équivalence de Nérode et l'automate minimal
reconnaissant le langage reconnu par l'automate donné
Principe général : l'algorithme calcule lettre par lettre les mots
séparant des états (il calcule donc les classes d'équivalences des
relations [=n]). Après examen de chaque longueur de mot possible,
un bilan est fait : il consiste à attribuer un numéro (en chiffre
romain) à chaque classe de [=n].

Construire un tableau dont les colonnes sont les différents
états de l'automate de départ.

La première ligne de bilan s'obtient en séparant (par £) les
états d'acceptation et les autres en deux classes.
  * Numéroter I l'état de la première colonne ;
  * Numéroter I ou II les états des autres colonnes de manière que
    tous les états d'acceptation soient numérotés de la même
    manière, et que tous les états non d'acceptation soient
    numérotées de l'autre manière.
    
Les lignes suivantes du tableau sont construites une par une en
regardant, pour chaque état, dans quel état mène la transition
par une lettre de A et en notant la classe à laquelle appartient
cet état dans la ligne bilan précédente. Cette opération est
réalisée à raison d'une ligne par lettre de A:

Un nouveau bilan est effectué qui prend en compte le bilan
précédent et toutes les lignes que l'on vient de calculer : deux
colonnes différentes donnent deux classes différentes. La ligne
obtenue fait le bilan de tout ce qui précède et c'est avec elle
que l'on recommence. Là encore, les classes sont numérotées
en chiffres romains à partir de la gauche.

On répète les deux opérations qui précèdent jusqu'à obtenir
deux lignes de bilan successives identiques.

Les états de l'automate minimal complet sont les classes de la
dernière ligne de bilan.

Les transitions se trouvent dans le tableau entre lavant-dernière 
et la dernière ligne de bilan.

L'état de départ est la classe contenant l'état de départ de
l'automate déterministe.

Les états d'acceptation sont les classes contenant des états
d'acceptation de l'automate initial ; puisque £ sépare les états
d'acceptation des autres, une classe ne contient soit que des
états d'acceptation, soit aucun état d'acceptation.

""",
"00bold":""" Exemple:
""",
"01image":"imgs/ex1_moore_c.gif",
"02image":"imgs/ex2_moore.gif",
"1":"""
On s'arrête car on a deux fois le même bilan.
"""

}
}
}
