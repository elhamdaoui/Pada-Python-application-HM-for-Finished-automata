# -*-coding:Latin-1 -*

__author__ = "abdelmajid"
__date__ = "$14 juin 2015 04:33:25$"

dictionnaire1 = {
"subsection0":{
"titre":" ",
"contenu":{
"0bold":"""
Th�or�me 3.9.1. """,
"1":"""Tout langage reconnaissable est reconnu par un unique (au renommage
pr�s des �tats) automate d�terministe complet tel que tout autre automate
d�terministe complet a au moins autant d'�tats que lui.

   L'automate d�crit ci-dessus est appel� automate minimal complet ou plus
simplement automate minimal reconnaissant le langage.

   Deux automates finis sont �quivalents s'ils reconnaissent le m�me langage. C'est
un r�sultat remarquable de la th�orie qu'il existe, pour tout automate fini, un seul
automate fini d�terministe minimal (c'est-�-dire ayant un nombre minimal d'�tat)
qui est �quivalent � l'automate donn�. De plus, cet automate, appel� automate
minimal, se calcule efficacement par l'algorithme de Moore (d'une complexit� en
O(n2) quadratique), l'algorithme de Hopcroft (Sa complexit� dans le pire est nlog(n)),
ou l'algorithme de Brzozowski (Sa complexit� dans le pire est exponentielle;).

L'unicit� de l'automate ayant un nombre minimal d'�tat n'est plus vraie pour les automates
non d�terministes.

On peut ainsi d�cider de l'�quivalence de deux automates en calculant, pour
chacun, l'automate minimal d�terministe correspondant, et en testant l'�galit� des
deux automates obtenus.
"""
}
},
"subsection1":{
"titre":"Equivalence de N�rode",
"contenu":{
"0":"""
D�finition : �tant donn�s un automate Aut, des �tats p et q et un
entier n >= 0, notons :
1. p [=] q le fait que p et q ne sont s�par�s par aucun mot
2. p [=n] q le fait que p et q ne sont s�par�s par aucun mot de
longueur inf�rieure ou �gale � n.
La relation [=] (d�finie sur les �tats de Aut) est appel�e Relation de
N�rode.
Lemme : ?tant donn� un automate Aut, les relations [=] et [=n]
(pour tout entier n >= 0) sont des relations d��quivalence (i.e.
r�flexive, sym�trique et transitive).

Lemme : Pour un automate de k �tats :
  1. pour tout entier n >= 0, p [=n+1] q si et seulement si p [=n] q et
pour toute lettre a, S(p,a) [=n] S(q,a) ,(S est la fonction du transition).
  2. il existe un entier n avec 0 <= n >= k tel que [=n]=[=n+1] (i.e.
pour tous �tats p et q, p [=n] q si et seulement si p [=n+1] q) et
pour tout entier m >= n, [=m] = [=n] = [=];
  3. Si [=n]=[=n+1] alors [=n+1] = [=n+2].
"""
}
},
"subsection2":{
"titre":"Algorithme de Moore",
"contenu":{
"0":"""
Donn�e : un automate complet d�terministe accessible
R�sultat : l'�quivalence de N�rode et l'automate minimal
reconnaissant le langage reconnu par l'automate donn�
Principe g�n�ral : l'algorithme calcule lettre par lettre les mots
s�parant des �tats (il calcule donc les classes d'�quivalences des
relations [=n]). Apr�s examen de chaque longueur de mot possible,
un bilan est fait : il consiste � attribuer un num�ro (en chiffre
romain) � chaque classe de [=n].

Construire un tableau dont les colonnes sont les diff�rents
�tats de l'automate de d�part.

La premi�re ligne de bilan s'obtient en s�parant (par �) les
�tats d'acceptation et les autres en deux classes.
  * Num�roter I l'�tat de la premi�re colonne ;
  * Num�roter I ou II les �tats des autres colonnes de mani�re que
    tous les �tats d'acceptation soient num�rot�s de la m�me
    mani�re, et que tous les �tats non d'acceptation soient
    num�rot�es de l'autre mani�re.
    
Les lignes suivantes du tableau sont construites une par une en
regardant, pour chaque �tat, dans quel �tat m�ne la transition
par une lettre de A et en notant la classe � laquelle appartient
cet �tat dans la ligne bilan pr�c�dente. Cette op�ration est
r�alis�e � raison d'une ligne par lettre de A:

Un nouveau bilan est effectu� qui prend en compte le bilan
pr�c�dent et toutes les lignes que l'on vient de calculer : deux
colonnes diff�rentes donnent deux classes diff�rentes. La ligne
obtenue fait le bilan de tout ce qui pr�c�de et c'est avec elle
que l'on recommence. L� encore, les classes sont num�rot�es
en chiffres romains � partir de la gauche.

On r�p�te les deux op�rations qui pr�c�dent jusqu'� obtenir
deux lignes de bilan successives identiques.

Les �tats de l'automate minimal complet sont les classes de la
derni�re ligne de bilan.

Les transitions se trouvent dans le tableau entre lavant-derni�re 
et la derni�re ligne de bilan.

L'�tat de d�part est la classe contenant l'�tat de d�part de
l'automate d�terministe.

Les �tats d'acceptation sont les classes contenant des �tats
d'acceptation de l'automate initial ; puisque � s�pare les �tats
d'acceptation des autres, une classe ne contient soit que des
�tats d'acceptation, soit aucun �tat d'acceptation.

""",
"00bold":""" Exemple:
""",
"01image":"imgs/ex1_moore_c.gif",
"02image":"imgs/ex2_moore.gif",
"1":"""
On s'arr�te car on a deux fois le m�me bilan.
"""

}
}
}
